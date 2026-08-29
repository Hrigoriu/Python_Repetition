from collections.abc import Callable


def apply_operation(
    value: float,
    operation: Callable[[float], float],
) -> float:
    """Застосовує довільну функцію `operation` до `value`.

    `operation` — це САМА ФУНКЦІЯ, передана як звичайний аргумент
    (без дужок виклику!). apply_operation не знає ЗАЗДАЛЕГІДЬ,
    яку саме операцію застосує — вона просто викликає те,
    що їй передали.
    """
    return operation(value)


def double(x):
    """Подвоює число."""
    return x * 2


def square(x):
    """Підносить число до квадрата."""
    return x**2


def celsius_to_fahrenheit(x):
    """Переводить температуру з Цельсія у Фаренгейт."""
    return x * 9 / 5 + 32


# --- Виклики: та сама функція apply_operation, різна поведінка ---
results = [
    ("apply_operation(5, double)", apply_operation(5, double)),
    ("apply_operation(5, square)", apply_operation(5, square)),
    (
        "apply_operation(37, celsius_to_fahrenheit)",
        apply_operation(37, celsius_to_fahrenheit),
    ),
    # lambda — "анонімна" функція без імені, визначена прямо в місці виклику
    ("apply_operation(10, lambda x: x + 100)", apply_operation(10, lambda x: x + 100)),
]

# --- Вивід у рамці ---
label_width = max(len(label) for label, _ in results)
value_width = max(len(str(v)) for _, v in results)
width = label_width + value_width + 5

print("\n┌" + "─" * width + "┐")
print("│" + "  ФУНКЦІЯ ЯК АРГУМЕНТ".center(width) + "│")
print("├" + "─" * width + "┤")
for label, value in results:
    print(f"│  {label.ljust(label_width)} │ {str(value).ljust(value_width)} │")
print("└" + "─" * width + "┘")
