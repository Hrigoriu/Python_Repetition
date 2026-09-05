"""medassistant_pipeline.py

Full patient data pipeline for MedAssistant:
    load JSON -> calculate statistics -> filter patients ->
    generate report -> save report

Architecture: each function has ONE responsibility (single
responsibility principle) — main() only orchestrates them.
"""

import json


# ═══════════════════════════════════════════
# LOAD
# ═══════════════════════════════════════════
def load_patients(path: str) -> list[dict] | None:
    """Load a list of patient records from a JSON file.

    Handles the two most common failure modes explicitly, so callers
    can rely on a clean None instead of an uncaught exception.

    Args:
        path: Path to the JSON file.

    Returns:
        list[dict] | None: The patient records, or None on failure.
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


# ═══════════════════════════════════════════
# CALCULATE
# ═══════════════════════════════════════════
def calculate_statistics(patients: list[dict]) -> dict:
    """Compute aggregate statistics over a list of patients.

    Args:
        patients: A list of patient dicts (must include "age" and
            "temperature").

    Returns:
        dict: total_patients, average_age, average_temperature.
    """
    total_patients = len(patients)
    average_age = sum(p["age"] for p in patients) / total_patients
    average_temperature = sum(p["temperature"] for p in patients) / total_patients

    return {
        "total_patients": total_patients,
        "average_age": average_age,
        "average_temperature": average_temperature,
    }


# ═══════════════════════════════════════════
# FILTER
# ═══════════════════════════════════════════
def filter_by_temperature(patients: list[dict], threshold: float) -> list[dict]:
    """Return patients whose temperature is at or above a threshold.

    Args:
        patients: A list of patient dicts (must include "temperature").
        threshold: Minimum temperature (inclusive) to be included.

    Returns:
        list[dict]: Matching patient records.
    """
    return [p for p in patients if p["temperature"] >= threshold]


def filter_by_diagnosis(patients: list[dict], diagnosis: str) -> list[dict]:
    """Return patients matching a given diagnosis (case-insensitive).

    Mirrors filter_by_temperature() for symmetry — same shape,
    different field.

    Args:
        patients: A list of patient dicts (must include "diagnosis").
        diagnosis: The diagnosis to match.

    Returns:
        list[dict]: Matching patient records.
    """
    return [p for p in patients if p["diagnosis"].lower() == diagnosis.lower()]


# ═══════════════════════════════════════════
# GENERATE REPORT — two formats, same source data
# ═══════════════════════════════════════════
def generate_text_report(
    stats: dict,
    high_temp_patients: list[dict],
    sinusitis_patients: list[dict],
) -> str:
    """Build a human-readable text report.

    Args:
        stats: Output of calculate_statistics().
        high_temp_patients: Output of filter_by_temperature().
        sinusitis_patients: Output of filter_by_diagnosis().

    Returns:
        str: The full report text.
    """
    title = "MEDASSISTANT PATIENT REPORT"

    high_temp_names = ", ".join(p["name"] for p in high_temp_patients) or "none"
    sinusitis_names = ", ".join(p["name"] for p in sinusitis_patients) or "none"

    return (
        f"{title}\n"
        f"{'=' * len(title)}\n\n"
        f"Total patients: {stats['total_patients']}\n"
        f"Average age: {stats['average_age']:.1f}\n"
        f"Average temperature: {stats['average_temperature']:.1f}\n\n"
        f"Patients with temperature >= 38.0: {high_temp_names}\n"
        f"Patients with sinusitis: {sinusitis_names}\n"
    )


def generate_json_report(
    stats: dict,
    high_temp_patients: list[dict],
    sinusitis_patients: list[dict],
) -> dict:
    """Build a machine-readable JSON-ready report.

    Args:
        stats: Output of calculate_statistics().
        high_temp_patients: Output of filter_by_temperature().
        sinusitis_patients: Output of filter_by_diagnosis().

    Returns:
        dict: The report data, ready for json.dump().
    """
    return {
        "total_patients": stats["total_patients"],
        "average_age": round(stats["average_age"], 1),
        "average_temperature": round(stats["average_temperature"], 1),
        "high_temperature_patients": [p["name"] for p in high_temp_patients],
        "sinusitis_patients": [p["name"] for p in sinusitis_patients],
    }


# ═══════════════════════════════════════════
# SAVE — one function, dispatches on report type
# ═══════════════════════════════════════════
def save_report(path: str, report: str | dict) -> None:
    """Save a report to disk, as plain text or JSON.

    A str report is written as-is; a dict report is serialized
    with json.dump(). This keeps ONE save function instead of two
    near-identical ones (DRY).

    Args:
        path: Destination file path.
        report: The report content — str for text, dict for JSON.
    """
    with open(path, "w", encoding="utf-8") as file:
        if isinstance(report, dict):
            json.dump(report, file, indent=2, ensure_ascii=False)
        else:
            file.write(report)


# ═══════════════════════════════════════════
# MAIN — orchestrates the pipeline, no logic of its own
# ═══════════════════════════════════════════
def main() -> None:
    patients = load_patients("data/medassistant_patients.json")
    if patients is None:
        return   # error already reported by load_patients()

    stats = calculate_statistics(patients)
    high_temp_patients = filter_by_temperature(patients, threshold=38.0)
    sinusitis_patients = filter_by_diagnosis(patients, diagnosis="sinusitis")

    text_report = generate_text_report(stats, high_temp_patients, sinusitis_patients)
    json_report = generate_json_report(stats, high_temp_patients, sinusitis_patients)

    save_report("data/medassistant_report.txt", text_report)
    save_report("data/medassistant_report.json", json_report)

    # --- Verify by reading both back and printing ---
    with open("data/medassistant_report.txt", "r", encoding="utf-8") as file:
        saved_text = file.read()

    lines = saved_text.rstrip("\n").split("\n")
    width = max(len(line) for line in lines) + 4

    print("\n┌" + "─" * width + "┐")
    print("│" + "  data/medassistant_report.txt".center(width) + "│")
    print("├" + "─" * width + "┤")
    for line in lines:
        print("│  " + line.ljust(width - 2) + "│")
    print("└" + "─" * width + "┘")

    print(f"\ndata/medassistant_report.json:\n{json.dumps(json_report, indent=2)}")


if __name__ == "__main__":
    main()

"""
┌────────────────────────────────────────────┐
│         data/medassistant_report.txt       │
├────────────────────────────────────────────┤
│  MEDASSISTANT PATIENT REPORT               │
│  ===========================               │
│                                            │
│  Total patients: 3                         │
│  Average age: 46.0                         │
│  Average temperature: 37.5                 │
│                                            │
│  Patients with temperature >= 38.0: Petro  │
│  Patients with sinusitis: Ivan, Petro      │
└────────────────────────────────────────────┘

data/medassistant_report.json:
{
  "total_patients": 3,
  "average_age": 46.0,
  "average_temperature": 37.5,
  "high_temperature_patients": [
    "Petro"
  ],
  "sinusitis_patients": [
    "Ivan",
    "Petro"
  ]
}
"""

"""
#*Чому процес побудовано саме так — пояснення кожного етапу:
load_patients()          → list[dict] | None    (зчитує файл, обробляє помилки вводу-виводу)
calculate_statistics()   → dict                 (чисті обчислення, без вводу-виводу, без виведення на екран)
filter_by_temperature()  → list[dict]           (чистий фільтр, шаблон, запозичений із Завдання 3)
filter_by_diagnosis()    → list[dict]           (така сама структура, як вище — симетрія, а не дублювання)
generate_text_report()   → str                  (чисте форматування, без доступу до файлів)
generate_json_report()   → dict                 (чисте форматування, без доступу до файлів)
save_report()            → None                 (ЄДИНА функція, яка записує на диск)
main()                   → лише координує, сама не містить бізнес-логіки

#*Чому функція filter_by_diagnosis() повторює структуру filter_by_temperature(), замість того щоб написати вбудований вираз:
# Both follow the exact same shape:
def filter_by_temperature(patients, threshold):
    return [p for p in patients if p["temperature"] >= threshold]

def filter_by_diagnosis(patients, diagnosis):
    return [p for p in patients if p["diagnosis"].lower() == diagnosis.lower()]

Це не просто стиль — це означає, що будь-який майбутній фільтр (за іменем, за віковим діапазоном, за відділом) може дотримуватися того самого, передбачуваного однорядкового шаблону. Читач, який розуміє одну функцію фільтрації, одразу розуміє їх усі. Вбудований вираз у функції calculate_statistics() також працював би, але це розмило б єдину відповідальність цієї функції (обчислення статистики) з не пов’язаною з нею (фільтрування) — змішуючи аспекти, які згодом доведеться змінювати незалежно один від одного.

#*Чому save_report() є ОДНІЄЮ функцією, а не save_text_report() + save_json_report():
def save_report(path, report):
    with open(path, "w", encoding="utf-8") as file:
        if isinstance(report, dict):
            json.dump(report, file, ...)
        else:
            file.write(report)

Каркас завдання називає саме одну функцію save_report(path, report) — і обидва типи звітів мають одну й ту саму базову дію («відкрити цей шлях, записати цей вміст»). Використання розгалуження на основі функції isinstance() всередині однієї функції дозволяє зберегти цю єдину дію в одному місці (DRY), замість того, щоб дублювати шаблонний код with open(...) у двох майже ідентичних функціях.

#*Чому функція main() не містить жодної логіки обчислення чи форматування:
def main():
    patients = load_patients(...)
    if patients is None:
        return
    stats = calculate_statistics(patients)
    ...

Функція main() виконує роль змісту для всього конвеєра — будь-хто, хто вперше знайомиться з кодом, може прочитати ці вісім рядків і зрозуміти весь хід роботи програми, не заглиблюючись у деталі реалізації. Кожен фактичний обчислювальний процес реалізовано у функції, назва якої вже вказує на її призначення.
"""
