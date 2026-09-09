"""medassistant.py

MedAssistant application entry point:
    imports -> data (load) -> calls (statistics + lookup) -> output (print + save report)
"""

import json

from patient_utils import find_patient
from statistics_utils import (
    average_age,
    average_temperature,
    oldest_patient,
)


# ═══════════════════════════════════════════
# LOAD
# ═══════════════════════════════════════════
def load_patients(path: str) -> list[dict] | None:
    """Load patient records from a JSON file, handling common errors.

    Args:
        path: Path to the JSON file.

    Returns:
        list[dict] | None: The records, or None on failure.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"⚠ Error: file '{path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"⚠ Error: file '{path}' contains invalid JSON ({e}).")
        return None


# ═══════════════════════════════════════════
# GENERATE REPORT
# ═══════════════════════════════════════════
def generate_report(patients: list[dict], searched_patient: dict | None, search_name: str) -> str:
    """Build a human-readable text report.

    Args:
        patients: All loaded patient records.
        searched_patient: Result of find_patient(), or None.
        search_name: The name that was searched for.

    Returns:
        str: The full report text.
    """
    title = "MEDASSISTANT REPORT"
    oldest = oldest_patient(patients)

    search_line = (
        f"{searched_patient['name']}, age {searched_patient['age']}, "
        f"diagnosis: {searched_patient['diagnosis']}"
        if searched_patient is not None
        else f"'{search_name}' not found"
    )

    return (
        f"{title}\n"
        f"{'=' * len(title)}\n\n"
        f"Total patients: {len(patients)}\n"
        f"Average age: {average_age(patients):.1f}\n"
        f"Average temperature: {average_temperature(patients):.1f}\n"
        f"Oldest patient: {oldest['name']} ({oldest['age']})\n\n"
        f"Search result for '{search_name}': {search_line}\n"
    )


# ═══════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════
def save_report(path: str, report: str) -> None:
    """Save a text report to disk.

    Args:
        path: Destination file path.
        report: The report content.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(report)


# ═══════════════════════════════════════════
# MAIN — orchestrates the pipeline only
# ═══════════════════════════════════════════
def main() -> None:
    patients = load_patients("data/patients.json")
    if patients is None:
        return

    search_name = "Petro"
    searched_patient = find_patient(patients, search_name)

    report = generate_report(patients, searched_patient, search_name)
    save_report("data/report.txt", report)

    # --- Verify by reading the saved report back and printing it framed ---
    with open("data/report.txt", "r", encoding="utf-8") as file:
        saved_report = file.read()

    lines = saved_report.rstrip("\n").split("\n")
    width = max(len(line) for line in lines) + 4

    print("\n┌" + "─" * width + "┐")
    print("│" + "  data/report.txt".center(width) + "│")
    print("├" + "─" * width + "┤")
    for line in lines:
        print("│  " + line.ljust(width - 2) + "│")
    print("└" + "─" * width + "┘")


if __name__ == "__main__":
    main()

"""
┌──────────────────────────────────────────────────────────────────┐
│                          data/report.txt                         │
├──────────────────────────────────────────────────────────────────┤
│  MEDASSISTANT REPORT                                             │
│  ===================                                             │
│                                                                  │
│  Total patients: 4                                               │
│  Average age: 41.8                                               │
│  Average temperature: 37.6                                       │
│  Oldest patient: Petro (61)                                      │
│                                                                  │
│  Search result for 'Petro': Petro, age 61, diagnosis: sinusitis  │
└──────────────────────────────────────────────────────────────────┘
"""
