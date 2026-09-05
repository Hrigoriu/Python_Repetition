# class_work_09.py (продовження)

import json


def load_json(path: str) -> dict | list | None:
    """Безпечно завантажує JSON-файл, обробляючи типові помилки.

    Args:
        path: Шлях до JSON-файлу.

    Returns:
        dict | list | None: Дані з файлу (dict або list — залежно від
            структури JSON), або None, якщо сталася помилка.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"⚠ Помилка: файл '{path}' не знайдено.")
        return None
    except json.JSONDecodeError as e:
        print(f"⚠ Помилка: файл '{path}' містить некоректний JSON ({e}).")
        return None


# --- Підготовка тестових файлів ---

# 1. Валідний файл (уже існує з попередніх задач)
# data/patients.json — вже коректний JSON

# 2. Навмисно "зіпсований" JSON (для демонстрації JSONDecodeError)
with open("data/broken.json", "w", encoding="utf-8") as file:
    file.write('{"name": "Ivan", "age": }')  # ← некоректний синтаксис (немає значення)


# --- Демонстрація трьох сценаріїв ---
result_valid = load_json("data/patients.json")
result_missing = load_json("data/nonexistent.json")
result_broken = load_json("data/broken.json")

# --- Вивід у рамці ---
lines = [
    (
        f"load_json('data/patients.json')   → {type(result_valid).__name__}"
        f" ({'дані завантажено' if result_valid is not None else 'None'})"
    ),
    f"load_json('data/nonexistent.json') → {result_missing}",
    f"load_json('data/broken.json')      → {result_broken}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  LOAD_JSON() — ОБРОБКА ПОМИЛОК".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")
