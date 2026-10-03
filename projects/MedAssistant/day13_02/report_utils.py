"""report_utils.py

Turning statistics into a text report, and saving it.
"""

from pathlib import Path

from patient_record import FEVER_THRESHOLD, SkippedRecord
from statistics_utils import Statistics


def build_report(stats: Statistics, skipped: list[SkippedRecord]) -> str:
    """Build the text report. Pure formatting: no file access.

    Args:
        stats: Statistics of the valid records.
        skipped: Records that were skipped, with reasons.

    Returns:
        str: The full report text.
    """
    title = "MEDASSISTANT PATIENT REPORT"
    lines = [
        title,
        "=" * len(title),
        "",
        f"Records in file: {stats.total + len(skipped)}",
        f"Valid records: {stats.total}",
        f"Skipped records: {len(skipped)}",
        "",
        f"Average age: {stats.average_age:.1f}",
        f"Average temperature: {stats.average_temperature:.1f}",
        f"Adults: {stats.adults} of {stats.total}",
        f"Oldest patient: {stats.oldest.name} ({stats.oldest.age})",
        "",
        f"Patients with fever (>= {FEVER_THRESHOLD}°C): {len(stats.fever_records)}",
    ]
    lines += [f"  - {record.summary()}" for record in stats.fever_records]

    if skipped:
        lines += ["", f"Skipped records ({len(skipped)}):"]
        for item in skipped:
            lines.append(f"  - index {item.index} ({item.label}):")
            lines += [f"      * {reason}" for reason in item.reasons]

    return "\n".join(lines) + "\n"


def save_report(path: Path, report: str) -> None:
    """Write the report to disk (the only function here that touches files)."""
    path.write_text(report, encoding="utf-8")