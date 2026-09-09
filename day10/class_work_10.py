"""
# !Task 1 — стандартний модуль math!

Створи class_work_10.py.

Використай:
import math

та виведи:
sqrt(144);
ceil(4.2);
floor(4.8);
pi.
"""

# class_work_10.py

import math

# --- Обов'язкові за завданням ---
sqrt_result = math.sqrt(144)      # квадратний корінь
ceil_result = math.ceil(4.2)       # округлення ВГОРУ (до найближчого цілого)
floor_result = math.floor(4.8)     # округлення ВНИЗ (до найближчого цілого)
pi_value = math.pi                  # константа π

# --- Додаткові функції/константи для ознайомлення ---
pow_result = math.pow(2, 10)         # піднесення до степеня (як float)
log_result = math.log(100, 10)        # логарифм за основою 10: log₁₀(100)
e_value = math.e                       # константа e (число Ейлера)

# --- Вивід у рамці ---
lines = [
    f"math.sqrt(144)   = {sqrt_result}",
    f"math.ceil(4.2)    = {ceil_result}",
    f"math.floor(4.8)   = {floor_result}",
    f"math.pi            = {pi_value}",
    "─" * 30,
    f"math.pow(2, 10)    = {pow_result}",
    f"math.log(100, 10)  = {log_result}",
    f"math.e              = {e_value}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  МОДУЛЬ MATH".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌───────────────────────────────────────────┐
│                 МОДУЛЬ MATH               │
├───────────────────────────────────────────┤
│  math.sqrt(144)   = 12.0                  │
│  math.ceil(4.2)    = 5                    │
│  math.floor(4.8)   = 4                    │
│  math.pi            = 3.141592653589793   │
│  ──────────────────────────────           │
│  math.pow(2, 10)    = 1024.0              │
│  math.log(100, 10)  = 2.0                 │
│  math.e              = 2.718281828459045  │
└───────────────────────────────────────────┘
"""

"""
*Пояснення обов'язкових функцій:
math.sqrt(144)   # → 12.0
# квадратний корінь: число, яке, помножене САМЕ НА СЕБЕ, дає 144 (12 × 12 = 144)
# ЗАВЖДИ повертає float, навіть якщо результат "рівний" (12.0, а не 12)

math.ceil(4.2)    # → 5
# "стеля" (ceiling): округлення ВГОРУ до найближчого цілого,
# незалежно від того, наскільки близько число до наступного цілого
math.ceil(4.01)   # → 5   (навіть маленький дробовий залишок округлюється вгору)

math.floor(4.8)   # → 4
# "підлога" (floor): округлення ВНИЗ до найближчого цілого
math.floor(4.99)  # → 4   (навіть майже 5 округлюється вниз)

math.pi           # → 3.141592653589793
# константа — НЕ функція (без дужок!), просто число з бібліотеки

*Різниця ceil()/floor() vs звичайного round():
round(4.2)   # → 4   (округлення за МАТЕМАТИЧНИМ правилом — до найближчого)
round(4.8)   # → 5

math.ceil(4.2)     # → 5   (ЗАВЖДИ вгору, незалежно від того, наскільки близько)
math.floor(4.8)    # → 4   (ЗАВЖДИ вниз, незалежно від того, наскільки близько)

round() округлює до найближчого цілого (як звикли зі школи), а ceil()/floor() завжди йдуть в один конкретний напрямок — це критично важливо в задачах на кшталт "скільки коробок потрібно?" (ceil, бо навіть 0.1 коробки потребує ще однієї цілої) чи "скільки повних наборів вийшло?" (floor, бо неповний залишок не рахується).

*Пояснення додаткових функцій:
math.pow(2, 10)   # → 1024.0
# 2 в 10-му степені. ЗАВЖДИ повертає float
# (на відміну від оператора ** — 2 ** 10 → 1024, int, без .0)

math.log(100, 10)   # → 2.0
#           ↑    ↑
#        число  основа
# "у який степінь треба звести 10, щоб отримати 100?" → 10² = 100 → відповідь 2

math.e             # → 2.718281828459045
# основа натурального логарифма (число Ейлера) — так само, як math.pi,
# фундаментальна математична константа

*Практичне застосування в медичному контексті (для прикладу):
# ceil() — скільки повних упаковок ліків потрібно замовити:
tablets_needed = 47
tablets_per_pack = 10
packs_to_order = math.ceil(tablets_needed / tablets_per_pack)   # → 5 (не 4.7!)

# sqrt() — та сама формула BMI, яку ти вже писав, теж технічно
# використовує піднесення до степеня (** 2), споріднене з math
"""

# ==============================================================================
# ==============================================================================

"""
# !Task 2 — from ... import!

Зроби те саме, але імпортуй конкретні функції:
from math import sqrt, ceil, floor, pi

Порівняй синтаксис.
"""

# class_work_10.py (продовження, або окремий блок)

from math import ceil, floor, pi, sqrt

# --- Ті самі виклики, але БЕЗ префікса "math." ---
sqrt_result = sqrt(144)
ceil_result = ceil(4.2)
floor_result = floor(4.8)
pi_value = pi

# --- Вивід у рамці ---
lines = [
    f"sqrt(144)   = {sqrt_result}",
    f"ceil(4.2)    = {ceil_result}",
    f"floor(4.8)   = {floor_result}",
    f"pi            = {pi_value}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  FROM MATH IMPORT ...".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────────────────┐
│          FROM MATH IMPORT ...       │
├─────────────────────────────────────┤
│  sqrt(144)   = 12.0                 │
│  ceil(4.2)    = 5                   │
│  floor(4.8)   = 4                   │
│  pi            = 3.141592653589793  │
└─────────────────────────────────────┘
"""

"""
*Порівняння синтаксису — Task 1 vs Task 2:
# Task 1: import math
import math
math.sqrt(144)   # ← ЗАВЖДИ через префікс "math."

# Task 2: from math import ...
from math import sqrt, ceil, floor, pi
sqrt(144)          # ← БЕЗ префікса, функція одразу доступна за іменем

*Стисле порівняння переваг/недоліків:
	                import math	                          from math import sqrt, ...
✅ Переваги	       видно, звідки взялась функція 	     коротший код, 
                    (math.sqrt) — не плутається           зручно для частого використання  
                    з власними функціями
⚠️ Недоліки	        трохи довше писати 	                  ризик конфлікту імен: якщо у своєму  
                    (math. щоразу)                        коді напишеш власну функцію sqrt(),
                                                          вона перекриє імпортовану
Коли обирати	    великі проєкти, 	                  короткі скрипти, кілька конкретних
                    багато модулів —                      функцій з одного модуля
                    читабельність важливіша

*Демонстрація ризику конфлікту імен — головна причина обирати import math:
# Варіант 1 — from math import sqrt
from math import sqrt

def sqrt(x):   # ⚠️ ВИПАДКОВО написав ВЛАСНУ функцію з тим самим ім'ям
    return "моя власна функція"

print(sqrt(144))   # → "моя власна функція"
                     # оригінальна math.sqrt() ТИХО "загубилась" — без жодної помилки!

# Варіант 2 — import math
# --- Порівняй з import math — конфлікту НЕ буде: ---
import math

def sqrt(x):   # це ОКРЕМА функція, не пов'язана з math.sqrt
    return "моя власна функція"

print(sqrt(144))        # → "моя власна функція"
print(math.sqrt(144))   # → 12.0  ✅ оригінальна функція ЗАВЖДИ доступна через math.

*Головний практичний висновок: 
import math — безпечніший вибір за замовчуванням, особливо в більших проєктах (як MedAssistant), бо префікс math. завжди чітко показує походження функції й захищає від випадкового "затирання" імен. 
from math import ... варто використовувати свідомо, коли впевнений, що конфліктів імен не буде — наприклад, для 1-2 дуже часто вживаних функцій у невеликому скрипті.
"""

# ==============================================================================
# ==============================================================================

"""
# !Task 3 — власний модуль!

Створи:
patient_utils.py

з функціями:
def normalize_name(name: str) -> str:
    ...

def is_adult(age: int) -> bool:
    ...

def calculate_bmi(weight: float, height: float) -> float:
    ...

Формула:
BMI = weight / height²

де height у метрах.
"""

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
    ВАЖЛИВО: height очікується у МЕТРАХ (не в сантиметрах!),
    інакше результат буде абсурдно малим.
    """
    assert weight > 0, "weight має бути більше 0"
    assert height > 0, "height має бути більше 0"

    return weight / (height ** 2)


# --- Демонстрація роботи модуля (виконується ЛИШЕ при прямому запуску) ---
if __name__ == "__main__":
    print(normalize_name("  ivan  "))       # → Ivan
    print(is_adult(17))                       # → False
    print(is_adult(42))                        # → True
    print(f"{calculate_bmi(82, 1.80):.1f}")     # → 25.3

"""
#*Пояснення height у МЕТРАХ — важлива відмінність від попередніх днів:

# Формула БЕЗ конвертації (як прямо вказано в завданні):
BMI = weight / height ** 2
#              ↑
#          height ВЖЕ у метрах

calculate_bmi(82, 1.80)   # ✅ правильно: 1.80 метра
# 82 / (1.80 ** 2) = 82 / 3.24 = 25.3

calculate_bmi(82, 180)    # ❌ ПАСТКА! Якщо передати 180 (см) замість 1.80 (м):
# 82 / (180 ** 2) = 82 / 32400 = 0.0025   ← абсурдно мале число!

⚠️ Це відрізняється від версії calculate_bmi() із попередніх днів, де функція приймала height_cm (у сантиметрах) і сама ділила на 100 всередині (height_m = height_cm / 100). Тут, за умовою завдання, конвертації немає — функція чекає, що виклик уже передасть значення в метрах. Це важливий нюанс, який варто чітко документувати (що й зроблено в docstring), інакше легко помилитись і передати сантиметри за звичкою з попередніх задач.

#*Пояснення if __name__ == "__main__"::
if __name__ == "__main__":
    print(normalize_name("  ivan  "))
    ...

1.__name__ — спеціальна вбудована змінна Python, яка автоматично отримує значення:
2."__main__" — якщо файл запущено напряму (python patient_utils.py)
3.ім'я модуля ("patient_utils") — якщо файл імпортовано з іншого файлу (import patient_utils)

# Якщо запустити ЦЕЙ файл напряму:
python patient_utils.py
# → __name__ == "__main__" → True → демонстраційний код ВИКОНАЄТЬСЯ

# Якщо ІМПОРТУВАТИ цей файл з іншого скрипту:
import patient_utils
# → __name__ == "patient_utils" → False → демонстраційний код НЕ виконається,
#   доступні лише функції (normalize_name, is_adult, calculate_bmi)

#*Навіщо це потрібно — головна причина використовувати if __name__ == "__main__"::
# ❌ БЕЗ цієї перевірки — демо-код виконається ЩОРАЗУ, навіть при імпорті:
# patient_utils.py:
print(normalize_name("  ivan  "))   # виконається ОДРАЗУ при import patient_utils!

# main.py:
import patient_utils   # 💥 несподівано друкує "Ivan" на екран,
                          #    хоча ти лише хотів ІМПОРТУВАТИ функції

Це стандартна практика для будь-якого файлу, який може використовуватись і як самостійний скрипт (для тестування), і як модуль, з якого імпортують функції в інші файли (наприклад, майбутній class_work_10.py чи MedAssistant).

#*Зв'язок із попередніми задачами: 
# normalize_name() — та сама функція з Практики №3 (день "Комбінація структур"); 
# calculate_bmi() — та сама формула BMI, що вже неодноразово застосовувалась, лише тепер із чіткою вимогою одиниць вимірювання; 
# is_adult() — нова, проста функція, що інкапсулює перевірку age >= 18, замість того щоб писати цю умову "напряму" щоразу, коли вона потрібна.
"""

# ==============================================================================
# ==============================================================================

"""
# !Task 4 — імпорт власного модуля!

У class_work_10.py:

from patient_utils import (
    normalize_name,
    is_adult,
    calculate_bmi,
)

Продемонструй роботу всіх трьох функцій.
"""

# class_work_10.py
# Варіант №1

from patient_utils import (
    calculate_bmi,
    is_adult,
    normalize_name,
)

# --- Демонстрація normalize_name() ---
raw_names = ["  ivan  ", "OLENA", " petro", "HANNA "]
normalized_names = [normalize_name(name) for name in raw_names]

# --- Демонстрація is_adult() ---
patients_ages = [
    ("Ivan", 42),
    ("Sofia", 15),
    ("Petro", 18),
    ("Mykola", 7),
]
adult_checks = [(name, age, is_adult(age)) for name, age in patients_ages]

# --- Демонстрація calculate_bmi() ---
patients_measurements = [
    ("Ivan", 82, 1.80),
    ("Olena", 55, 1.65),
    ("Petro", 95, 1.75),
]
bmi_results = [(name, f"{calculate_bmi(weight, height):.1f}")
               for name, weight, height in patients_measurements]

# --- Вивід у рамці ---
lines = ["normalize_name():"]
lines += [f"  {raw!r} → {norm!r}" for raw, norm in zip(raw_names, normalized_names)]
lines.append("─" * 45)
lines.append("is_adult():")
lines += [f"  {name} ({age} р.) → {result}" for name, age, result in adult_checks]
lines.append("─" * 45)
lines.append("calculate_bmi():")
lines += [f"  {name} ({weight} кг, {height} м) → BMI {bmi}"
          for name, weight, height, bmi
          in [(n, m[1], m[2], r[1]) for n, m, r in zip(
              [p[0] for p in patients_measurements],
              patients_measurements,
              bmi_results
          )]]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ДЕМОНСТРАЦІЯ PATIENT_UTILS".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")



# Варіант №2 - спрощена, чиста версія
# class_work_10.py 

from patient_utils import (
    calculate_bmi,
    is_adult,
    normalize_name,
)

# --- Демонстрація normalize_name() ---
raw_names = ["  ivan  ", "OLENA", " petro", "HANNA "]

# --- Демонстрація is_adult() ---
patients_ages = [
    ("Ivan", 42),
    ("Sofia", 15),
    ("Petro", 18),
    ("Mykola", 7),
]

# --- Демонстрація calculate_bmi() ---
patients_measurements = [
    ("Ivan", 82, 1.80),
    ("Olena", 55, 1.65),
    ("Petro", 95, 1.75),
]

# --- Формуємо рядки для виводу ---
lines = ["normalize_name():"]
for raw in raw_names:
    lines.append(f"  {raw!r} → {normalize_name(raw)!r}")

lines.append("─" * 40)
lines.append("is_adult():")
for name, age in patients_ages:
    lines.append(f"  {name} ({age} р.) → {is_adult(age)}")

lines.append("─" * 40)
lines.append("calculate_bmi():")
for name, weight, height in patients_measurements:
    bmi = calculate_bmi(weight, height)
    lines.append(f"  {name} ({weight} кг, {height} м) → BMI {bmi:.1f}")

# --- Вивід у рамці ---
width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ДЕМОНСТРАЦІЯ PATIENT_UTILS".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────────────────────────────┐
│             ДЕМОНСТРАЦІЯ PATIENT_UTILS          │
├─────────────────────────────────────────────────┤
│  normalize_name():                              │
│    '  ivan  ' → 'Ivan'                          │
│    'OLENA' → 'Olena'                            │
│    ' petro' → 'Petro'                           │
│    'HANNA ' → 'Hanna'                           │
│  ─────────────────────────────────────────────  │
│  is_adult():                                    │
│    Ivan (42 р.) → True                          │
│    Sofia (15 р.) → False                        │
│    Petro (18 р.) → True                         │
│    Mykola (7 р.) → False                        │
│  ─────────────────────────────────────────────  │
│  calculate_bmi():                               │
│    Ivan (82 кг, 1.8 м) → BMI 25.3               │
│    Olena (55 кг, 1.65 м) → BMI 20.2             │
│    Petro (95 кг, 1.75 м) → BMI 31.0             │
└─────────────────────────────────────────────────┘
"""

"""
#*Пояснення from ... import (...) з дужками — синтаксис для кількох імен:
from patient_utils import (
    normalize_name,
    is_adult,
    calculate_bmi,
)

Круглі дужки ( ... ) дозволяють розбити довгий список імпортованих імен на кілька рядків — так само, як ти вже бачив із багаторядковим формуванням рядка звіту (report = (...) у Challenge 4 попереднього дня). 

Це чисто стилістичний прийом для читабельності — синтаксично те саме, що:
from patient_utils import normalize_name, is_adult, calculate_bmi

#*Чому демонстрація важлива саме з РІЗНИМИ прикладами для is_adult():
patients_ages = [
    ("Ivan", 42),     # 42 >= 18 → True
    ("Sofia", 15),    # 15 >= 18 → False
    ("Petro", 18),    # 18 >= 18 → True  ← межовий випадок!
    ("Mykola", 7),    # 7 >= 18  → False
]

Тестовий приклад Petro, 18 — навмисно межовий випадок (edge case): перевіряє, що функція коректно обробляє саме 18 років (а не помилково вимагає > 18, що дало б False для рівно 18-річного). Такі "граничні" тести — важлива звичка для перевірки правильності логіки (пригадай Практику №2 з BMI-межами "без перекриттів" — той самий принцип).

#*Кожна функція протестована на "типовому" наборі даних, що показує різноманітність:
raw_names = ["  ivan  ", "OLENA", " petro", "HANNA "]
# ← різні комбінації: пробіли з обох боків, ВСЕ ВЕЛИКЕ, пробіл лише зліва

patients_measurements = [..., ("Petro", 95, 1.75)]
# ← Petro з BMI ≈ 31.0 (Obesity-категорія з попередніх днів) — показує,
#   що функція коректно рахує і "вищі" значення BMI
"""

# ==============================================================================
# ==============================================================================

"""
#!Task 5 — __name__!

У patient_utils.py додай:
print(f"Module name: {__name__}")

Запусти class_work_10.py і подивись результат.

Потім зроби:
if __name__ == "__main__":
    print("patient_utils.py launched directly")

та поясни різницю.
"""

#1.
# patient_utils.py
"""Утилітарні функції для роботи з даними пацієнтів."""

print(f"Module name: {__name__}")   # ← НОВИЙ рядок: виконується ОДРАЗУ при завантаженні модуля


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


# --- Демонстрація роботи модуля (виконується ЛИШЕ при прямому запуску) ---
if __name__ == "__main__":
    print("patient_utils.py launched directly")
    print(normalize_name("  ivan  "))
    print(is_adult(17))
    print(is_adult(42))
    print(f"{calculate_bmi(82, 1.80):.1f}")

#2.
# class_work_10.py

from patient_utils import (
    calculate_bmi,
    is_adult,
    normalize_name,
)

# --- Демонстрація normalize_name() ---
raw_names = ["  ivan  ", "OLENA", " petro", "HANNA "]

# --- Демонстрація is_adult() ---
patients_ages = [
    ("Ivan", 42),
    ("Sofia", 15),
    ("Petro", 18),
    ("Mykola", 7),
]

# --- Демонстрація calculate_bmi() ---
patients_measurements = [
    ("Ivan", 82, 1.80),
    ("Olena", 55, 1.65),
    ("Petro", 95, 1.75),
]

lines = ["normalize_name():"]
for raw in raw_names:
    lines.append(f"  {raw!r} → {normalize_name(raw)!r}")

lines.append("─" * 40)
lines.append("is_adult():")
for name, age in patients_ages:
    lines.append(f"  {name} ({age} р.) → {is_adult(age)}")

lines.append("─" * 40)
lines.append("calculate_bmi():")
for name, weight, height in patients_measurements:
    bmi = calculate_bmi(weight, height)
    lines.append(f"  {name} ({weight} кг, {height} м) → BMI {bmi:.1f}")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ДЕМОНСТРАЦІЯ PATIENT_UTILS".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
Результат запуску python patient_utils.py (напряму):
Module name: __main__
patient_utils.py launched directly
Ivan
False
True
25.3
"""

"""
#*Пояснення — чому тут __name__ == "__main__":

Коли файл запускається безпосередньо командою python patient_utils.py, Python встановлює для цього конкретного файлу __name__ = "__main__" — незалежно від того, як файл насправді називається. 
Тому й print(f"Module name: {__name__}") виведе __main__, і блок if __name__ == "__main__": виконається.

#*Головна різниця — зведена таблиця:
Спосіб запуску	                __name__ 	        if __name__ == "__main__": 
                                дорівнює            виконається?
python patient_utils.py 	    "__main__"	        ✅ Так
    (напряму)
import patient_utils 	        "patient_utils"	    ❌ Ні
    (з іншого файлу)

#*Ключовий висновок — навіщо це важливо на практиці:
print(f"Module name: {__name__}")   # ← БЕЗ УМОВИ — виконується ЗАВЖДИ, при кожному запуску
                                       #    (і при import, і при прямому запуску) — 
                                       #    це "побічний ефект", якого зазвичай хочеться уникнути

if __name__ == "__main__":
    print("patient_utils.py launched directly")   # ← З УМОВОЮ — виконується ЛИШЕ
                                                     #    при прямому запуску файлу

1.Перший рядок (print без умови) демонструє проблему: код у модулі виконується щоразу, коли модуль завантажується — навіть якщо ти лише хотів скористатись функціями з нього, а не запускати його "демо". 
2.Другий підхід (if __name__ == "__main__":) — це правильне, стандартне рішення: код усередині блоку виконується тільки тоді, коли файл є точкою входу програми, а не просто бібліотекою функцій, яку хтось інший імпортує.

Саме тому в patient_utils.py демонстраційний код (виклики normalize_name(), is_adult() тощо) обгорнутий у if __name__ == "__main__": — а от голий print(f"Module name: ...") навмисно залишений без умови в цьому завданні, щоб наочно показати різницю в поведінці.
"""

# ==============================================================================
# ==============================================================================

"""
# !Task 6 — окремий модуль статистики!

Створи:
statistics_utils.py

з функціями:
def average(numbers: list[float]) -> float:
    ...

def maximum(numbers: list[float]) -> float:
    ...

def minimum(numbers: list[float]) -> float:
    ...

Потім імпортуй їх у class_work_10.py.
"""

#1.
"""statistics_utils.py

Aggregate statistics over a list of patient records, for MedAssistant.
"""


def average_age(patients: list[dict]) -> float:
    """Compute the average age across all patients.

    Args:
        patients: A list of patient records (must include "age").

    Returns:
        float: The average age.
    """
    return sum(p["age"] for p in patients) / len(patients)


def average_temperature(patients: list[dict]) -> float:
    """Compute the average temperature across all patients.

    Args:
        patients: A list of patient records (must include "temperature").

    Returns:
        float: The average temperature.
    """
    return sum(p["temperature"] for p in patients) / len(patients)


def oldest_patient(patients: list[dict]) -> dict:
    """Find the oldest patient in the list.

    Args:
        patients: A list of patient records (must include "age").

    Returns:
        dict: The patient record with the highest age.
    """
    return max(patients, key=lambda p: p["age"])

#2.
# class_work_10.py

from patient_utils import normalize_name, is_adult, calculate_bmi
from statistics_utils import average, maximum, minimum

# --- Дані для демонстрації статистики ---
patient_temperatures = [36.6, 38.2, 37.4, 39.1, 36.9]

# --- Обчислення через statistics_utils ---
avg_temp = average(patient_temperatures)
max_temp = maximum(patient_temperatures)
min_temp = minimum(patient_temperatures)

# --- Перевірка на порожньому списку ---
try:
    average([])
except ValueError as e:
    empty_list_error = f"❌ ValueError: {e}"

# --- Вивід у рамці ---
lines = [
    f"Температури: {patient_temperatures}",
    "─" * 40,
    f"average(): {avg_temp:.2f}",
    f"maximum(): {max_temp}",
    f"minimum(): {min_temp}",
    "─" * 40,
    f"average([]) → {empty_list_error}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  STATISTICS_UTILS".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
Module name: patient_utils

┌───────────────────────────────────────────────────────────────────┐
│                           STATISTICS_UTILS                        │
├───────────────────────────────────────────────────────────────────┤
│  Температури: [36.6, 38.2, 37.4, 39.1, 36.9]                      │
│  ────────────────────────────────────────                         │
│  average(): 37.64                                                 │
│  maximum(): 39.1                                                  │
│  minimum(): 36.6                                                  │
│  ────────────────────────────────────────                         │
│  average([]) → ❌ ValueError: Список чисел не може бути порожнім.  │
└───────────────────────────────────────────────────────────────────┘
"""

"""
#*Пояснення _check_not_empty() — приватна допоміжна функція (DRY):
def _check_not_empty(numbers):
    if not numbers:
        raise ValueError("Список чисел не може бути порожнім.")

Замість того, щоб писати if not numbers: raise ValueError(...) тричі (в average, maximum, minimum), логіка перевірки винесена в одну окрему функцію, яку викликають усі три. Якщо завтра захочеш змінити текст помилки чи логіку перевірки — правиш лише одне місце.

#*Чому назва починається з підкреслення _check_not_empty:
def _check_not_empty(numbers):   # ← підкреслення на початку
    ...

Це конвенція (домовленість) у Python: функція/змінна з _ на початку сигналізує "внутрішнє використання" — вона призначена лише для допомоги всередині цього модуля, а не для того, щоб хтось ІНШИЙ імпортував і викликав _check_not_empty() напряму з іншого файлу. Python технічно не забороняє це зробити, але підкреслення — чіткий сигнал "не використовуй це ззовні".

#*Порівняння двох варіантів реалізації:
# Варіант A — коротко, покладаємось на вбудовані функції:
def average(numbers):
    return sum(numbers) / len(numbers)

# Варіант B — довше, але показує, ЩО САМЕ відбувається "під капотом":
def average_manual(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)
	
                    Варіант A	                 Варіант B
Рядків коду	        1-2	                          4-5
Швидкість	        ✅ вбудовані функції 	    звичайна (чистий Python)
                    оптимізовані (написані на C)
Навчальна цінність	менша (це вже "магія")	     ✅ показує саму логіку алгоритму
Продакшн-код	    ✅ завжди обирай це	        лише для навчання/розуміння

#*Головний практичний висновок: 
# для реального коду (як у MedAssistant) завжди варто обирати Варіант A — вбудовані функції sum(), max(), min() надійніші (перевірені мільйонами розробників) і швидші за будь-яку "саморобну" реалізацію. 
# для навчання — Варіант B корисний виключно, щоб зрозуміти, як ці вбудовані функції насправді працюють "під капотом".

#*Обробка порожнього списку — де саме падає помилка:
average([])
# 1. Викликається average([])
# 2. Усередині: _check_not_empty([])
# 3. not [] → True (порожній список — falsy, як у Challenge №2 попередніх днів)
# 4. raise ValueError("Список чисел не може бути порожнім.")
# 5. Помилка "спливає" з average() назовні — функція НЕ доходить до sum(numbers)/len(numbers)

Без цієї перевірки average([]) викликала б sum([]) / len([]) → 0 / 0 → незрозумілу ZeroDivisionError, замість чіткого повідомлення про справжню причину проблеми (порожній вхід).
"""

# ==============================================================================
# ==============================================================================

"""
# !Task 7 — правильна структура!

Перебудуй код так:
day10/
├── class_work_10.py
├── patient_utils.py
└── statistics_utils.py

У class_work_10.py повинні залишитися переважно:
imports
↓
data
↓
calls
↓
output

А не реалізації всіх функцій.
"""

#1.
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

#2.
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

#3.
# class_work_10.py

# ═══════════════════════════════════════════
# IMPORTS
# ═══════════════════════════════════════════
from patient_utils import normalize_name, is_adult, calculate_bmi
from statistics_utils import average, maximum, minimum


# ═══════════════════════════════════════════
# DATA
# ═══════════════════════════════════════════
raw_names = ["  ivan  ", "OLENA", " petro", "HANNA "]

patients_ages = [
    ("Ivan", 42),
    ("Sofia", 15),
    ("Petro", 18),
    ("Mykola", 7),
]

patients_measurements = [
    ("Ivan", 82, 1.80),
    ("Olena", 55, 1.65),
    ("Petro", 95, 1.75),
]

patient_temperatures = [36.6, 38.2, 37.4, 39.1, 36.9]


# ═══════════════════════════════════════════
# CALLS
# ═══════════════════════════════════════════
normalized_names = [normalize_name(name) for name in raw_names]
adult_checks = [(name, age, is_adult(age)) for name, age in patients_ages]
bmi_results = [
    (name, calculate_bmi(weight, height))
    for name, weight, height in patients_measurements
]

avg_temp = average(patient_temperatures)
max_temp = maximum(patient_temperatures)
min_temp = minimum(patient_temperatures)

try:
    average([])
    empty_check = "не впало (несподівано)"
except ValueError as e:
    empty_check = f"❌ ValueError: {e}"


# ═══════════════════════════════════════════
# OUTPUT
# ═══════════════════════════════════════════
def print_framed(title: str, lines: list[str]) -> None:
    """Допоміжна функція ВИВОДУ — не бізнес-логіка, лише форматування."""
    width = max(len(title), max(len(line) for line in lines)) + 4
    print("\n┌" + "─" * width + "┐")
    print("│" + f"  {title}".center(width) + "│")
    print("├" + "─" * width + "┤")
    for line in lines:
        print("│  " + line.ljust(width - 2) + "│")
    print("└" + "─" * width + "┘")


print_framed("NORMALIZE_NAME()", [
    f"{raw!r} → {norm!r}" for raw, norm in zip(raw_names, normalized_names)
])

print_framed("IS_ADULT()", [
    f"{name} ({age} р.) → {result}" for name, age, result in adult_checks
])

print_framed("CALCULATE_BMI()", [
    f"{name} ({weight} кг, {height} м) → BMI {bmi:.1f}"
    for (name, weight, height), (_, bmi) in zip(patients_measurements, bmi_results)
])

print_framed("STATISTICS_UTILS", [
    f"Температури: {patient_temperatures}",
    f"average(): {avg_temp:.2f}",
    f"maximum(): {max_temp}",
    f"minimum(): {min_temp}",
    f"average([]) → {empty_check}",
])

"""
┌───────────────────────┐
│     NORMALIZE_NAME()  │
├───────────────────────┤
│  '  ivan  ' → 'Ivan'  │
│  'OLENA' → 'Olena'    │
│  ' petro' → 'Petro'   │
│  'HANNA ' → 'Hanna'   │
└───────────────────────┘

┌─────────────────────────┐
│         IS_ADULT()      │
├─────────────────────────┤
│  Ivan (42 р.) → True    │
│  Sofia (15 р.) → False  │
│  Petro (18 р.) → True   │
│  Mykola (7 р.) → False  │
└─────────────────────────┘

┌────────────────────────────────────┐
│           CALCULATE_BMI()          │
├────────────────────────────────────┤
│  Ivan (82 кг, 1.8 м) → BMI 25.3    │
│  Olena (55 кг, 1.65 м) → BMI 20.2  │
│  Petro (95 кг, 1.75 м) → BMI 31.0  │
└────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────┐
│                           STATISTICS_UTILS                        │
├───────────────────────────────────────────────────────────────────┤
│  Температури: [36.6, 38.2, 37.4, 39.1, 36.9]                      │
│  average(): 37.64                                                 │
│  maximum(): 39.1                                                  │
│  minimum(): 36.6                                                  │
│  average([]) → ❌ ValueError: Список чисел не може бути порожнім.  │
└───────────────────────────────────────────────────────────────────┘
"""

"""
#*Що саме змінилось структурно:
ДО (Task 4-6):                      ПІСЛЯ (Task 7):
class_work_10.py містив:            class_work_10.py містить ЛИШЕ:
- import                             - import       ✅
- дані                                - дані          ✅
- виклики функцій                      - виклики       ✅
- inline-форматування виводу            - виклик print_framed()
  (повторюваний код рамки            - print_framed() — ОДНА функція
   в кожному блоці)                    форматування, а не дублювання
                                        коду рамки чотири рази

#*Чому print_framed() — це НЕ порушення принципу "лише imports/data/calls/output":
def print_framed(title, lines):
    ...

Це не бізнес-логіка (не рахує BMI, не перевіряє вік) — це чисто допоміжна функція форматування виводу, яка належить саме до розділу OUTPUT. Вона винесена в окрему функцію, бо код рамки (┌─┐│└┘) повторювався в кожному з чотирьох блоків Task 4 і Task 6 — це порушувало DRY. Тепер print_framed() викликається чотири рази з різними даними, замість чотирьох майже однакових шматків коду малювання рамки.

#*Головний принцип file structure, який демонструє це завдання:
Файл	            Відповідальність
patient_utils.py	ЩО робити з даними пацієнта (нормалізація, перевірка віку, BMI)
statistics_utils.py	ЩО робити зі списками чисел (середнє, максимум, мінімум)
class_work_10.py	ЯКІ дані використати і ЯК показати результат

Це називається розділення відповідальностей на рівні файлів (не лише функцій, як раніше) — кожен модуль відповідає за одну сферу логіки, а головний скрипт лише координує їх, не реалізуючи власну "бізнес-логіку" всередині себе. Це та сама архітектурна ідея, що вже застосовувалась у main() з "MedAssistant Data Pipeline" (Challenge 6, day09) — тільки там розділення було на рівні функцій усередині одного файлу, а тут — на рівні окремих файлів-модулів.
"""
