"""statistics_utils.py

Aggregate statistics over a list of Patient objects, for MedAssistant.
"""

from patient import Patient


def average_age(patients: list[Patient]) -> float:
    """Compute the average age across all patients."""
    return sum(p.age for p in patients) / len(patients)


def average_temperature(patients: list[Patient]) -> float:
    """Compute the average temperature across all patients."""
    return sum(p.temperature for p in patients) / len(patients)


def oldest_patient(patients: list[Patient]) -> Patient:
    """Find the oldest patient in the list."""
    return max(patients, key=lambda p: p.age)


def fever_patients(patients: list[Patient]) -> list[Patient]:
    """Return patients whose is_fever() is True.

    Reads like natural language, as the challenge asked:
        [p for p in patients if p.is_fever()]
    """
    return [p for p in patients if p.is_fever()]