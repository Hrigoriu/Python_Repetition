"""report_utils.py

Формування й збереження звіту. Приймає готові дані, нічого не рахує сам.
"""

from patient_record import SkippedRecord
from statistics_utils import Statistics


def build_report(stats: Statistics, skipped: list[SkippedRecord]) -> str:
    """Повертає текст звіту (без файлів і print())."""
    title = "ЗВІТ MEDASSISTANT"

    lines = [
        title,
        "=" * len(title),
        "",
        f"Записів у файлі:  {stats.total + len(skipped)}",
        f"Валідних:         {stats.total}",
        f"Пропущено:        {len(skipped)}",
        "",
        "Статистика (лише валідні записи):",
        f"  Середній вік:         {stats.average_age:.1f}",
        f"  Середня температура:  {stats.average_temperature:.1f}",
        f"  Найстарший пацієнт:   {stats.oldest.name} ({stats.oldest.age})",
        f"  Дорослих:             {stats.adults} з {stats.total}",
        "",
        "Пацієнти з лихоманкою:",
    ]
    lines += [f"  - {r.summary()}" for r in stats.fever] or ["  (немає)"]

    lines += ["", "Пропущені записи:"]
    lines += [f"  - запис №{s.number}: {s.reason}" for s in skipped] or ["  (немає)"]

    return "\n".join(lines) + "\n"


def save_report(path: str, text: str) -> None:
    """Зберігає звіт. Помилки запису (OSError) обробляє main()."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)