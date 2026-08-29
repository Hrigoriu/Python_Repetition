## 🧠 Challenge №5 — рівень Junior+

"""
Створи функцію:
def analyze_temperatures(
    temperatures: list[float],
) -> dict:
    ...

Вона повинна повернути:
{
    "normal": 3,
    "fever": 2,
    "high_fever": 1,
}

Використовуй окрему функцію:
classify_temperature()

яку ти вже створив у День 5.
Тобто цього разу ми починаємо перевикористовувати код із попередніх днів.
Це дуже важливий момент.
"""

def classify_temperature(temp: float) -> str:
    """Classify a single body temperature reading.

    (Same function as in the earlier MedAssistant temperature challenge —
    reused here, not duplicated.)
    """
    if temp < 37.5:
        return "Normal"
    elif temp < 39.0:
        return "Fever"
    else:
        return "High fever"


def analyze_temperatures(temperatures: list[float]) -> dict[str, int]:
    """Count how many readings fall into each temperature category.

    Reuses classify_temperature() for the actual classification logic —
    this function's only job is counting, not re-deciding the thresholds.

    Args:
        temperatures: A list of body temperature readings in Celsius.

    Returns:
        dict: All three category keys always present (0 if unused):
            {"normal": int, "fever": int, "high_fever": int}
    """
    counts = {"normal": 0, "fever": 0, "high_fever": 0}

    for temp in temperatures:
        category = classify_temperature(temp)          # e.g. "High fever"
        key = category.lower().replace(" ", "_")        # → "high_fever"
        counts[key] += 1

    return counts


# --- Demo with a few test sets ---
test_sets = [
    ("Ward A", [36.6, 37.2, 38.1, 39.0, 37.8, 36.4]),
    ("Ward B", [36.1, 36.5, 36.9]),
    ("ICU",    [39.5, 40.1, 38.7, 39.2]),
]

results = [(label, analyze_temperatures(temps)) for label, temps in test_sets]

# --- Framed table output ---
header = f"{'Ward':<10} │ {'normal':>7} │ {'fever':>7} │ {'high_fever':>10}"
rows = [
    f"{label:<10} │ {counts['normal']:>7} │ {counts['fever']:>7} │ {counts['high_fever']:>10}"
    for label, counts in results
]

width = max(len(header), max(len(r) for r in rows)) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  TEMPERATURE ANALYSIS BY WARD".center(width) + "│")
print("├" + "─" * width + "┤")
print("│  " + header.ljust(width - 2) + "│")
print("│  " + "─" * (width - 4) + "│")
for row in rows:
    print("│  " + row.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌───────────────────────────────────────────────┐
│           TEMPERATURE ANALYSIS BY WARD        │
├───────────────────────────────────────────────┤
│  Ward       │  normal │   fever │ high_fever  │
│  ───────────────────────────────────────────  │
│  Ward A     │       3 │       2 │          1  │
│  Ward B     │       3 │       0 │          0  │
│  ICU        │       0 │       1 │          3  │
└───────────────────────────────────────────────┘
"""

"""
Чому це — важливий момент перевикористання коду:

def analyze_temperatures(temperatures):
    counts = {"normal": 0, "fever": 0, "high_fever": 0}
    for temp in temperatures:
        category = classify_temperature(temp)   # ← ВИКЛИК готової функції,
        ...                                        #   а НЕ повторення її логіки

# ❌ ПОГАНО — дублювання порогів температури ВСЕРЕДИНІ analyze_temperatures():
def analyze_temperatures(temperatures):
    counts = {"normal": 0, "fever": 0, "high_fever": 0}
    for temp in temperatures:
        if temp < 37.5:              # ← та сама логіка, що вже є в classify_temperature()!
            counts["normal"] += 1
        elif temp < 39.0:
            counts["fever"] += 1
        else:
            counts["high_fever"] += 1
    return counts
    # ПРОБЛЕМА: якщо завтра пороги зміняться (напр. 37.5 → 37.8),
    # доведеться шукати і виправляти ДВА місця в коді — легко забути одне

Перетворення "High fever" → "high_fever":
"High fever".lower()               # → "high fever"
"high fever".replace(" ", "_")      # → "high_fever"

Це дозволяє не переписувати classify_temperature(), а лише "адаптувати" її результат під потрібний формат ключів словника — сама функція класифікації залишається недоторканою й однаковою скрізь, де вона використовується.

Чому всі три ключі — завжди в dict:
counts = {"normal": 0, "fever": 0, "high_fever": 0}   # ← ініціалізація ОДРАЗУ з усіма ключами

for temp in temperatures:
    counts[key] += 1   # тільки ЗБІЛЬШУЄМО існуючий ключ, ніколи не створюємо новий

Це зручніше для подальшого коду, який використає результат: не треба перевіряти if "high_fever" in counts — ключ гарантовано є, навіть якщо значення 0.
"""