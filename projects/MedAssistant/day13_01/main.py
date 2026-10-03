"""main.py

Лише послідовність кроків:
JSON -> PatientRecord.from_dict() -> валідація -> list[PatientRecord] -> статистика -> звіт
"""

import json
import sys

from patient_record import load_records
from report_utils import build_report, save_report
from statistics_utils import calculate_statistics


def main(data_path: str = "data/patients.json", report_path: str = "data/report.txt") -> int:
    """Повертає 0 при успіху і 1 при помилці. Програма не падає з traceback."""
    print("MEDASSISTANT")
    print("============\n")

    # --- Завантаження: кожен запис перевіряє сам PatientRecord ---
    print("Завантаження записів...")
    try:
        records, skipped = load_records(data_path)
    except FileNotFoundError:                       # має стояти ПЕРЕД OSError (його підклас)
        print(f"✗ Файл не знайдено:\n  {data_path}")
        return 1
    except OSError as e:
        print(f"✗ Не вдалося прочитати файл:\n  {e}")
        return 1
    except json.JSONDecodeError as e:               # має стояти ПЕРЕД ValueError (його підклас)
        print(f"✗ Некоректний JSON:\n  {e}")
        return 1
    except ValueError as e:
        print(f"✗ Некоректна структура файлу:\n  {e}")
        return 1

    print(f"✓ Валідних записів: {len(records)}, пропущено: {len(skipped)}")
    for item in skipped:
        print(f"  ⚠ запис №{item.number}: {item.reason}")
    if not records:
        print("✗ Немає жодного валідного запису, звіт не сформовано")
        return 1
    print()

    # --- Статистика ---
    print("Розрахунок статистики...")
    stats = calculate_statistics(records)
    print("✓ Статистика розрахована\n")

    # --- Звіт ---
    print("Формування звіту...")
    report = build_report(stats, skipped)
    try:
        save_report(report_path, report)
    except OSError as e:
        print(f"✗ Не вдалося зберегти звіт:\n  {e}")
        return 1
    print(f"✓ Звіт збережено: {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""
MEDASSISTANT
============

Завантаження записів...
✓ Валідних записів: 4, пропущено: 3
  ⚠ запис №5: відсутні поля: diagnosis
  ⚠ запис №6: id має бути додатним цілим числом, отримано -6; name не може бути порожнім, отримано ''; age має бути додатним цілим числом, отримано '61'; temperature має бути в діапазоні 25.0-45.0, отримано 99
  ⚠ запис №7: запис має бути словником (dict), отримано str

Розрахунок статистики...
✓ Статистика розрахована

Формування звіту...
✓ Звіт збережено: data/report.txt
"""
