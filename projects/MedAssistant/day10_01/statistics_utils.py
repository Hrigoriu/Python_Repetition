"""statistics_utils.py

Aggregate statistics over a list of patient records, for MedAssistant.
"""


def average_age(patients: list[dict]) -> float:
    """Compute the average age across all patients.

    Args:
        patients: A list of patient records (must include "age").

    Returns:
        float: The average age.
    """
    return sum(p["age"] for p in patients) / len(patients)


def average_temperature(patients: list[dict]) -> float:
    """Compute the average temperature across all patients.

    Args:
        patients: A list of patient records (must include "temperature").

    Returns:
        float: The average temperature.
    """
    return sum(p["temperature"] for p in patients) / len(patients)


def oldest_patient(patients: list[dict]) -> dict:
    """Find the oldest patient in the list.

    Args:
        patients: A list of patient records (must include "age").

    Returns:
        dict: The patient record with the highest age.
    """
    return max(patients, key=lambda p: p["age"])