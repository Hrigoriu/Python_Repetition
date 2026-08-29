THRESHOLD = 39.0


def get_high_risk_patients(patients: list[tuple[str, float]]) -> list[str]:
    """Повертає імена пацієнтів із температурою >= 39.0.

    Використовує list comprehension: одночасно фільтрує (if temp >= THRESHOLD)
    і трансформує (беремо лише name, відкидаючи temp).
    """
    return [name for name, temp in patients if temp >= THRESHOLD]


def get_high_risk_patients_for_loop(patients: list[tuple[str, float]]) -> list[str]:
    """Той самий результат, реалізований звичайним for — для порівняння."""
    result = []
    for name, temp in patients:
        if temp >= THRESHOLD:
            result.append(name)
    return result


# --- Демонстрація ---
patients = [
    ("Ivan", 36.6),
    ("Olena", 38.2),
    ("Petro", 39.1),
    ("Hanna", 37.0),
    ("Dmytro", 39.5),
]

high_risk_comprehension = get_high_risk_patients(patients)
high_risk_for_loop = get_high_risk_patients_for_loop(patients)

# --- Вивід у рамці ---
lines = [
    f"Пацієнти: {patients}",
    "─" * 30,
    f"List comprehension: {high_risk_comprehension}",
    f"Звичайний for:      {high_risk_for_loop}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ПАЦІЄНТИ ГРУПИ РИЗИКУ (≥ 39.0)".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")