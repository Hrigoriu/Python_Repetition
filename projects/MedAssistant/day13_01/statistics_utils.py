"""statistics_utils.py

Чиста статистика над list[PatientRecord]: без файлів і без print().
"""

from dataclasses import dataclass

from patient_record import PatientRecord


@dataclass(frozen=True)
class Statistics:
    """Готовий набір результатів: його приймає report_utils."""
    total: int
    adults: int
    average_age: float
    average_temperature: float
    oldest: PatientRecord
    fever: tuple[PatientRecord, ...]


def _require_records(records: list[PatientRecord]) -> None:
    """Спільна перевірка (DRY): статистика порожнього списку не має сенсу."""
    if not records:
        raise ValueError("немає записів для статистики")


def average_age(records: list[PatientRecord]) -> float:
    _require_records(records)
    return sum(r.age for r in records) / len(records)


def average_temperature(records: list[PatientRecord]) -> float:
    _require_records(records)
    return sum(r.temperature for r in records) / len(records)


def oldest_patient(records: list[PatientRecord]) -> PatientRecord:
    _require_records(records)
    return max(records, key=lambda r: r.age)


def count_adults(records: list[PatientRecord]) -> int:
    return sum(1 for r in records if r.is_adult())


def fever_records(records: list[PatientRecord]) -> list[PatientRecord]:
    return [r for r in records if r.is_fever()]


def calculate_statistics(records: list[PatientRecord]) -> Statistics:
    """Складає окремі функції в один результат (Composition)."""
    return Statistics(
        total=len(records),
        adults=count_adults(records),
        average_age=average_age(records),
        average_temperature=average_temperature(records),
        oldest=oldest_patient(records),
        fever=tuple(fever_records(records)),
    )