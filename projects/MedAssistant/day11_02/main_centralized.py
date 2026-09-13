"""main_centralized.py

Educational variant of MedAssistant's pipeline, demonstrating a
CENTRALIZED error-handling pattern:

    patient_utils.py
          |
      raise ValueError / FileNotFoundError / JSONDecodeError
          |
    main_centralized.py
          |
      ONE try/except block catches everything, at ONE place

Contrast this with the earlier main.py, where each stage had its
OWN try/except — here, ALL stages run inside a SINGLE try, and every
exception type is handled in ONE place, at the end.
"""

import json

from patient_utils import load_patients, validate_patients
from report_utils import generate_report, save_report
from statistics_utils import average_age, average_temperature, oldest_patient


def main() -> None:
    print("MEDASSISTANT (centralized error handling)")
    print("==========================================\n")

    try:
        # --- every stage lives here, with NO local try/except ---
        print("Loading patients...")
        patients = load_patients("data/patients.json")
        print("✓ JSON loaded\n")

        print("Validating patients...")
        valid_patients, invalid_entries = validate_patients(patients)
        if invalid_entries:
            print(f"⚠ {len(invalid_entries)} invalid patient(s) skipped:")
            for entry in invalid_entries:
                print(f"  Patient #{entry['index']} ({entry['label']}): {entry['reason']}")
        print(f"✓ Validation passed for {len(valid_patients)} patient(s)\n")

        print("Calculating statistics...")
        avg_age = average_age(valid_patients)
        avg_temp = average_temperature(valid_patients)
        oldest = oldest_patient(valid_patients)
        print("✓ Statistics calculated\n")

        print("Generating report...")
        report = generate_report(len(valid_patients), avg_age, avg_temp, oldest, invalid_entries)
        save_report("data/report.txt", report)
        print("✓ Report generated")

    # --- ONE place, at the end, handles EVERY exception type ---
    except FileNotFoundError as e:
        print(f"✗ File not found:\n  {e}")
    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON:\n  {e}")
    except ValueError as e:
        print(f"✗ Validation failed:\n  {e}")


if __name__ == "__main__":
    main()

"""
#*При відсутності файла про пацієнтів

MEDASSISTANT (centralized error handling)
==========================================

Loading patients...
✗ File not found:
  [Errno 2] No such file or directory: 'data/patients.json'
"""

"""
MEDASSISTANT (centralized error handling)
==========================================

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
