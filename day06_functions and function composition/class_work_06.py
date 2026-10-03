"""
# !Практика №1 — проста функція!

Напиши:
def greet(name: str) -> str:
    ...

яка повертає:
Hello, Hrigoriu!

Не використовуй print() всередині функції.
"""


def greet(name: str) -> str:
    "Повертає привітання для заданого імені."
    return f"Hello, {name}!"


# --- Кілька прикладів виклику ---
greeting_1 = greet("Hrigoriu")
greeting_2 = greet("Olena")

# --- Вивід у рамці ---
lines = [
    greeting_1,
    greeting_2,
]
width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  GREET()".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")


"""
┌────────────────────┐
│       GREET()      │
├────────────────────┤
│  Hello, Hrigoriu!  │
│  Hello, Olena!     │
└────────────────────┘
"""

"""
**Чому `return`, а не `print()` всередині функції:**

Це одна з найважливіших звичок для написання якісного коду. 
Різниця:
"""


# ❌ ПОГАНО — функція сама вирішує "показати" результат:
def greet(name: str) -> None:
    print(f"Hello, {name}!")  # функція ЩОСЬ РОБИТЬ (side effect), нічого не повертає


result = greet("Ivan")  # виведе "Hello, Ivan!" на екран
print(result)  # → None !!! бо greet() нічого не return-ить


# ✅ ДОБРЕ — функція повертає ДАНІ, а виклик коду вирішує, що з ними робити:
def greet(name: str) -> str:
    return f"Hello, {name}!"  # функція ПОВЕРТАЄ значення, нічого не друкує


result = greet("Ivan")  # нічого не виводиться, result = "Hello, Ivan!"
print(result)  # ← ТУТ ми вирішуємо вивести


"""
**Три причини, чому `return` краще за `print()` всередині функції:**

1. **Гнучкість використання** — результат `return` можна вивести, записати у файл, надіслати по мережі, порівняти з іншим рядком, підставити в інший рядок. 
Результат `print()` — лише текст на екрані, з ним більше нічого не зробиш програмно.

```python
greeting = greet("Ivan")
if "Ivan" in greeting:          # ✅ можна аналізувати
    print("Знайдено ім'я")

log_file.write(greet("Ivan"))   # ✅ можна записати у файл
```

2. **Тестованість** — функцію з `return` легко перевірити автоматично:
```python
assert greet("Ivan") == "Hello, Ivan!"   # ✅ просто порівняти результат

# З print() всередині — так перевірити НЕ можна,
# бо print() нічого не повертає (результат — None)
```

3. **Композиція (об'єднання функцій)** — результат однієї функції можна одразу передати в іншу:
```python
def shout(text: str) -> str:
    return text.upper()

print(shout(greet("Ivan")))   # ✅ "HELLO, IVAN!"
# Це неможливо, якщо greet() сама вже все надрукувала і повернула None
```

**Правило "гарного тону" в Python:
** функції, що **обчислюють** щось — повертають результат (`return`). 
** функції, що **виводять** щось на екран — викликаються окремо, у "верхньому рівні" програми, а не всередині логіки обчислень.
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №2 — математичні функції!

Створи:
def add(a: float, b: float) -> float:
    ...

def subtract(a: float, b: float) -> float:
    ...

def multiply(a: float, b: float) -> float:
    ...

def divide(a: float, b: float) -> float:
    ...

Для divide() передбач:
ZeroDivisionError
або власну перевірку.
"""


def add(a: float, b: float) -> float:
    "Повертає суму двох чисел."
    return a + b


def subtract(a: float, b: float) -> float:
    "Повертає різницю двох чисел."
    return a - b


def multiply(a: float, b: float) -> float:
    "Повертає добуток двох чисел."
    return a * b


def divide(a: float, b: float) -> float:
    """Повертає частку від ділення a на b.
    Власна перевірка на нуль — дає ЗРОЗУМІЛЕ повідомлення про помилку,
    замість того, щоб чекати, поки Python сам кине ZeroDivisionError.
    """
    if b == 0:
        raise ValueError("Ділення на нуль неможливе (b дорівнює 0).")
    return a / b


def divide_raw(a: float, b: float) -> float:
    """Те саме, але БЕЗ власної перевірки —
    Python сам кине стандартний ZeroDivisionError.
    """
    return a / b  # якщо b == 0 → Python автоматично кидає ZeroDivisionError


# --- Демонстрація роботи ---
results = []

results.append(("add(10, 5)", add(10, 5)))
results.append(("subtract(10, 5)", subtract(10, 5)))
results.append(("multiply(10, 5)", multiply(10, 5)))
results.append(("divide(10, 5)", divide(10, 5)))

# --- Порівняння двох підходів до ділення на 0 ---
try:
    divide(10, 0)  # з власною перевіркою → ValueError
except ValueError as e:
    results.append(("divide(10, 0) — власна перевірка", f"❌ ValueError: {e}"))

try:
    divide_raw(10, 0)  # без перевірки → ZeroDivisionError
except ZeroDivisionError as e:
    results.append(("divide_raw(10, 0) — без перевірки", f"❌ ZeroDivisionError: {e}"))

# --- Вивід у рамці ---
label_width = max(len(label) for label, _ in results)
value_width = max(len(str(v)) for _, v in results)
width = label_width + value_width + 5

print("\n┌" + "─" * width + "┐")
print("│" + "  МАТЕМАТИЧНІ ФУНКЦІЇ".center(width) + "│")
print("├" + "─" * width + "┤")
for label, value in results:
    print(f"│  {label.ljust(label_width)} │ {str(value).ljust(value_width)} │")
print("└" + "─" * width + "┘")


"""
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                      МАТЕМАТИЧНІ ФУНКЦІЇ                                    │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│  add(10, 5)                        │ 15                                                      │
│  subtract(10, 5)                   │ 5                                                       │
│  multiply(10, 5)                   │ 50                                                      │
│  divide(10, 5)                     │ 2.0                                                     │
│  divide(10, 0) — власна перевірка  │ ❌ ValueError: Ділення на нуль неможливе (b дорівнює 0). │
│  divide_raw(10, 0) — без перевірки │ ❌ ZeroDivisionError: division by zero                   │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
"""


# Порівняння двох підходів до ділення на 0:**
# --- Варіант 1: власна перевірка (raise ValueError) ---
def divide(a, b):
    if b == 0:
        raise ValueError("Ділення на нуль неможливе (b дорівнює 0).")
    return a / b


# --- Варіант 2: без перевірки (Python сам кидає помилку) ---
def divide_raw(a, b):
    return a / b  # b == 0 → автоматично ZeroDivisionError


"""
|---|---|---|---|---|Власна перевірка (`ValueError`)    |Стандартна (`ZeroDivisionError`) |
| Повідомлення      |✅ твоє власне, зрозуміле         |⚠️ технічне: `"division by zero"` |
| Контроль          |✅ можеш додати іншу логіку (лог, дефолтне значення) | ❌ лише те, що дає Python |
| Швидкість написання |трохи більше коду                |найкоротший варіант |
| Коли краще        |публічне API, бібліотека для інших |внутрішній швидкий скрипт |

#Чому `raise`, а не `return None` при помилці:**

# ❌ ПОГАНО — помилку легко пропустити:
def divide(a, b):
    if b == 0:
        return None   # викликач може забути перевірити на None!

result = divide(10, 0)
print(result * 2)   # 💥 TypeError десь далі в коді, важко знайти причину

# ✅ ДОБРЕ — помилка "голосно" зупиняє виконання одразу там, де сталась:
def divide(a, b):
    if b == 0:
        raise ValueError("...")

result = divide(10, 0)   # 💥 ValueError одразу тут, з чіткою причиною
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №3 — BMI!

Створи:
def calculate_bmi(
    weight: float,
    height_cm: float,
) -> float:
    ...

Вимоги:
weight > 0;
height_cm > 0;
повернути BMI;
результат округляти не всередині функції.

Наприклад:
bmi = calculate_bmi(82, 180)
print(f"BMI: {bmi:.1f}")
"""


def calculate_bmi(weight: float, height_cm: float) -> float:
    """Обчислює BMI (індекс маси тіла).

    assert перевіряє коректність вхідних даних — якщо умова False,
    Python одразу зупиняє програму з AssertionError.
    Округлення НЕ робиться тут — функція повертає "сире" число,
    а форматування (скільки знаків показати) — це відповідальність
    того коду, який ВИКЛИКАЄ функцію, а не самої функції.
    """
    assert weight > 0, "weight має бути більше 0"
    assert height_cm > 0, "height_cm має бути більше 0"

    height_m = height_cm / 100
    return weight / (height_m**2)


# --- Тестові випадки ---
test_cases = [
    (82, 180),
    (55, 165),
    (95, 175),
]

results = []
for weight, height in test_cases:
    bmi = calculate_bmi(weight, height)
    results.append((f"calculate_bmi({weight}, {height})", f"{bmi:.1f}"))

# --- Тест перевірки assert (некоректні дані) ---
try:
    calculate_bmi(-10, 180)
except AssertionError as e:
    results.append(("calculate_bmi(-10, 180)", f"❌ AssertionError: {e}"))

try:
    calculate_bmi(70, 0)
except AssertionError as e:
    results.append(("calculate_bmi(70, 0)", f"❌ AssertionError: {e}"))

# --- Вивід у рамці ---
label_width = max(len(label) for label, _ in results)
value_width = max(len(str(v)) for _, v in results)
width = label_width + value_width + 5

print("\n┌" + "─" * width + "┐")
print("│" + "  CALCULATE_BMI()".center(width) + "│")
print("├" + "─" * width + "┤")
for label, value in results:
    print(f"│  {label.ljust(label_width)} │ {str(value).ljust(value_width)} │")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────────────────────────────────────────────────────┐
│                              CALCULATE_BMI()                            │
├─────────────────────────────────────────────────────────────────────────┤
│  calculate_bmi(82, 180)  │ 25.3                                          │
│  calculate_bmi(55, 165)  │ 20.2                                          │
│  calculate_bmi(95, 175)  │ 31.0                                          │
│  calculate_bmi(-10, 180) │ ❌ AssertionError: weight має бути більше 0    │
│  calculate_bmi(70, 0)    │ ❌ AssertionError: height_cm має бути більше 0 │
└─────────────────────────────────────────────────────────────────────────┘
"""

"""
Якщо умова True — assert нічого не робить, код продовжується як звичайно. 
Якщо False — одразу кидає AssertionError і зупиняє виконання.

assert vs raise ValueError — коли що використовувати:

	                    assert	                                                    raise ValueError
Призначення	            перевірка логіки програми ("цього не повинно статись")	    перевірка вхідних даних від користувача
Можна вимкнути	        ✅ так, флагом python -O (прибирає всі assert)	          ❌ ні, завжди активна
Використання в продакшн	⚠️ обережно — може бути вимкнено	                       ✅ надійно

⚠️ Важливий нюанс: 
assert можна повністю вимкнути прапорцем -O при запуску (python -O script.py) — тоді всі перевірки assert просто зникають, і код продовжить виконуватись навіть з некоректними даними! Тому для навчальних задач і внутрішньої логіки assert — це нормально, але для публічного API (яке викликають інші люди) частіше обирають raise ValueError, як у минулому завданні з divide().

Чому округлення не робиться всередині функції:

# ❌ ПОГАНО — функція нав'язує СВОЄ уявлення про округлення:
def calculate_bmi(weight, height_cm):
    ...
    return round(bmi, 1)   # завжди 1 знак — а якщо комусь треба 2?

# ✅ ДОБРЕ — функція повертає точне значення,
#    а той, хто ВИКЛИКАЄ функцію, сам вирішує, як його показати:
bmi = calculate_bmi(82, 180)   # bmi = 25.30864197530864 (точне)
print(f"{bmi:.1f}")             # → 25.3  (округлення тільки для показу)
print(f"{bmi:.3f}")             # → 25.309 (можна інакше — дані не втрачені)
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №4 — категорія BMI!

Створи окрему функцію:
def bmi_category(bmi: float) -> str:
    ...

Вона повинна повертати:
Underweight
Normal
Overweight
Obesity

Важливо
Не змішуй:
calculate_bmi()

та:
bmi_category()
в одну функцію.

Це перше практичне тренування separation of concerns.
"""


def calculate_bmi(weight: float, height_cm: float) -> float:
    """Обчислює BMI. Не знає нічого про категорії — лише число."""
    assert weight > 0, "weight має бути більше 0"
    assert height_cm > 0, "height_cm має бути більше 0"

    height_m = height_cm / 100
    return weight / (height_m**2)


def bmi_category(bmi: float) -> str:
    """Визначає категорію за ЧИСЛОВИМ значенням BMI.

    Не знає НІЧОГО про вагу чи зріст — приймає лише готове число.
    Це і є розділення відповідальностей (separation of concerns):
    одна функція рахує BMI, інша — лише класифікує вже готове число.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:  # Python вже знає: bmi >= 18.5
        return "Normal"
    elif bmi < 30:  # Python вже знає: bmi >= 25
        return "Overweight"
    else:  # bmi >= 30
        return "Obesity"


# --- Використання ОБОХ функцій разом, але окремо ---
test_cases = [
    (82, 180),
    (55, 165),
    (95, 175),
    (48, 170),
]

results = []
for weight, height in test_cases:
    bmi = calculate_bmi(weight, height)  # функція 1: тільки рахує
    category = bmi_category(bmi)  # функція 2: тільки класифікує
    results.append((f"{weight} кг, {height} см", f"BMI {bmi:.1f} → {category}"))

# --- Вивід у рамці ---
label_width = max(len(label) for label, _ in results)
value_width = max(len(value) for _, value in results)
width = label_width + value_width + 5

print("\n┌" + "─" * width + "┐")
print("│" + "  BMI CALCULATOR".center(width) + "│")
print("├" + "─" * width + "┤")
for label, value in results:
    print(f"│  {label.ljust(label_width)} │ {value.ljust(value_width)} │")
print("└" + "─" * width + "┘")

"""
┌────────────────────────────────────────┐
│              BMI CALCULATOR            │
├────────────────────────────────────────┤
│  82 кг, 180 см │ BMI 25.3 → Overweight  │
│  55 кг, 165 см │ BMI 20.2 → Normal      │
│  95 кг, 175 см │ BMI 31.0 → Obesity     │
│  48 кг, 170 см │ BMI 16.6 → Underweight │
└────────────────────────────────────────┘
"""

"""
Чому важливо НЕ змішувати ці дві функції — суть separation of concerns:

# ❌ ПОГАНО — одна функція робить ДВІ різні речі:
def calculate_bmi_and_category(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    # ... і т.д.
    # ПРОБЛЕМА: якщо комусь треба саме ЧИСЛО bmi (для графіка, для БД,
    # для порівняння з попереднім виміром) — воно ВТРАЧЕНО,
    # функція повернула тільки текст категорії!


# ✅ ДОБРЕ — кожна функція робить ОДНУ річ:
bmi = calculate_bmi(82, 180)      # ← можна використати САМЕ число bmi
category = bmi_category(bmi)      # ← а можна ще й класифікувати

print(bmi)         # 25.3 ... — для графіків, аналітики, БД
print(category)    # "Overweight" — для показу людині


Три практичні переваги розділення:
1. Повторне використання — bmi_category() можна застосувати навіть якщо BMI прийшов звідкись інакше (з файлу, з API, з бази даних), а не тільки через calculate_bmi():
old_bmi_from_database = 27.4
category = bmi_category(old_bmi_from_database)   # ✅ працює!

2. Простіше тестувати — можна перевірити bmi_category() окремо, без потреби рахувати справжній BMI:
assert bmi_category(17.0) == "Underweight"
assert bmi_category(27.0) == "Overweight"

3. Легше змінювати — якщо завтра зміняться межі категорій (наприклад, для педіатричних пацієнтів), правиш тільки bmi_category(), не чіпаючи логіку обчислення.

Правило "Single Responsibility" (одна з основ гарного коду): кожна функція повинна робити рівно одну річ і робити її добре. calculate_bmi() — рахує. bmi_category() — класифікує. Не два в одному.
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №5 — *args!

Напиши:
def calculate_average(*numbers: float) -> float:
    ...

Приклади:
calculate_average(10, 20)
→ 15

calculate_average(10, 20, 30, 40)
→ 25

Якщо аргументів немає — придумай коректну поведінку.
"""


def calculate_average(*numbers: float) -> float:
    """Обчислює середнє арифметичне довільної кількості чисел.

    *numbers — "збирає" будь-яку кількість позиційних аргументів
    в один tuple. Викликач може передати 0, 1, 2, 100 чисел — функція
    прийме будь-яку кількість, не потребуючи змінювати сигнатуру.
    """
    if not numbers:
        # порожній tuple — це falsy, тому `not numbers` == True
        raise ValueError("Неможливо обчислити середнє: аргументи відсутні.")

    return sum(numbers) / len(numbers)


# --- Демонстрація роботи ---
results = []

results.append(("calculate_average(10, 20)", calculate_average(10, 20)))
results.append(("calculate_average(10, 20, 30, 40)", calculate_average(10, 20, 30, 40)))
results.append(("calculate_average(15)", calculate_average(15)))
results.append(
    (
        "calculate_average(36.6, 37.2, 38.1)",
        f"{calculate_average(36.6, 37.2, 38.1):.2f}",
    )
)

# --- Тест порожнього виклику ---
try:
    calculate_average()
except ValueError as e:
    results.append(("calculate_average()", f"❌ ValueError: {e}"))

# --- Вивід у рамці ---
label_width = max(len(label) for label, _ in results)
value_width = max(len(str(v)) for _, v in results)
width = label_width + value_width + 5

print("\n┌" + "─" * width + "┐")
print("│" + "  CALCULATE_AVERAGE()".center(width) + "│")
print("├" + "─" * width + "┤")
for label, value in results:
    print(f"│  {label.ljust(label_width)} │ {str(value).ljust(value_width)} │")
print("└" + "─" * width + "┘")

"""
┌──────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                          CALCULATE_AVERAGE()                                         │
├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
│  calculate_average(10, 20)           │ 15.0                                                           │
│  calculate_average(10, 20, 30, 40)   │ 25.0                                                           │
│  calculate_average(15)               │ 15.0                                                           │
│  calculate_average(36.6, 37.2, 38.1) │ 37.30                                                          │
│  calculate_average()                 │ ❌ ValueError: Неможливо обчислити середнє: аргументи відсутні. │
└──────────────────────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
Пояснення *args (тут — *numbers):
def calculate_average(*numbers):
    print(numbers)   # завжди TUPLE, незалежно від кількості аргументів

calculate_average(10, 20)           # numbers = (10, 20)
calculate_average(10, 20, 30, 40)   # numbers = (10, 20, 30, 40)
calculate_average(15)               # numbers = (15,)
calculate_average()                 # numbers = ()  — порожній tuple

Зірочка * перед іменем параметра каже Python: "збери всі позиційні аргументи, скільки б їх не було, в один tuple з цим іменем". 
Це називається variadic function (функція зі змінною кількістю аргументів).

Чому not numbers перевіряє порожній tuple:
# Порожній tuple — falsy (як порожній список чи рядок, з Challenge №2):
not ()          # → True   (порожній tuple — falsy)
not (10, 20)    # → False  (непорожній — truthy)

if not numbers:   # те саме що: if len(numbers) == 0:
    raise ValueError(...)

Чому ValueError, а не 0.0 при порожньому виклику:
# ❌ Тихо повернути 0.0 — приховує помилку:
def calculate_average(*numbers):
    if not numbers:
        return 0.0   # виглядає як "середнє нуля елементів = 0",
                      # але математично середнє ПОРОЖНЬОЇ множини НЕ ІСНУЄ

result = calculate_average()   # 0.0 — виглядає як валідний результат!
if result < 10:                 # цей код і не здогадається, що щось не так
    print("Низьке середнє")     # ХИБНИЙ висновок — даних не було взагалі

# ✅ ValueError — явно сигналізує "тут немає що рахувати":
result = calculate_average()   # 💥 одразу видно проблему

Це узгоджується з тим самим принципом, що й у divide() з Практики №2: явна помилка краща за тиху хибну відповідь.

Різниця з попередньою задачею (add, subtract...):

	                    add(a, b)	            calculate_average(*numbers)
Кількість аргументів	рівно 2, фіксовано	    будь-яка, від 0 до безлічі
Виклик	                add(10, 20)	            calculate_average(10, 20, 30, ...)
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №6 — **kwargs!

Створи:
def create_patient_report(**patient_data):
    ...

Наприклад:
create_patient_report(
    name="Ivan",
    age=42,
    diagnosis="Sinusitis",
)

Функція повинна сформувати читабельний текстовий звіт.
"""

REQUIRED_FIELDS = ("name", "age", "diagnosis")


def create_patient_report(**patient_data) -> str:
    """Формує текстовий звіт з довільних іменованих даних пацієнта.

    **patient_data — "збирає" будь-яку кількість іменованих аргументів
    в один dict. Так функція приймає гнучкий набір полів, не потребуючи
    заздалегідь знати їх усі (KISS: не пишемо окремий параметр
    для кожного можливого поля).

    Функція лише ПОВЕРТАЄ рядок (return), а не друкує — рішення,
    що робити зі звітом (print, зберегти у файл, надіслати) —
    залишається за викликачем (той самий принцип, що й у greet()).
    """
    # Валідація обов'язкових полів
    missing = [field for field in REQUIRED_FIELDS if field not in patient_data]
    if missing:
        raise ValueError(f"Відсутні обов'язкові поля: {', '.join(missing)}")

    # Формуємо звіт: обов'язкові поля — першими, у фіксованому порядку
    lines = [
        f"{field.capitalize()}: {patient_data[field]}" for field in REQUIRED_FIELDS
    ]

    # Усі ІНШІ поля (яких немає в REQUIRED_FIELDS) — додаємо після,
    # у тому порядку, в якому їх передали
    extra_fields = {k: v for k, v in patient_data.items() if k not in REQUIRED_FIELDS}
    for key, value in extra_fields.items():
        lines.append(f"{key.capitalize()}: {value}")

    return "\n".join(lines)


# --- Приклад використання ---
report = create_patient_report(
    name="Ivan",
    age=42,
    diagnosis="Sinusitis",
)

# --- Приклад із додатковими полями (гнучкість **kwargs) ---
report_extended = create_patient_report(
    name="Olena",
    age=35,
    diagnosis="Fever",
    temperature=38.2,
    ward="ЛОР-відділення",
)


# --- Вивід у рамці (окремо від логіки формування звіту) ---
def print_framed(title: str, text: str) -> None:
    lines = text.split("\n")
    width = max(len(title), max(len(line) for line in lines)) + 4

    print("\n┌" + "─" * width + "┐")
    print("│" + f"  {title}".center(width) + "│")
    print("├" + "─" * width + "┤")
    for line in lines:
        print("│  " + line.ljust(width - 2) + "│")
    print("└" + "─" * width + "┘")


print_framed("PATIENT REPORT", report)
print_framed("PATIENT REPORT (extended)", report_extended)

# --- Тест валідації ---
try:
    create_patient_report(name="Petro")  # відсутні age та diagnosis
except ValueError as e:
    print(f"\n❌ ValueError: {e}")

"""
┌────────────────────────┐
│      PATIENT REPORT    │
├────────────────────────┤
│  Name: Ivan            │
│  Age: 42               │
│  Diagnosis: Sinusitis  │
└────────────────────────┘

┌─────────────────────────────┐
│   PATIENT REPORT (extended) │
├─────────────────────────────┤
│  Name: Olena                │
│  Age: 35                    │
│  Diagnosis: Fever           │
│  Temperature: 38.2          │
│  Ward: ЛОР-відділення       │
└─────────────────────────────┘

❌ ValueError: Відсутні обов'язкові поля: age, diagnosis
"""

"""
Пояснення **kwargs (тут — **patient_data):

def create_patient_report(**patient_data):
    print(patient_data)   # завжди DICT, ключі — імена аргументів

create_patient_report(name="Ivan", age=42)
# patient_data = {"name": "Ivan", "age": 42}

Подвійна зірочка ** каже Python: "збери всі іменовані аргументи (ключ=значення) в один словник з цим іменем". Це відрізняється від *args з минулої задачі — там збирались позиційні аргументи в tuple, тут — іменовані аргументи в dict.

Порівняння *args vs **kwargs:

	                *args	                        **kwargs
Приймає	            func(10, 20, 30)	            func(a=10, b=20)
Зберігає в	        tuple	                        dict
Доступ	            за позицією	                    за ключем (іменем)
Приклад з минулого	calculate_average(*numbers)	    create_patient_report(**patient_data)

Чому саме **kwargs тут доречний (а не звичайні параметри):

# ❌ Негнучко — фіксований набір параметрів:
def create_patient_report(name, age, diagnosis, temperature=None, ward=None, ...):
    # що робити, коли завтра з'явиться ще одне поле? Змінювати сигнатуру щоразу

# ✅ Гнучко — **kwargs приймає будь-який набір полів:
def create_patient_report(**patient_data):
    # temperature, ward, allergies — що завгодно можна передати,
    # не змінюючи саму функцію

Валідація обов'язкових полів:

REQUIRED_FIELDS = ("name", "age", "diagnosis")
missing = [f for f in REQUIRED_FIELDS if f not in patient_data]
#                                          ↑
#              `in` для dict перевіряє наявність КЛЮЧА
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №7 — keyword-only!

Створи:
def create_measurement(
    patient_name: str,
    *,
    weight: float,
    height: float,
):
    ...

Правильний виклик:
create_measurement(
    "Ivan",
    weight=82,
    height=180,
)

Спробуй пояснити, навіщо тут *.
"""


def create_measurement(
    patient_name: str,
    *,
    weight: float,
    height: float,
) -> dict:
    """Створює запис вимірювання пацієнта.

    patient_name — звичайний параметр, можна передати позиційно.
    Зірочка `*` після нього означає: усе, що йде ПІСЛЯ —
    можна передати ТІЛЬКИ за іменем (keyword-only), не позиційно.
    """
    return {
        "patient_name": patient_name,
        "weight": weight,
        "height": height,
    }


# --- Правильний виклик ---
measurement = create_measurement(
    "Ivan",
    weight=82,
    height=180,
)
print(measurement)
# {'patient_name': 'Ivan', 'weight': 82, 'height': 180}


# --- Спроба виклику БЕЗ імен (позиційно) — наочна помилка ---
try:
    create_measurement("Ivan", 82, 180)  # weight і height передані позиційно
except TypeError as e:
    print(f"\n❌ TypeError: {e}")

"""
{'patient_name': 'Ivan', 'weight': 82, 'height': 180}

❌ TypeError: create_measurement() takes 1 positional argument but 3 were given
"""

"""
Навіщо тут *:
Зірочка * у сигнатурі функції — це не параметр, а розділювач. 
Все, що стоїть до неї, можна передавати як завгодно (позиційно або за іменем). 
Все, що після — тільки за іменем:

def create_measurement(patient_name, *, weight, height):
#                       ↑            ↑      ↑      ↑
#                  звичайний    розділювач  keyword-only параметри

Головна причина використовувати * — захист від помилок через переплутаний порядок:

# ❌ БЕЗ * — легко переплутати порядок аргументів:
def create_measurement(patient_name, weight, height):
    ...

create_measurement("Ivan", 180, 82)   # 💥 весь код виконається БЕЗ помилки,
                                        # але weight=180, height=82 — ПЕРЕПЛУТАНО!
                                        # Python не має способу це помітити

# ✅ З * — переплутати НЕМОЖЛИВО:
def create_measurement(patient_name, *, weight, height):
    ...

create_measurement("Ivan", weight=82, height=180)   # ✅ явно, однозначно
create_measurement("Ivan", height=180, weight=82)   # ✅ теж працює — порядок keyword-only не важливий!
create_measurement("Ivan", 82, 180)                 # 💥 TypeError — Python ОДРАЗУ каже "так не можна"

Чому це особливо важливо саме для медичних даних:

Вага (82) і зріст (180) — обидва просто числа (float/int). Якщо їх передати позиційно і випадково переплутати місцями, код виконається без жодної помилки, але дані будуть невірні — а це вже небезпечно в медичному контексті (неправильний BMI, неправильні висновки). * перетворює потенційну тиху помилку в даних на явну помилку синтаксису, яку побачиш одразу при запуску, а не десь пізніше при аналізі результатів.

Порівняння з попередніми задачами:

Синтаксис	    Що робить	                            Приклад із курсу
def f(a, b)	    звичайні параметри — позиційно або за іменем	add(a, b)
def f(*args)	збирає позиційні аргументи в tuple	    calculate_average(*numbers)
def f(**kwargs)	збирає іменовані аргументи в dict	    create_patient_report(**patient_data)
def f(a, *, b)	a — будь-як, b — тільки за іменем	    create_measurement(name, *, weight, height)
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №8 — функція як аргумент!

Створи:

def apply_operation(
    value: float,
    operation,
) -> float:
    ...

і функції:

def double(x):
    return x * 2


def square(x):
    return x ** 2

Потім:

apply_operation(5, double)
apply_operation(5, square)
"""

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

"""
┌───────────────────────────────────────────────────┐
│                 ФУНКЦІЯ ЯК АРГУМЕНТ               │
├───────────────────────────────────────────────────┤
│  apply_operation(5, double)                 │ 10   │
│  apply_operation(5, square)                 │ 25   │
│  apply_operation(37, celsius_to_fahrenheit) │ 98.6 │
│  apply_operation(10, lambda x: x + 100)     │ 110  │
└───────────────────────────────────────────────────┘
"""

"""
Головна ідея — функції в Python "як звичайні дані":

apply_operation(5, double)   # ← передаємо double БЕЗ дужок ()
#                    ↑
#              це саме функція-об'єкт, а НЕ виклик функції

apply_operation(5, double())    # ❌ так НЕ треба — double() виконався б
                                 # ще ДО передачі, і apply_operation отримав
                                 # би вже готове число, а не функцію

Що відбувається всередині крок за кроком:

apply_operation(5, double)
# 1. value = 5
# 2. operation = double  (сама функція, ще НЕ викликана)
# 3. return operation(value)  →  return double(5)  →  return 10

Функції в Python — це об'єкти першого класу (first-class citizens): їх можна передавати як аргументи, зберігати в змінних, повертати з інших функцій — так само, як числа чи рядки.

lambda — коротка "анонімна" функція:
# Звичайна функція:
def add_hundred(x):
    return x + 100

# Те саме через lambda — коротший запис для простих однорядкових функцій:
add_hundred = lambda x: x + 100
#              ↑        ↑
#          аргумент    що повернути (без слова return!)

apply_operation(10, lambda x: x + 100)   # можна писати "на льоту", без імені

Практична цінність цього патерну:
# Уяви медичний конвеєр обробки вимірювань:
readings = [36.6, 37.2, 38.1]

celsius_readings = [apply_operation(t, lambda x: x) for t in readings]
fahrenheit_readings = [apply_operation(t, celsius_to_fahrenheit) for t in readings]

# apply_operation НЕ ЗМІНЮЄТЬСЯ — просто підставляємо іншу функцію,
# і поведінка повністю інша. Це основа патерну "стратегія" (Strategy pattern)
"""
