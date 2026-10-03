# class_work_10.py

# ═══════════════════════════════════════════
# IMPORTS
# ═══════════════════════════════════════════
from patient_utils import calculate_bmi, is_adult, normalize_name
from statistics_utils import average, maximum, minimum

# ═══════════════════════════════════════════
# DATA
# ═══════════════════════════════════════════
raw_names = ["  ivan  ", "OLENA", " petro", "HANNA "]

patients_ages = [
    ("Ivan", 42),
    ("Sofia", 15),
    ("Petro", 18),
    ("Mykola", 7),
]

patients_measurements = [
    ("Ivan", 82, 1.80),
    ("Olena", 55, 1.65),
    ("Petro", 95, 1.75),
]

patient_temperatures = [36.6, 38.2, 37.4, 39.1, 36.9]


# ═══════════════════════════════════════════
# CALLS
# ═══════════════════════════════════════════
normalized_names = [normalize_name(name) for name in raw_names]
adult_checks = [(name, age, is_adult(age)) for name, age in patients_ages]
bmi_results = [
    (name, calculate_bmi(weight, height))
    for name, weight, height in patients_measurements
]

avg_temp = average(patient_temperatures)
max_temp = maximum(patient_temperatures)
min_temp = minimum(patient_temperatures)

try:
    average([])
    empty_check = "не впало (несподівано)"
except ValueError as e:
    empty_check = f"❌ ValueError: {e}"


# ═══════════════════════════════════════════
# OUTPUT
# ═══════════════════════════════════════════
def print_framed(title: str, lines: list[str]) -> None:
    """Допоміжна функція ВИВОДУ — не бізнес-логіка, лише форматування."""
    width = max(len(title), max(len(line) for line in lines)) + 4
    print("\n┌" + "─" * width + "┐")
    print("│" + f"  {title}".center(width) + "│")
    print("├" + "─" * width + "┤")
    for line in lines:
        print("│  " + line.ljust(width - 2) + "│")
    print("└" + "─" * width + "┘")


print_framed(
    "NORMALIZE_NAME()",
    [f"{raw!r} → {norm!r}" for raw, norm in zip(raw_names, normalized_names)],
)

print_framed(
    "IS_ADULT()",
    [f"{name} ({age} р.) → {result}" for name, age, result in adult_checks],
)

print_framed(
    "CALCULATE_BMI()",
    [
        f"{name} ({weight} кг, {height} м) → BMI {bmi:.1f}"
        for (name, weight, height), (_, bmi) in zip(patients_measurements, bmi_results)
    ],
)

print_framed(
    "STATISTICS_UTILS",
    [
        f"Температури: {patient_temperatures}",
        f"average(): {avg_temp:.2f}",
        f"maximum(): {max_temp}",
        f"minimum(): {min_temp}",
        f"average([]) → {empty_check}",
    ],
)

"""
┌───────────────────────┐
│     NORMALIZE_NAME()  │
├───────────────────────┤
│  '  ivan  ' → 'Ivan'  │
│  'OLENA' → 'Olena'    │
│  ' petro' → 'Petro'   │
│  'HANNA ' → 'Hanna'   │
└───────────────────────┘

┌─────────────────────────┐
│         IS_ADULT()      │
├─────────────────────────┤
│  Ivan (42 р.) → True    │
│  Sofia (15 р.) → False  │
│  Petro (18 р.) → True   │
│  Mykola (7 р.) → False  │
└─────────────────────────┘

┌────────────────────────────────────┐
│           CALCULATE_BMI()          │
├────────────────────────────────────┤
│  Ivan (82 кг, 1.8 м) → BMI 25.3    │
│  Olena (55 кг, 1.65 м) → BMI 20.2  │
│  Petro (95 кг, 1.75 м) → BMI 31.0  │
└────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────┐
│                           STATISTICS_UTILS                        │
├───────────────────────────────────────────────────────────────────┤
│  Температури: [36.6, 38.2, 37.4, 39.1, 36.9]                      │
│  average(): 37.64                                                 │
│  maximum(): 39.1                                                  │
│  minimum(): 36.6                                                  │
│  average([]) → ❌ ValueError: Список чисел не може бути порожнім. │
└───────────────────────────────────────────────────────────────────┘
"""
