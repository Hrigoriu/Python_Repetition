# statistics_utils.py
"""Утилітарні функції для базової статистики над списками чисел."""


def _check_not_empty(numbers: list[float]) -> None:
    """Спільна перевірка для всіх трьох функцій — не дублюємо валідацію."""
    if not numbers:
        raise ValueError("Список чисел не може бути порожнім.")


# ═══════════════════════════════════════════
# ВАРІАНТ A — прості обгортки навколо вбудованих функцій (KISS)
# ═══════════════════════════════════════════
def average(numbers: list[float]) -> float:
    """Обчислює середнє арифметичне списку чисел."""
    _check_not_empty(numbers)
    return sum(numbers) / len(numbers)


def maximum(numbers: list[float]) -> float:
    """Знаходить найбільше число у списку."""
    _check_not_empty(numbers)
    return max(numbers)


def minimum(numbers: list[float]) -> float:
    """Знаходить найменше число у списку."""
    _check_not_empty(numbers)
    return min(numbers)


# ═══════════════════════════════════════════
# ВАРІАНТ B — ручна реалізація через for (без sum()/max()/min())
# ═══════════════════════════════════════════
def average_manual(numbers: list[float]) -> float:
    """Те саме, але БЕЗ вбудованої sum() — рахуємо суму вручну."""
    _check_not_empty(numbers)

    total = 0
    for number in numbers:
        total += number

    return total / len(numbers)


def maximum_manual(numbers: list[float]) -> float:
    """Те саме, але БЕЗ вбудованої max() — шукаємо рекорд вручну."""
    _check_not_empty(numbers)

    result = numbers[0]
    for number in numbers:
        if number > result:
            result = number

    return result


def minimum_manual(numbers: list[float]) -> float:
    """Те саме, але БЕЗ вбудованої min() — шукаємо рекорд вручну."""
    _check_not_empty(numbers)

    result = numbers[0]
    for number in numbers:
        if number < result:
            result = number

    return result


# --- Демонстрація роботи модуля (виконується ЛИШЕ при прямому запуску) ---
if __name__ == "__main__":
    sample = [36.6, 38.2, 37.4, 39.1, 36.9]
    print(f"average({sample}) = {average(sample):.2f}")
    print(f"maximum({sample}) = {maximum(sample)}")
    print(f"minimum({sample}) = {minimum(sample)}")

"""
average([36.6, 38.2, 37.4, 39.1, 36.9]) = 37.64
maximum([36.6, 38.2, 37.4, 39.1, 36.9]) = 39.1
minimum([36.6, 38.2, 37.4, 39.1, 36.9]) = 36.6
"""
