"""temperature_batch_classifier.py

Batch temperature classification for MedAssistant, reusing the
single-reading classifier rather than duplicating its logic.
"""


def classify_temperature(temp: float) -> str:
    """Classify a single body temperature reading.

    Args:
        temp: Body temperature in degrees Celsius.

    Returns:
        str: "normal", "fever", or "high_fever".
    """
    if temp < 37.5:
        return "normal"
    elif temp < 39.0:      # already known: temp >= 37.5 here
        return "fever"
    else:                  # temp >= 39.0
        return "high_fever"


def classify_all(temperatures: list[float]) -> list[str]:
    """Classify a whole list of temperature readings.

    Reuses classify_temperature() for each reading — this function's
    only job is mapping over the list, not re-deciding the thresholds.

    Args:
        temperatures: A list of body temperature readings in Celsius.

    Returns:
        list[str]: One category per input reading, same order.
    """
    return [classify_temperature(temp) for temp in temperatures]


# --- Demo ---
temperatures = [
    36.6,
    38.1,
    39.2,
    37.0,
]

categories = classify_all(temperatures)

# --- Framed table output ---
MARKER = {"normal": "🟢", "fever": "🟡", "high_fever": "🔴"}

rows = [
    f"{temp:<6.1f} →  {MARKER[cat]} {cat}"
    for temp, cat in zip(temperatures, categories)
]

width = max(len(row) for row in rows) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  BATCH TEMPERATURE CLASSIFICATION".center(width) + "│")
print("├" + "─" * width + "┤")
for row in rows:
    print("│  " + row.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

print(f"\nclassify_all({temperatures}) → {categories}")

"""
┌──────────────────────────┐
│  BATCH TEMPERATURE CLASSIFICATION│
├──────────────────────────┤
│  36.6   →  🟢 normal      │
│  38.1   →  🟡 fever       │
│  39.2   →  🔴 high_fever  │
│  37.0   →  🟢 normal      │
└──────────────────────────┘

classify_all([36.6, 38.1, 39.2, 37.0]) → ['normal', 'fever', 'high_fever', 'normal']
"""

"""
Це той самий принцип DRY, що й у попередньому завданні analyze_temperatures(): функція classify_temperature() є єдиним авторитетним джерелом інформації щодо того, що вважається  "normal", "fever", або "high_fever". Якщо клініка коли-небудь змінить поріг лихоманки з 37,5 на 37,8, у всьому коді потрібно буде редагувати лише одне місце — функція classify_all() (та всі інші, що її використовують) автоматично врахує цю зміну, і ризик того, що одна копія буде оновлена, а інша — пропущена, дорівнює нулю.

#*Розбір виразу:
[classify_temperature(temp) for temp in temperatures]
#  ↑                          ↑
#  що додати до              цикл по кожному
#  нового списку (виклик функції)   елементу вхідного списку

Для [36.6, 38.1, 39.2, 37.0]:

classify_temperature(36.6) → "normal"
classify_temperature(38.1) → "fever"
classify_temperature(39.2) → "high_fever"
classify_temperature(37.0) → "normal"

→ ["normal", "fever", "high_fever", "normal"] — точно відповідає очікуваному результату.
"""