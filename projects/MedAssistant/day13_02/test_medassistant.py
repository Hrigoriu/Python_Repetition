"""Tests for MedAssistant v2. Run with: python -m unittest -v"""

import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from abc import ABC, abstractmethod
from contextlib import redirect_stdout
from dataclasses import FrozenInstanceError
from pathlib import Path
from unittest.mock import patch

import main as app
from patient_record import (
    PatientRecord,
    RecordValidationError,
    SkippedRecord,
    build_records,
)
from report_utils import build_report, save_report
from statistics_utils import (
    average_age,
    average_temperature,
    calculate_statistics,
    count_adults,
    fever_records,
    oldest_record,
)

PROJECT_DIR = Path(__file__).resolve().parent

BASE = {
    "id": 1,
    "name": "Ivan",
    "age": 42,
    "diagnosis": "sinusitis",
    "temperature": 36.8,
}


def make(**overrides) -> PatientRecord:
    return PatientRecord(**{**BASE, **overrides})


class TestPatientRecordValidation(unittest.TestCase):
    def test_valid_record_keeps_its_fields(self):
        record = make()
        self.assertEqual(
            (record.id, record.name, record.age, record.diagnosis, record.temperature),
            (1, "Ivan", 42, "sinusitis", 36.8),
        )

    def test_boundary_values_are_accepted(self):
        for overrides in (
            {"temperature": 25.0},
            {"temperature": 45.0},
            {"temperature": 38},
            {"age": 1},
            {"id": 1},
        ):
            with self.subTest(overrides=overrides):
                make(**overrides)

    def test_each_bad_value_gives_exactly_one_error_naming_the_field(self):
        bad_values = {
            "id": [0, -1, "1", None, True, 1.5],
            "name": ["", "   ", None, 5],
            "age": [0, -5, "42", None, True, 42.0],
            "diagnosis": ["", "  ", None],
            "temperature": [24.9, 45.1, "37", None, True, float("nan"), float("inf")],
        }
        for field, values in bad_values.items():
            for value in values:
                with self.subTest(field=field, value=value):
                    with self.assertRaises(RecordValidationError) as ctx:
                        make(**{field: value})
                    errors = ctx.exception.errors
                    self.assertEqual(len(errors), 1)
                    self.assertTrue(errors[0].startswith(field))

    def test_all_errors_are_collected_in_field_order(self):
        with self.assertRaises(RecordValidationError) as ctx:
            PatientRecord(-1, "", -5, "", 100)
        errors = ctx.exception.errors
        self.assertEqual(len(errors), 5)
        fields = ("id", "name", "age", "diagnosis", "temperature")
        for error, field in zip(errors, fields, strict=True):
            self.assertTrue(error.startswith(field), error)

    def test_error_is_a_value_error_with_joined_message(self):
        with self.assertRaises(ValueError) as ctx:
            make(id=0, name="")
        error = ctx.exception
        self.assertIsInstance(error, RecordValidationError)
        self.assertEqual(str(error), "; ".join(error.errors))


class TestPatientRecordBehavior(unittest.TestCase):
    def test_is_adult_boundary(self):
        for age, expected in ((1, False), (17, False), (18, True), (19, True)):
            with self.subTest(age=age):
                self.assertEqual(make(age=age).is_adult(), expected)

    def test_is_fever_boundary(self):
        for temperature, expected in (
            (36.6, False),
            (37.4, False),
            (37.5, True),
            (37.6, True),
            (38, True),
        ):
            with self.subTest(temperature=temperature):
                self.assertEqual(make(temperature=temperature).is_fever(), expected)

    def test_summary_text(self):
        self.assertEqual(
            make().summary(),
            "#1 Ivan (42, adult) — sinusitis, 36.8°C (no fever)",
        )
        self.assertEqual(
            make(id=2, name="Sofia", age=15, diagnosis="otitis", temperature=38.0).summary(),
            "#2 Sofia (15, minor) — otitis, 38.0°C (fever)",
        )

    def test_summary_returns_text_and_prints_nothing(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            result = make().summary()
        self.assertIsInstance(result, str)
        self.assertEqual(buffer.getvalue(), "")

    def test_equality_by_value(self):
        self.assertEqual(make(), make())
        self.assertNotEqual(make(), make(id=2))


class TestFromDict(unittest.TestCase):
    def test_builds_the_same_record_as_the_constructor(self):
        self.assertEqual(PatientRecord.from_dict(BASE), make())

    def test_extra_keys_are_ignored(self):
        self.assertEqual(PatientRecord.from_dict({**BASE, "ward": "ENT"}), make())

    def test_all_missing_keys_are_reported_together(self):
        with self.assertRaises(RecordValidationError) as ctx:
            PatientRecord.from_dict({"id": 1})
        self.assertEqual(
            ctx.exception.errors,
            [
                "missing key 'name'",
                "missing key 'age'",
                "missing key 'diagnosis'",
                "missing key 'temperature'",
            ],
        )

    def test_non_dict_input_is_rejected(self):
        for value in ("text", None, 5, [1, 2]):
            with self.subTest(value=value):
                with self.assertRaises(RecordValidationError) as ctx:
                    PatientRecord.from_dict(value)
                self.assertIn("JSON object", ctx.exception.errors[0])

    def test_invalid_values_are_caught_by_post_init(self):
        with self.assertRaises(RecordValidationError) as ctx:
            PatientRecord.from_dict({**BASE, "age": "61"})
        self.assertTrue(ctx.exception.errors[0].startswith("age"))

    def test_input_dict_is_not_modified(self):
        data = dict(BASE)
        PatientRecord.from_dict(data)
        self.assertEqual(data, BASE)


class TestBuildRecords(unittest.TestCase):
    def test_valid_and_invalid_are_separated(self):
        raw = [
            BASE,
            {**BASE, "id": 2, "temperature": 1000},
            "x",
            {**BASE, "id": 3, "name": "Olena"},
        ]
        records, skipped = build_records(raw)
        self.assertEqual([r.id for r in records], [1, 3])
        self.assertEqual([s.index for s in skipped], [1, 2])
        self.assertEqual([s.label for s in skipped], ["Ivan", "unnamed"])
        self.assertTrue(all(isinstance(s, SkippedRecord) for s in skipped))
        self.assertTrue(all(isinstance(s.reasons, tuple) for s in skipped))

    def test_reasons_are_kept_as_separate_items(self):
        bad = {"id": -1, "name": "", "age": 1, "diagnosis": "d", "temperature": 36.6}
        _, skipped = build_records([bad])
        self.assertEqual(len(skipped[0].reasons), 2)

    def test_empty_list_gives_empty_results(self):
        self.assertEqual(build_records([]), ([], []))

    def test_non_list_raises_value_error(self):
        for value in ({"a": 1}, "text", None, 5):
            with self.subTest(value=value), self.assertRaises(ValueError):
                build_records(value)

    def test_real_bugs_are_not_swallowed(self):
        with patch.object(PatientRecord, "from_dict", side_effect=RuntimeError("bug")), self.assertRaises(RuntimeError):
            build_records([BASE])


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.records = [
            make(id=1, age=20, temperature=36.0),
            make(id=2, age=40, temperature=38.0),
            make(id=3, age=40, temperature=37.5),
            make(id=4, age=10, temperature=39.0),
        ]

    def test_individual_functions(self):
        self.assertAlmostEqual(average_age(self.records), 27.5)
        self.assertAlmostEqual(average_temperature(self.records), 37.625)
        self.assertEqual(count_adults(self.records), 3)
        self.assertEqual([r.id for r in fever_records(self.records)], [2, 3, 4])

    def test_oldest_takes_the_first_on_a_tie(self):
        self.assertEqual(oldest_record(self.records).id, 2)

    def test_calculate_statistics_combines_everything(self):
        stats = calculate_statistics(self.records)
        self.assertEqual(stats.total, 4)
        self.assertEqual(stats.adults, 3)
        self.assertAlmostEqual(stats.average_age, 27.5)
        self.assertAlmostEqual(stats.average_temperature, 37.625)
        self.assertEqual(stats.oldest.id, 2)
        self.assertEqual([r.id for r in stats.fever_records], [2, 3, 4])

    def test_statistics_object_is_frozen(self):
        stats = calculate_statistics(self.records)
        with self.assertRaises(FrozenInstanceError):
            stats.total = 99

    def test_empty_input_fails_fast_with_a_clear_message(self):
        for function in (average_age, average_temperature, oldest_record, calculate_statistics):
            with self.subTest(function=function.__name__), self.assertRaisesRegex(ValueError, "no valid records"):
                function([])
        self.assertEqual(fever_records([]), [])
        self.assertEqual(count_adults([]), 0)


class TestReport(unittest.TestCase):
    def setUp(self):
        self.records = [
            make(id=1, name="Ivan", age=42, temperature=36.8),
            make(id=2, name="Olena", age=35, temperature=38.4),
            make(id=3, name="Sofia", age=15, diagnosis="otitis", temperature=38.0),
        ]
        self.stats = calculate_statistics(self.records)

    def test_report_without_skipped_records(self):
        report = build_report(self.stats, [])
        for expected in (
            "MEDASSISTANT PATIENT REPORT",
            "Records in file: 3",
            "Valid records: 3",
            "Skipped records: 0",
            "Average age: 30.7",
            "Average temperature: 37.7",
            "Adults: 2 of 3",
            "Oldest patient: Ivan (42)",
            "Patients with fever (>= 37.5°C): 2",
            "  - #2 Olena (35, adult) — sinusitis, 38.4°C (fever)",
            "  - #3 Sofia (15, minor) — otitis, 38.0°C (fever)",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, report)
        self.assertNotIn("Skipped records (", report)
        self.assertTrue(report.endswith("\n"))

    def test_report_counts_valid_plus_skipped_as_records_in_file(self):
        skipped = [SkippedRecord(4, "Mykola", ("missing key 'temperature'",))]
        report = build_report(self.stats, skipped)
        self.assertIn("Records in file: 4", report)
        self.assertIn("Valid records: 3", report)
        self.assertIn("Skipped records: 1", report)

    def test_skipped_section_shows_index_label_and_every_reason(self):
        skipped = [
            SkippedRecord(4, "Mykola", ("missing key 'temperature'",)),
            SkippedRecord(
                5,
                "unnamed",
                (
                    "id must be a positive integer, got -6",
                    "name must be a non-empty string, got ''",
                ),
            ),
        ]
        report = build_report(self.stats, skipped)
        for expected in (
            "Skipped records (2):",
            "  - index 4 (Mykola):",
            "      * missing key 'temperature'",
            "  - index 5 (unnamed):",
            "      * id must be a positive integer, got -6",
            "      * name must be a non-empty string, got ''",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, report)

    def test_report_with_no_fever_lists_nobody(self):
        stats = calculate_statistics([make()])
        report = build_report(stats, [])
        self.assertIn("Patients with fever (>= 37.5°C): 0", report)
        self.assertNotIn("  - #", report)

    def test_save_report_keeps_non_ascii_characters(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "report.txt"
            report = build_report(self.stats, [])
            save_report(path, report)
            self.assertEqual(path.read_text(encoding="utf-8"), report)


class TestPipeline(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.dir = Path(temp.name)
        self.data_path = self.dir / "patients.json"
        self.report_path = self.dir / "report.txt"

    def run_pipeline(self, content=None, report_path=None):
        if content is not None:
            self.data_path.write_text(content, encoding="utf-8")
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = app.main(self.data_path, report_path or self.report_path)
        return code, buffer.getvalue()

    def test_valid_and_invalid_records_still_produce_a_report(self):
        content = json.dumps([BASE, {"id": 2}, {**BASE, "id": 3, "name": "Olena"}])
        code, output = self.run_pipeline(content)
        self.assertEqual(code, 0)
        self.assertIn("⚠ 1 record(s) skipped:", output)
        self.assertIn("  index 1 (unnamed):", output)
        self.assertIn("✓ 2 valid record(s)", output)
        report = self.report_path.read_text(encoding="utf-8")
        self.assertIn("Valid records: 2", report)
        self.assertIn("Skipped records (1):", report)

    def test_all_valid_records_print_no_warning(self):
        code, output = self.run_pipeline(json.dumps([BASE]))
        self.assertEqual(code, 0)
        self.assertNotIn("skipped", output)
        self.assertTrue(self.report_path.exists())

    def test_missing_file(self):
        code, output = self.run_pipeline()
        self.assertEqual(code, 1)
        self.assertIn("✗ File not found", output)
        self.assertIn(str(self.data_path), output)
        self.assertFalse(self.report_path.exists())

    def test_broken_json_is_reported_as_invalid_json_not_as_value_error(self):
        code, output = self.run_pipeline('[{"id": 1,')
        self.assertEqual(code, 1)
        self.assertIn("✗ Invalid JSON", output)
        self.assertFalse(self.report_path.exists())

    def test_json_that_is_not_an_array(self):
        code, output = self.run_pipeline('{"id": 1}')
        self.assertEqual(code, 1)
        self.assertIn("expected a JSON array", output)
        self.assertFalse(self.report_path.exists())

    def test_empty_array_and_all_invalid_records_stop_with_a_clear_message(self):
        for content in ("[]", json.dumps([{"id": 1}, "x"])):
            with self.subTest(content=content):
                code, output = self.run_pipeline(content)
                self.assertEqual(code, 1)
                self.assertIn("no valid records", output)
                self.assertFalse(self.report_path.exists())

    def test_unwritable_report_path_names_the_report_not_the_input(self):
        bad_report = self.dir / "no_such_folder" / "report.txt"
        code, output = self.run_pipeline(json.dumps([BASE]), report_path=bad_report)
        self.assertEqual(code, 1)
        self.assertIn(str(bad_report), output)

    def test_shipped_sample_data(self):
        code, _ = self.run_pipeline_with_shipped_data()
        self.assertEqual(code, 0)
        report = self.report_path.read_text(encoding="utf-8")
        for expected in (
            "Records in file: 8",
            "Valid records: 5",
            "Skipped records: 3",
            "Average age: 36.4",
            "Average temperature: 38.0",
            "Adults: 4 of 5",
            "Oldest patient: Petro (61)",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, report)

    def run_pipeline_with_shipped_data(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = app.main(app.DATA_PATH, self.report_path)
        return code, buffer.getvalue()

    def test_script_runs_from_any_working_directory(self):
        copy = self.dir / "project_copy"
        shutil.copytree(PROJECT_DIR, copy, ignore=shutil.ignore_patterns("__pycache__", "report.*"))
        env = {**os.environ, "PYTHONUTF8": "1"}
        result = subprocess.run(
            [sys.executable, "-X", "utf8", str(copy / "main.py")],
            cwd=tempfile.gettempdir(),
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
            env=env,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("✓ Report saved: report.txt", result.stdout)
        self.assertTrue((copy / "data" / "report.txt").exists())


class self(ABC):
    """A tiny, self-contained interface with useful default implementations."""

    @property
    @abstractmethod
    def name(self):
        return getattr(self, "_name", "self")

    @abstractmethod
    def run(self):
        return {"name": self.name}

    def describe(self):
        return f"{self.name}: {self.run()}"


if __name__ == "__main__":
    unittest.main()
