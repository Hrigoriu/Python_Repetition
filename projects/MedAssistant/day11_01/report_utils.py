"""report_utils.py

Report generation and saving for MedAssistant.
"""


def generate_report(
    total_valid: int,
    avg_age: float,
    avg_temp: float,
    oldest: dict,
    invalid_entries: list[dict],
) -> str:
    """Build a human-readable text report, including skipped patients.

    Args:
        total_valid: Number of patients that passed validation.
        avg_age: Average age among valid patients.
        avg_temp: Average temperature among valid patients.
        oldest: The oldest valid patient.
        invalid_entries: Output of validate_patients()'s second value —
            patients that were skipped, with reasons.

    Returns:
        str: The full report text.
    """
    title = "MEDASSISTANT PATIENT REPORT"

    report = (
        f"{title}\n"
        f"{'=' * len(title)}\n\n"
        f"Total valid patients: {total_valid}\n"
        f"Average age: {avg_age:.1f}\n"
        f"Average temperature: {avg_temp:.1f}\n"
        f"Oldest patient: {oldest['name']} ({oldest['age']})\n"
    )

    if invalid_entries:
        report += f"\nSkipped invalid patients: {len(invalid_entries)}\n"
        for entry in invalid_entries:
            report += f"  - {entry['label']} (index {entry['index']}): {entry['reason']}\n"

    return report


def save_report(path: str, report: str) -> None:
    """Save a text report to disk."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(report)