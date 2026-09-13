"""patient_utils.py

Loading and validating patient records for MedAssistant.

IMPORTANT (centralized error handling pattern): every function here
ONLY raises exceptions when something goes wrong — none of them ever
call print(). Deciding HOW to report a problem to the user belongs
entirely to the caller (main), not to these helpers.
"""

import json


def load_patients(path: str) -> list[dict]:
    """Load patient records from a JSON file.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_patient(patient: dict) -> None:
    """Validate a single patient record, collecting ALL field errors.

    Raises:
        ValueError: If any field is missing or invalid.
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
    """Split patients into valid and invalid — does NOT stop on its own.

    Raises:
        ValueError: ONLY if every single patient is invalid (nobody
            left to process). If at least one patient is valid, this
            function returns normally — it does not raise for
            partial failures.

    Returns:
        tuple[list[dict], list[dict]]: (valid_patients, invalid_entries).
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

    if not valid_patients:
        raise ValueError(
            f"All {len(patients)} patient(s) are invalid — nothing to process. "
            f"Details: {invalid_entries}"
        )

    return valid_patients, invalid_entries