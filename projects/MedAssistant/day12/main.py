"""main.py

MedAssistant pipeline, now built on Patient objects instead of
list[dict]:

    JSON -> load -> Patient objects -> validation -> methods ->
    statistics -> report
"""

import json

from patient import Patient
from report_utils import generate_report, save_report
from statistics_utils import (
    average_age,
    average_temperature,
    fever_patients,
    oldest_patient,
)



def load_patients(path: str) -> list[Patient]:
    """Load raw JSON and turn each record into a validated Patient.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
        ValueError: If any record fails Patient's own validation.
    """
    with open(path, "r", encoding="utf-8") as file:
        raw_records = json.load(file)

    return [Patient.from_dict(record) for record in raw_records]


def main() -> None:
    print("MEDASSISTANT")
    print("============\n")

    try:
        print("Loading patients...")
        patients = load_patients("data/patients.json")
        print(f"✓ {len(patients)} Patient object(s) loaded\n")

        # --- logic now reads like natural language ---
        print("Checking patients...")
        for patient in patients:
            if patient.is_fever():
                print(f"  ⚠ {patient.name} has a fever ({patient.temperature}°C)")
            if not patient.is_adult():
                print(f"  ℹ {patient.name} is a minor ({patient.age})")
        print()

        print("Calculating statistics...")
        avg_age = average_age(patients)
        avg_temp = average_temperature(patients)
        oldest = oldest_patient(patients)
        fevers = fever_patients(patients)
        print("✓ Statistics calculated\n")

        print("Generating report...")
        report = generate_report(patients, avg_age, avg_temp, oldest, fevers)
        save_report("data/report.txt", report)
        print("✓ Report generated")

    except FileNotFoundError as e:
        print(f"✗ File not found:\n  {e}")
    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON:\n  {e}")
    except ValueError as e:
        print(f"✗ Validation failed:\n  {e}")


if __name__ == "__main__":
    main()

"""
MEDASSISTANT
============

Loading patients...
✓ 3 Patient object(s) loaded

Checking patients...
  ⚠ Petro has a fever (38.5°C)

Calculating statistics...
✓ Statistics calculated

Generating report...
✓ Report generated
"""
