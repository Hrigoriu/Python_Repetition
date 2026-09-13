"""main.py

MedAssistant Error Handling pipeline:
    load -> validate (skip invalid) -> process (statistics) -> report

Invalid patients no longer halt the whole pipeline: they are
reported as warnings, and the report is generated from the valid
patients only.
"""

import json

from patient_utils import load_patients, validate_patients
from report_utils import generate_report, save_report
from statistics_utils import average_age, average_temperature, oldest_patient


def run_pipeline(data_path: str, report_path: str) -> None:
    print("MEDASSISTANT")
    print("============\n")

    # ── STAGE 1: LOAD ──────────────────────────
    print("Loading patients...")
    try:
        patients = load_patients(data_path)
    except FileNotFoundError:
        print(f"✗ File not found:\n  {data_path}")
        return
    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON:\n  {e}")
        return
    print("✓ JSON loaded\n")

    # ── STAGE 2: VALIDATE (skip invalid, don't stop) ──
    print("Validating patients...")
    valid_patients, invalid_entries = validate_patients(patients)

    if invalid_entries:
        print(f"⚠ {len(invalid_entries)} invalid patient(s) skipped:")
        for entry in invalid_entries:
            print(f"  Patient #{entry['index']} ({entry['label']}): {entry['reason']}")

    if not valid_patients:
        print("✗ No valid patients remain — cannot continue.")
        return

    print(f"✓ Validation passed for {len(valid_patients)} patient(s)\n")

    # ── STAGE 3: PROCESS (statistics) — valid patients only ──
    print("Calculating statistics...")
    avg_age = average_age(valid_patients)
    avg_temp = average_temperature(valid_patients)
    oldest = oldest_patient(valid_patients)
    print("✓ Statistics calculated\n")

    # ── STAGE 4: REPORT ─────────────────────────
    print("Generating report...")
    report = generate_report(
        len(valid_patients), avg_age, avg_temp, oldest, invalid_entries
    )
    save_report(report_path, report)
    print("✓ Report generated")


if __name__ == "__main__":
    run_pipeline("data/patients.json", "data/report.txt")

"""
MEDASSISTANT
============

Loading patients...
✓ JSON loaded

Validating patients...
⚠ 3 invalid patient(s) skipped:
  Patient #0 (Ivan): 'temperature' must be in range 25.0-45.0, got 13.2
  Patient #3 (55): 'id' must be positive, got -4; 'name' must be a string, got 55; 'age' must be an integer, got '61'
  Patient #4 (Petro): 'temperature' must be in range 25.0-45.0, got 58.5
✓ Validation passed for 2 patient(s)

Calculating statistics...
✓ Statistics calculated

Generating report...
✓ Report generated
"""

"""
#report.txt
MEDASSISTANT PATIENT REPORT
===========================

Total valid patients: 2
Average age: 48.0
Average temperature: 37.6
Oldest patient: Petro (61)

Skipped invalid patients: 3
  - Ivan (index 0): 'temperature' must be in range 25.0-45.0, got 13.2
  - 55 (index 3): 'id' must be positive, got -4; 'name' must be a string, got 55; 'age' must be an integer, got '61'
  - Petro (index 4): 'temperature' must be in range 25.0-45.0, got 58.5

"""

