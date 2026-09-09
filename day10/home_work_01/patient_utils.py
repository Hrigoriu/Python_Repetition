"""patient_utils.py

Patient lookup utilities for MedAssistant.
"""


def find_patient(patients: list[dict], name: str) -> dict | None:
    """Find a patient by name (case-insensitive).

    Args:
        patients: A list of patient records.
        name: The name to search for.

    Returns:
        dict | None: The matching patient record, or None if not found.
    """
    for patient in patients:
        if patient["name"].lower() == name.lower():
            return patient
    return None