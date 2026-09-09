"""patient_utils.py

Loading, searching, and filtering patient records for MedAssistant.
"""

import json


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


def find_patient(patients: list[dict], name: str) -> dict | None:
    """Find a patient by name (case-insensitive).

    Args:
        patients: A list of patient records.
        name: The name to search for.

    Returns:
        dict | None: The matching record, or None if not found.
    """
    for patient in patients:
        if patient["name"].lower() == name.lower():
            return patient
    return None


def filter_by_temperature(patients: list[dict], threshold: float) -> list[dict]:
    """Return patients whose temperature is at or above a threshold.

    Args:
        patients: A list of patient records (must include "temperature").
        threshold: Minimum temperature (inclusive) to be included.

    Returns:
        list[dict]: Matching records.
    """
    return [p for p in patients if p["temperature"] >= threshold]


def filter_by_diagnosis(patients: list[dict], diagnosis: str) -> list[dict]:
    """Return patients matching a given diagnosis (case-insensitive).

    Mirrors filter_by_temperature() for symmetry.

    Args:
        patients: A list of patient records (must include "diagnosis").
        diagnosis: The diagnosis to match.

    Returns:
        list[dict]: Matching records.
    """
    return [p for p in patients if p["diagnosis"].lower() == diagnosis.lower()]