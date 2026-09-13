"""patient_utils.py

Loading and validating patient records for MedAssistant.

Deliberately does NOT swallow exceptions here — FileNotFoundError,
json.JSONDecodeError, and ValueError are all allowed to propagate to
the caller, so main() can catch each one at the right pipeline stage
and report a controlled, specific message instead of a crash.
"""

import json


def load_patients(path: str) -> list[dict]:
    """Load patient records from a JSON file.

    Deliberately does not catch anything — FileNotFoundError and
    json.JSONDecodeError propagate to the caller, which decides how
    to report each one.

    Args:
        path: Path to the JSON file.

    Returns:
        list[dict]: The patient records.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_patient(patient: dict) -> None:
    """Validate a single patient record, collecting ALL field errors.

    Checks every field regardless of earlier failures, then raises
    once with the full list of problems (not just the first one).

    Args:
        patient: A single patient record.

    Raises:
        ValueError: If any field is missing or invalid. The message
            lists every problem found for this patient.
    """
    errors = []

    if "id" not in patient:
        errors.append("missing 'id'")
    elif not isinstance(patient["id"], int) or isinstance(patient["id"], bool):
        errors.append(f"'id' must be an integer, got {patient['id']!r}")
    elif patient["id"] <= 0:
        errors.append(f"'id' must be positive, got {patient['id']}")

    if "name" not in patient:
        errors.append("missing 'name'")
    elif not isinstance(patient["name"], str):
        errors.append(f"'name' must be a string, got {patient['name']!r}")
    elif not patient["name"].strip():
        errors.append("'name' cannot be empty")

    if "age" not in patient:
        errors.append("missing 'age'")
    elif not isinstance(patient["age"], int) or isinstance(patient["age"], bool):
        errors.append(f"'age' must be an integer, got {patient['age']!r}")
    elif patient["age"] <= 0:
        errors.append(f"'age' must be greater than 0, got {patient['age']}")

    if "temperature" not in patient:
        errors.append("missing 'temperature'")
    elif not isinstance(patient["temperature"], (int, float)) or isinstance(patient["temperature"], bool):
        errors.append(f"'temperature' must be a number, got {patient['temperature']!r}")
    elif not (25.0 <= patient["temperature"] <= 45.0):
        errors.append(f"'temperature' must be in range 25.0-45.0, got {patient['temperature']}")

    if errors:
        raise ValueError("; ".join(errors))


def validate_patients(patients: list[dict]) -> tuple[list[dict], list[dict]]:
    """Split patients into valid and invalid, WITHOUT stopping the pipeline.

    Unlike a previous version that raised ValueError and halted
    everything, this now checks every patient and RETURNS both
    groups — the caller decides what to do (typically: proceed with
    the valid ones, report the invalid ones as skipped).

    Args:
        patients: A list of patient records.

    Returns:
        tuple[list[dict], list[dict]]: (valid_patients, invalid_entries).
            Each invalid_entries item is:
            {"index": int, "label": str, "reason": str}
    """
    valid_patients = []
    invalid_entries = []

    for index, patient in enumerate(patients):
        try:
            validate_patient(patient)
            valid_patients.append(patient)
        except ValueError as e:
            label = patient.get("name", f"unnamed (index {index})")
            invalid_entries.append({"index": index, "label": label, "reason": str(e)})

    return valid_patients, invalid_entries