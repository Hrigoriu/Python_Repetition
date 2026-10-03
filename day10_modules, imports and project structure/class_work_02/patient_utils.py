# patient_utils.py
"""Утилітарні функції для роботи з даними пацієнтів."""


def normalize_name(name: str) -> str:
    """Прибирає пробіли та приводить ім'я до формату 'Перша літера велика'."""
    return name.strip().capitalize()


def is_adult(age: int) -> bool:
    """Перевіряє, чи є пацієнт повнолітнім (18 років і більше)."""
    return age >= 18


def calculate_bmi(weight: float, height: float) -> float:
    """Обчислює BMI (індекс маси тіла).

    Формула: BMI = weight / height²
    ВАЖЛИВО: height очікується у МЕТРАХ (не в сантиметрах!).
    """
    assert weight > 0, "weight має бути більше 0"
    assert height > 0, "height має бути більше 0"
    return weight / (height ** 2)


if __name__ == "__main__":
    print("patient_utils.py launched directly")
    print(normalize_name("  ivan  "))
    print(is_adult(42))
    print(f"{calculate_bmi(82, 1.80):.1f}")