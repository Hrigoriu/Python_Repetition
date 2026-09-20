"""report_utils.py

Report generation and saving for MedAssistant.
"""

from patient import Patient


def generate_report(
    patients: list[Patient],
    avg_age: float,
    avg_temp: float,
    oldest: Patient,
    fevers: list[Patient],
) -> str:
    """Build a human-readable text report from Patient objects."""
    title = "MEDASSISTANT PATIENT REPORT"

    lines = [
        f"{title}",
        "=" * len(title),
        "",
        f"Total patients: {len(patients)}",
        f"Average age: {avg_age:.1f}",
        f"Average temperature: {avg_temp:.1f}",
        f"Oldest patient: {oldest.name} ({oldest.age})",
        "",
        "Patients with fever:",
    ]
    lines += [f"  - {p.summary()}" for p in fevers] if fevers else ["  (none)"]

    return "\n".join(lines) + "\n"


def save_report(path: str, report: str) -> None:
    """Save a text report to disk."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(report)