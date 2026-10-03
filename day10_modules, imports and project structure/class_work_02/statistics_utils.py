# statistics_utils.py
"""Утилітарні функції для базової статистики над списками чисел."""


def _check_not_empty(numbers: list[float]) -> None:
    if not numbers:
        raise ValueError("Список чисел не може бути порожнім.")


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


if __name__ == "__main__":
    sample = [36.6, 38.2, 37.4, 39.1, 36.9]
    print(f"average({sample}) = {average(sample):.2f}")
    print(f"maximum({sample}) = {maximum(sample)}")
    print(f"minimum({sample}) = {minimum(sample)}")