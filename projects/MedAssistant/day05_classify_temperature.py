
# 🚀 Challenge №4 — `MedAssistant`

"""
Створи:
temperatures = [
    36.6,
    37.2,
    38.1,
    39.0,
    37.8,
    36.4,
]

Програма повинна пройти по всіх температурах і визначити:
< 37.5      → Normal
37.5–38.9   → Fever
39+         → High fever

Приклад:
36.6 → Normal
37.2 → Normal
38.1 → Fever
39.0 → High fever
37.8 → Fever
36.4 → Normal
"""

"""
Classifies a list of patient temperature readings into risk categories
for the MedAssistant project.
"""

from collections import Counter


def classify_temperature(temp: float) -> str:
    """Classify a single body temperature reading.

    Args:
        temp: Body temperature in degrees Celsius.

    Returns:
        str: One of "Normal", "Fever", or "High fever".
    """
    if temp < 37.5:
        return "Normal"
    elif temp < 39.0:      # Python already knows temp >= 37.5 here
        return "Fever"
    else:                  # temp >= 39.0
        return "High fever"


MARKER = {
    "Normal":      "🟢",
    "Fever":       "🟡",
    "High fever":  "🔴",
}


temperatures = [
    36.6,
    37.2,
    38.1,
    39.0,
    37.8,
    36.4,
]

# --- Classify each reading and build display rows ---
categories = [classify_temperature(t) for t in temperatures]

rows = [
    f"{temp:.1f} °C  →  {MARKER[cat]} {cat}"
    for temp, cat in zip(temperatures, categories)
]

# --- Summary count ---
counts = Counter(categories)
summary_line = (
    f"Normal: {counts['Normal']}  |  "
    f"Fever: {counts['Fever']}  |  "
    f"High fever: {counts['High fever']}"
)

# --- Framed output ---
lines = rows + ["─" * max(len(r) for r in rows), summary_line]
width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  TEMPERATURE CLASSIFICATION".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────────────────────────────┐
│          TEMPERATURE CLASSIFICATION        │
├────────────────────────────────────────────┤
│  36.6 °C  →  🟢 Normal                      │
│  37.2 °C  →  🟢 Normal                      │
│  38.1 °C  →  🟡 Fever                       │
│  39.0 °C  →  🔴 High fever                  │
│  37.8 °C  →  🟡 Fever                       │
│  36.4 °C  →  🟢 Normal                      │
│  ────────────────────────                  │
│  Normal: 3  |  Fever: 2  |  High fever: 1  │
└────────────────────────────────────────────┘
"""

"""
Ключові проектні рішення:

classify_temperature() як самостійна функція — суто логічна, без побічних ефектів (всередині немає print()). Це дозволяє тестувати її незалежно та повторно використовувати в інших частинах MedAssistant (наприклад, у класі MedicalMeasurement або майбутньому класі PatientReport), дотримуючись того самого шаблону «розмежування інтересів», що й у попередніх модулях.

Логіка меж без перекриття — той самий принцип, що й у попередніх вправах щодо ІМТ/температури: elif temp < 39.0 неявним чином означає 37.5 <= temp < 39.0, оскільки попередній if вже виключив значення < 37.5.

Counter from collections — підклас dict, створений саме для цього: підрахунку входжень. Counter(categories) автоматично підраховує, скільки разів з’являється кожен рядок категорії, що є більш чітким підходом, ніж ручне інкрементування трьох окремих змінних.

zip(temperatures, categories) — об’єднує кожне необроблене значення з його обчисленою категорією для відображення, повторно використовуючи шаблон zip() із попереднього практичного завдання.
"""
