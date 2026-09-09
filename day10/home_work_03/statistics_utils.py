"""statistics_utils.py

Aggregate statistics over a list of patient records, for MedAssistant.
"""


def average_age(patients: list[dict]) -> float:
    """Compute the average age across all patients."""
    return sum(p["age"] for p in patients) / len(patients)


def average_temperature(patients: list[dict]) -> float:
    """Compute the average temperature across all patients."""
    return sum(p["temperature"] for p in patients) / len(patients)


def oldest_patient(patients: list[dict]) -> dict:
    """Find the oldest patient in the list."""
    return max(patients, key=lambda p: p["age"])