"""patient_record.py

Модель PatientRecord (dataclass) та побудова списку записів із сирих даних JSON.
"""

import json
from dataclasses import dataclass, fields

# Пороги в одному місці (DRY): змінюємо тут, і всі методи отримують нове значення
ADULT_AGE = 18
FEVER_THRESHOLD = 37.5
MIN_TEMPERATURE = 25.0
MAX_TEMPERATURE = 45.0


def _is_positive_int(value: object) -> bool:
    """int > 0. bool виключаємо: у Python True == 1."""
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _is_non_empty_str(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _is_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


@dataclass
class PatientRecord:
    id: int
    name: str
    age: int
    diagnosis: str
    temperature: float

    def __post_init__(self) -> None:
        """Перевіряє ВСІ поля й піднімає ОДНЕ ValueError з усіма проблемами.

        @dataclass не перевіряє типи з анотацій, тому перевірки пишемо самі.
        Невалідний запис створити неможливо: Fail Fast.
        """
        errors = []

        if not _is_positive_int(self.id):
            errors.append(f"id має бути додатним цілим числом, отримано {self.id!r}")
        if not _is_non_empty_str(self.name):
            errors.append(f"name не може бути порожнім, отримано {self.name!r}")
        if not _is_positive_int(self.age):
            errors.append(f"age має бути додатним цілим числом, отримано {self.age!r}")
        if not _is_non_empty_str(self.diagnosis):
            errors.append(f"diagnosis не може бути порожнім, отримано {self.diagnosis!r}")

        if not _is_number(self.temperature):
            errors.append(f"temperature має бути числом, отримано {self.temperature!r}")
        elif not (MIN_TEMPERATURE <= self.temperature <= MAX_TEMPERATURE):
            errors.append(
                f"temperature має бути в діапазоні {MIN_TEMPERATURE}-{MAX_TEMPERATURE}, "
                f"отримано {self.temperature}"
            )

        if errors:
            raise ValueError("; ".join(errors))

    def is_adult(self) -> bool:
        return self.age >= ADULT_AGE

    def is_fever(self) -> bool:
        return self.temperature >= FEVER_THRESHOLD

    def summary(self) -> str:
        """Короткий опис запису. Повертає рядок, друкує той, хто викликає."""
        age_status = "дорослий" if self.is_adult() else "неповнолітній"
        fever_status = "лихоманка" if self.is_fever() else "без лихоманки"
        return (
            f"#{self.id} {self.name} ({self.age}, {age_status}) — "
            f"{self.diagnosis}, {self.temperature}°C ({fever_status})"
        )

    @classmethod
    def from_dict(cls, data: dict) -> "PatientRecord":
        """dict -> PatientRecord. На будь-які погані дані піднімає ЛИШЕ ValueError.

        Імена полів беремо з самого dataclass (fields), а не пишемо вдруге:
        додали поле в клас, і воно автоматично стало обов'язковим тут (DRY).
        """
        if not isinstance(data, dict):
            raise ValueError(f"запис має бути словником (dict), отримано {type(data).__name__}")

        names = [f.name for f in fields(cls)]
        missing = [name for name in names if name not in data]
        if missing:
            raise ValueError("відсутні поля: " + ", ".join(missing))

        return cls(**{name: data[name] for name in names})   # значення перевірить __post_init__


@dataclass(frozen=True)
class SkippedRecord:
    """Запис, який не вдалося перетворити на PatientRecord, і причина."""
    number: int     # позиція в JSON-списку, рахуючи з 1
    reason: str


def build_records(raw_records: list) -> tuple[list[PatientRecord], list[SkippedRecord]]:
    """Сирі записи -> (валідні PatientRecord, пропущені з причинами).

    Один поганий запис не зупиняє решту.
    """
    records = []
    skipped = []

    for number, raw in enumerate(raw_records, start=1):
        try:
            records.append(PatientRecord.from_dict(raw))
        except ValueError as e:
            skipped.append(SkippedRecord(number, str(e)))

    return records, skipped


def read_json(path: str) -> object:
    """Лише читає JSON-файл. Помилки файлу не ловимо, їх обробляє main()."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_records(path: str) -> tuple[list[PatientRecord], list[SkippedRecord]]:
    """JSON-файл -> (валідні записи, пропущені записи)."""
    raw = read_json(path)
    if not isinstance(raw, list):
        raise ValueError(f"очікувався JSON-список записів, отримано {type(raw).__name__}")
    return build_records(raw)