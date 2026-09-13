"""main.py

MedAssistant v2 — modular pipeline entry point.
"""

import json

from patient_utils import (
    filter_by_diagnosis,
    filter_by_temperature,
    load_patients,
)
from report_utils import (
    generate_json_report,
    generate_text_report,
    save_report,
)
from statistics_utils import (
    average_age,
    average_temperature,
    oldest_patient,
)


def main() -> None:
    # load patients
    patients = load_patients("data/medassistant_patients.json")
    if patients is None:
        return

    # calculate statistics
    total_patients = len(patients)
    avg_age = average_age(patients)
    avg_temp = average_temperature(patients)
    oldest = oldest_patient(patients)

    # filter patients
    high_temp_patients = filter_by_temperature(patients, threshold=38.0)
    sinusitis_patients = filter_by_diagnosis(patients, diagnosis="sinusitis")

    # generate report
    text_report = generate_text_report(
        total_patients,
        avg_age,
        avg_temp,
        oldest,
        high_temp_patients,
        sinusitis_patients,
    )
    json_report = generate_json_report(
        total_patients,
        avg_age,
        avg_temp,
        oldest,
        high_temp_patients,
        sinusitis_patients,
    )

    # save report
    save_report("data/report.txt", text_report)
    save_report("data/report.json", json_report)

    # --- verify by reading back and printing ---
    with open("data/report.txt", "r", encoding="utf-8") as file:
        saved_text = file.read()

    lines = saved_text.rstrip("\n").split("\n")
    width = max(len(line) for line in lines) + 4

    print("\n┌" + "─" * width + "┐")
    print("│" + "  data/report.txt".center(width) + "│")
    print("├" + "─" * width + "┤")
    for line in lines:
        print("│  " + line.ljust(width - 2) + "│")
    print("└" + "─" * width + "┘")

    print(f"\ndata/report.json:\n{json.dumps(json_report, indent=2)}")


if __name__ == "__main__":
    main()

"""
┌────────────────────────────────────────────┐
│               data/report.txt              │
├────────────────────────────────────────────┤
│  MEDASSISTANT PATIENT REPORT               │
│  ===========================               │
│                                            │
│  Total patients: 3                         │
│  Average age: 46.0                         │
│  Average temperature: 37.5                 │
│  Oldest patient: Petro (61)                │
│                                            │
│  Patients with temperature >= 38.0: Petro  │
│  Patients with sinusitis: Ivan, Petro      │
└────────────────────────────────────────────┘

data/report.json:
{
  "total_patients": 3,
  "average_age": 46.0,
  "average_temperature": 37.5,
  "oldest_patient": "Petro",
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
#*Чому функція main() майже нагадує саму схему конвеєра:
def main():
    patients = load_patients(...)         # load patients
    if patients is None:
        return

    avg_age = average_age(patients)         # calculate statistics
    avg_temp = average_temperature(patients)
    oldest = oldest_patient(patients)

    high_temp = filter_by_temperature(...)   # filter patients
    sinusitis = filter_by_diagnosis(...)

    text_report = generate_text_report(...)   # generate report
    json_report = generate_json_report(...)

    save_report(..., text_report)              # save report
    save_report(..., json_report)

Кожен рядок — це окремий виклик функції з описовою назвою: тут зовсім немає арифметичних операцій, форматування рядків, а також викликів open() чи json.load(). Той, хто вперше читає функцію main(), може зрозуміти поведінку всієї програми за п’ять рядків, не відкриваючи жодного з інших трьох файлів.

#*Чому призначення кожного файлу безпосередньо відповідає його назві:
Файл                    Відповідає за                           НЕ відповідає за
patient_utils.py        завантаження, пошук, фільтрування       статистика, текст/формат звіту
                        необроблених даних про пацієнтів

statistics_utils.py     чиста математика над списками           введення-виведення файлів, 
                        пацієнтів                               форматування

report_utils.py         перетворення чисел у текст              логіка обробки даних про пацієнтів, 
                        або JSON, збереження на диск            логіка статистики

main.py                 послідовне виконання вищезазначених     будь-які фактичні обчислення
                        операцій, нічого іншого

#*Чому функції filter_by_temperature() та filter_by_diagnosis() розміщені у файлі patient_utils.py, а не у report_utils.py:

Фільтрування — це питання про те, які пацієнти відповідають критеріям; 
це логіка домену пацієнтів, яка належить до тієї ж категорії, що й функція find_patient(). 
Це не має нічого спільного з тим, як виглядає звіт, а саме це є єдиною сферою відповідальності файлу report_utils.py. Збереження функцій фільтрування в цьому модулі означає, що якщо завтра вам знадобиться filter_by_temperature() десь, де це не має нічого спільного зі звітами (наприклад, у динамічній інформаційній панелі), ви зможете імпортувати її з patient_utils, не затягуючи при цьому жодного коду, пов’язаного зі звітами.
"""
