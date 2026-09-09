"""report_utils.py

Report generation and saving for MedAssistant.
"""

import json


def generate_text_report(
    total_patients: int,
    avg_age: float,
    avg_temp: float,
    oldest: dict,
    high_temp_patients: list[dict],
    sinusitis_patients: list[dict],
) -> str:
    """Build a human-readable text report."""
    title = "MEDASSISTANT PATIENT REPORT"

    high_temp_names = ", ".join(p["name"] for p in high_temp_patients) or "none"
    sinusitis_names = ", ".join(p["name"] for p in sinusitis_patients) or "none"

    return (
        f"{title}\n"
        f"{'=' * len(title)}\n\n"
        f"Total patients: {total_patients}\n"
        f"Average age: {avg_age:.1f}\n"
        f"Average temperature: {avg_temp:.1f}\n"
        f"Oldest patient: {oldest['name']} ({oldest['age']})\n\n"
        f"Patients with temperature >= 38.0: {high_temp_names}\n"
        f"Patients with sinusitis: {sinusitis_names}\n"
    )


def generate_json_report(
    total_patients: int,
    avg_age: float,
    avg_temp: float,
    oldest: dict,
    high_temp_patients: list[dict],
    sinusitis_patients: list[dict],
) -> dict:
    """Build a machine-readable JSON-ready report."""
    return {
        "total_patients": total_patients,
        "average_age": round(avg_age, 1),
        "average_temperature": round(avg_temp, 1),
        "oldest_patient": oldest["name"],
        "high_temperature_patients": [p["name"] for p in high_temp_patients],
        "sinusitis_patients": [p["name"] for p in sinusitis_patients],
    }


def save_report(path: str, report: str | dict) -> None:
    """Save a report to disk, as plain text or JSON.

    A str report is written as-is; a dict report is serialized
    with json.dump() — one function instead of two near-duplicates.
    """
    with open(path, "w", encoding="utf-8") as file:
        if isinstance(report, dict):
            json.dump(report, file, indent=2, ensure_ascii=False)
        else:
            file.write(report)