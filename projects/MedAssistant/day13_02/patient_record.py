"""patient_record.py

The PatientRecord data model for MedAssistant: state, validation, and
the behavior that belongs to a single patient record.
"""

from dataclasses import dataclass, fields

ADULT_AGE = 18
FEVER_THRESHOLD = 37.5
MIN_TEMPERATURE = 25.0
MAX_TEMPERATURE = 45.0


class RecordValidationError(ValueError):
    """Raised when a record is invalid.

    Carries EVERY problem found (not just the first), as a list, so callers
    never have to split a message string to get the individual problems.
    It subclasses ValueError, so `except ValueError` still catches it.
    """

    def __init__(self, errors: list[str]) -> None:
        self.errors = list(errors)
        super().__init__("; ".join(self.errors))


def _is_int(value: object) -> bool:
    """True for real integers. bool is excluded: True would pass as 1."""
    return isinstance(value, int) and not isinstance(value, bool)


def _is_number(value: object) -> bool:
    """True for int/float. bool is excluded for the same reason."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


@dataclass
class PatientRecord:
    id: int
    name: str
    age: int
    diagnosis: str
    temperature: float

    def __post_init__(self) -> None:
        """Validate every field right after the generated __init__ ran.

        Collect-all: all fields are checked and all problems are reported
        together, so one run shows everything that is wrong.

        Raises:
            RecordValidationError: If at least one field is invalid.
        """
        errors = []

        if not _is_int(self.id) or self.id <= 0:
            errors.append(f"id must be a positive integer, got {self.id!r}")

        if not isinstance(self.name, str) or not self.name.strip():
            errors.append(f"name must be a non-empty string, got {self.name!r}")

        if not _is_int(self.age) or self.age <= 0:
            errors.append(f"age must be a positive integer, got {self.age!r}")

        if not isinstance(self.diagnosis, str) or not self.diagnosis.strip():
            errors.append(f"diagnosis must be a non-empty string, got {self.diagnosis!r}")

        if not _is_number(self.temperature):
            errors.append(f"temperature must be a number, got {self.temperature!r}")
        elif not MIN_TEMPERATURE <= self.temperature <= MAX_TEMPERATURE:
            errors.append(
                f"temperature must be between {MIN_TEMPERATURE} and "
                f"{MAX_TEMPERATURE}, got {self.temperature}"
            )

        if errors:
            raise RecordValidationError(errors)

    @classmethod
    def from_dict(cls, data: dict) -> "PatientRecord":
        """Build a PatientRecord from a plain dict (e.g. one JSON object).

        Expected keys are taken from the dataclass fields themselves, so
        adding a field later needs no change here. Unknown extra keys are
        ignored. Value checks are NOT repeated here: the constructor runs
        __post_init__, which is the single place that knows the rules.

        Args:
            data: The raw record.

        Returns:
            PatientRecord: A valid record.

        Raises:
            RecordValidationError: If data is not a dict, keys are missing,
                or any value is invalid.
        """
        if not isinstance(data, dict):
            raise RecordValidationError(
                [f"record must be a JSON object, got {type(data).__name__}"]
            )

        names = [field.name for field in fields(cls)]
        missing = [name for name in names if name not in data]
        if missing:
            raise RecordValidationError([f"missing key {name!r}" for name in missing])

        return cls(**{name: data[name] for name in names})

    def is_adult(self) -> bool:
        """Check whether the patient is an adult (18 or older)."""
        return self.age >= ADULT_AGE

    def is_fever(self) -> bool:
        """Check whether the temperature indicates a fever (>= 37.5 C)."""
        return self.temperature >= FEVER_THRESHOLD

    def summary(self) -> str:
        """Return a one-line, human-readable description of the record."""
        age_group = "adult" if self.is_adult() else "minor"
        fever_status = "fever" if self.is_fever() else "no fever"
        return (
            f"#{self.id} {self.name} ({self.age}, {age_group}) — "
            f"{self.diagnosis}, {self.temperature}°C ({fever_status})"
        )


@dataclass(frozen=True)
class SkippedRecord:
    """A raw record that could not become a PatientRecord, and why."""

    index: int
    label: str
    reasons: tuple[str, ...]


def _label(data: object) -> str:
    """Best-effort human label for a raw record (its name, if it has one)."""
    name = data.get("name") if isinstance(data, dict) else None
    return name if isinstance(name, str) and name.strip() else "unnamed"


def build_records(
    raw_records: list,
) -> tuple[list[PatientRecord], list[SkippedRecord]]:
    """Turn raw JSON records into valid PatientRecords; skip the bad ones.

    One bad record never stops the rest. Only RecordValidationError is
    caught: any other exception is a real bug and must not be hidden.

    Args:
        raw_records: The decoded JSON (expected to be a list).

    Returns:
        tuple: (valid records, skipped records with reasons).

    Raises:
        ValueError: If raw_records is not a list at all.
    """
    if not isinstance(raw_records, list):
        raise ValueError(f"expected a JSON array of records, got {type(raw_records).__name__}")

    records = []
    skipped = []

    for index, data in enumerate(raw_records):
        try:
            records.append(PatientRecord.from_dict(data))
        except RecordValidationError as error:
            skipped.append(SkippedRecord(index, _label(data), tuple(error.errors)))

    return records, skipped