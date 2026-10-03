"""statistics_utils.py

Aggregate statistics over a list of PatientRecord objects.
Pure computation: no file access, no printing.
"""

from dataclasses import dataclass

from patient_record import PatientRecord


@dataclass(frozen=True)
class Statistics:
    """All aggregate results in one object, passed to the report builder."""

    total: int
    adults: int
    average_age: float
    average_temperature: float
    oldest: PatientRecord
    fever_records: tuple[PatientRecord, ...]


def _require_records(records: list[PatientRecord]) -> None:
    """Fail Fast with a clear message instead of ZeroDivisionError later."""
    if not records:
        raise ValueError("cannot calculate statistics: no valid records")


def average_age(records: list[PatientRecord]) -> float:
    """Average age of the given records."""
    _require_records(records)
    return sum(record.age for record in records) / len(records)


def average_temperature(records: list[PatientRecord]) -> float:
    """Average temperature of the given records."""
    _require_records(records)
    return sum(record.temperature for record in records) / len(records)


def oldest_record(records: list[PatientRecord]) -> PatientRecord:
    """The record with the highest age (the first one if there is a tie)."""
    _require_records(records)
    return max(records, key=lambda record: record.age)


def fever_records(records: list[PatientRecord]) -> list[PatientRecord]:
    """Records for which is_fever() is True."""
    return [record for record in records if record.is_fever()]


def count_adults(records: list[PatientRecord]) -> int:
    """How many records satisfy is_adult()."""
    return sum(1 for record in records if record.is_adult())


def calculate_statistics(records: list[PatientRecord]) -> Statistics:
    """Combine all statistics into one Statistics object.

    Raises:
        ValueError: If records is empty.
    """
    _require_records(records)
    return Statistics(
        total=len(records),
        adults=count_adults(records),
        average_age=average_age(records),
        average_temperature=average_temperature(records),
        oldest=oldest_record(records),
        fever_records=tuple(fever_records(records)),
    )