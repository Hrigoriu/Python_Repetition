"""patient_status_map.py

Combines list + dict + dict comprehension + function into a single
pipeline for MedAssistant: raw patient records → a name-to-status map.
"""


def classify_temperature(temp: float) -> str:
    """Classify a single body temperature reading.

    (Reused from earlier MedAssistant challenges — not duplicated.)
    """
    if temp < 37.5:
        return "normal"
    elif temp < 39.0:
        return "fever"
    else:
        return "high_fever"


patients = [
    {"name": "Ivan", "temperature": 36.6},
    {"name": "Olena", "temperature": 38.2},
    {"name": "Petro", "temperature": 39.1},
]

# --- Variant 1: one-line dict comprehension ---
status_map_v1 = {
    patient["name"]: classify_temperature(patient["temperature"])
    for patient in patients
}


# --- Variant 2: wrapped in a named function ---
def build_patient_status_map(patients: list[dict]) -> dict:
    """Build a {name: status} map from a list of patient records.

    Args:
        patients: A list of dicts, each with "name" and "temperature".

    Returns:
        dict: Patient name mapped to its temperature category.
    """
    return {
        patient["name"]: classify_temperature(patient["temperature"])
        for patient in patients
    }


status_map_v2 = build_patient_status_map(patients)

# --- Framed output ---
lines = [f"{name:<8} → {status}" for name, status in status_map_v1.items()]
width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  PATIENT STATUS MAP".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

print(f"\nstatus_map_v1 == status_map_v2: {status_map_v1 == status_map_v2}")

"""
┌─────────────────────────┐
│     PATIENT STATUS MAP  │
├─────────────────────────┤
│  Ivan     → normal      │
│  Olena    → fever       │
│  Petro    → high_fever  │
└─────────────────────────┘

status_map_v1 == status_map_v2: True
"""

"""
#*Розбір виразу dict comprehension — пояснення кожного елемента:
{
    patient["name"]: classify_temperature(patient["temperature"])
    for patient in patients
}
#  ↑                  ↑                                 ↑
# key                value                          iterate over
# (name field)   (call the function, using           the LIST of dicts
#                 the temperature field)

#*Усе, що тут поєднується, відповідає чотирьом елементам, зазначеним у назві завдання:
patients                                   # ← list of dicts (the LIST)
patients[0]                                # ← {"name": "Ivan", "temperature": 36.6}  (a DICT)
patient["temperature"]                     # ← reading a value OUT of that dict
classify_temperature(patient["temperature"])  # ← calling a FUNCTION with it
{k: v for ... in ...}                      # ← DICT COMPREHENSION building the final result

#*Покрокова інструкція для заданого вхідного значення:
patients = [
    {"name": "Ivan", "temperature": 36.6},
    {"name": "Olena", "temperature": 38.2},
    {"name": "Petro", "temperature": 39.1},
]

# Iteration 1: patient = {"name": "Ivan", "temperature": 36.6}
#   key   = patient["name"]                     → "Ivan"
#   value = classify_temperature(36.6)          → "normal"

# Iteration 2: patient = {"name": "Olena", "temperature": 38.2}
#   key   = "Olena"
#   value = classify_temperature(38.2)          → "fever"

# Iteration 3: patient = {"name": "Petro", "temperature": 39.1}
#   key   = "Petro"
#   value = classify_temperature(39.1)          → "high_fever"

# result:
{"Ivan": "normal", "Olena": "fever", "Petro": "high_fever"}

#*Чому функцію `classify_temperature()` використовують повторно, а не створюють її дублікат 
(за тим самим принципом DRY, що й у всіх попередніх завданнях):
{
    patient["name"]: classify_temperature(patient["temperature"])
    #                 ↑
    #     calls the SAME function that already knows the thresholds —
    #     this comprehension never rewrites "< 37.5 / < 39.0" itself
    for patient in patients
}

Якщо завтра поріг температури зміниться, редагувати потрібно лише у функції classify_temperature() — цей вираз (comprehension), функції analyze_patients(), classify_all() та всі інші функції, створені в рамках цих завдань, автоматично залишаться правильними.
"""
