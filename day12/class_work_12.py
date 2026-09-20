"""
# !Task 1 — перший клас!

Створи:
class Patient:
    pass

та створіть три екземпляри:
Ivan
Olena
Petro

Покажи, що це різні об'єкти.
"""

class Patient:
    pass   # порожній клас — без атрибутів, без методів, лише "форма" для об'єктів


# --- Створюємо ТРИ окремих екземпляри ---
patient1 = Patient()
patient2 = Patient()
patient3 = Patient()

# --- Додаємо ім'я КОЖНОМУ екземпляру ОКРЕМО (клас сам не має __init__) ---
patient1.name = "Ivan"
patient2.name = "Olena"
patient3.name = "Petro"

# --- Доказ, що це РІЗНІ об'єкти ---
lines = [
    f"patient1.name = {patient1.name}, id = {id(patient1)}",
    f"patient2.name = {patient2.name}, id = {id(patient2)}",
    f"patient3.name = {patient3.name}, id = {id(patient3)}",
    "─" * 40,
    f"patient1 is patient2: {patient1 is patient2}",
    f"patient1 is patient3: {patient1 is patient3}",
    f"patient2 is patient3: {patient2 is patient3}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ТРИ ЕКЗЕМПЛЯРИ PATIENT".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────────────────────────┐
│             ТРИ ЕКЗЕМПЛЯРИ PATIENT          │
├─────────────────────────────────────────────┤
│  patient1.name = Ivan, id = 2597695753248   │
│  patient2.name = Olena, id = 2597695785552  │
│  patient3.name = Petro, id = 2597695785872  │
│  ────────────────────────────────────────   │
│  patient1 is patient2: False                │
│  patient1 is patient3: False                │
│  patient2 is patient3: False                │
└─────────────────────────────────────────────┘
"""

"""
*Пояснення class Patient: pass:
class Patient:
    pass   # ← "порожнє тіло" — клас technically існує, але нічого не робить сам по собі

pass тут — це "заглушка": Python вимагає, щоб у тілі класу (чи функції, чи будь-якого блоку з :) було хоч щось, навіть якщо нічого конкретного поки не потрібно. pass буквально означає "нічого не роби, просто пропусти" — синтаксично коректний, семантично порожній рядок коду.

*Чому можна додати patient1.name = "Ivan", хоч у класі немає __init__:
patient1 = Patient()    # створюємо ПОРОЖНІЙ об'єкт (жодних атрибутів)
patient1.name = "Ivan"    # ⬅ Python ДОЗВОЛЯЄ додавати атрибути "на льоту",
                            #   навіть якщо клас їх НЕ передбачав заздалегідь

*Це особливість Python: 
об'єкти за замовчуванням мають внутрішній словник (__dict__), куди можна динамічно додавати нові атрибути після створення об'єкта — на відміну від деяких інших мов, де структура об'єкта фіксована класом.

*Доказ, що patient1, patient2, patient3 — РІЗНІ об'єкти:
patient1 = Patient()   # створює НОВИЙ об'єкт у пам'яті
patient2 = Patient()   # створює ЩЕ ОДИН, ІНШИЙ об'єкт
patient3 = Patient()   # і ЩЕ ОДИН

# КОЖЕН виклик Patient() створює НОВУ, окрему "коробку" у пам'яті —
# навіть якщо всередині вони порожні й "однакові за формою"

id(patient1)   # → якесь число  A
id(patient2)   # → ІНШЕ число   B  (A ≠ B)
id(patient3)   # → ЩЕ ІНШЕ число C

patient1 is patient2   # → False — це РІЗНІ об'єкти

*Зв'язок із Практикою №2 (день "базові типи") — той самий id():
Це та сама ідея, що вже застосовувалась раніше для перевірки int, str, list — кожен виклик конструктора (Patient(), як і [1, 2, 3] чи "текст") створює новий об'єкт у пам'яті. is порівнює саме ідентичність (те, чи це один і той самий об'єкт), а не вміст — навіть якщо два пацієнти мали б однакове ім'я, вони все одно були б різними об'єктами:

patient4 = Patient()
patient4.name = "Ivan"   # ТАКЕ САМЕ ім'я, як у patient1

patient1 is patient4       # → False!  Різні об'єкти, навіть з однаковим "name"
patient1.name == patient4.name   # → True   (значення атрибута ОДНАКОВЕ,
                                    #           але це НЕ робить об'єкти "тим самим")

Це — суть об'єктно-орієнтованого програмування, що починається саме тут: клас — це "шаблон" чи "форма", а кожен екземпляр (об'єкт) — це окрема, незалежна сутність, навіть якщо всі вони створені з одного й того самого класу.
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 2 — __init__!

Розшир:
class Patient:
    def __init__(self, name: str, age: int):
        ...

Збережи:
name
age

Створи щонайменше 4 пацієнти.
"""

class Patient:
    def __init__(self, name: str, age: int):
        """Створює пацієнта і зберігає його ім'я та вік.

        assert одразу перевіряє коректність — якщо вік некоректний,
        об'єкт НАВІТЬ НЕ СТВОРИТЬСЯ.
        """
        assert age > 0, f"Вік має бути більшим за 0, отримано: {age}"

        self.name = name   # ← self.ЩОСЬ = зберігає значення В САМОМУ об'єкті
        self.age = age


# --- Створюємо ЩОНАЙМЕНШЕ 4 пацієнти ---
patient1 = Patient("Ivan", 42)
patient2 = Patient("Olena", 35)
patient3 = Patient("Petro", 61)
patient4 = Patient("Hanna", 29)

patients = [patient1, patient2, patient3, patient4]

# --- Вивід у рамці ---
lines = [f"{p.name}, {p.age} років" for p in patients]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  СПИСОК ПАЦІЄНТІВ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

# --- Демонстрація валідації: спроба створити некоректного пацієнта ---
try:
    bad_patient = Patient("Test", -5)
except AssertionError as e:
    print(f"\n❌ AssertionError: {e}")

"""
┌───────────────────┐
│   СПИСОК ПАЦІЄНТІВ│
├───────────────────┤
│  Ivan, 42 років   │
│  Olena, 35 років  │
│  Petro, 61 років  │
│  Hanna, 29 років  │
└───────────────────┘

❌ AssertionError: Вік має бути більшим за 0, отримано: -5
"""

"""
#*Пояснення __init__ — "конструктор" об'єкта:
class Patient:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

__init__ — спеціальний метод, який Python автоматично викликає, щойно ти пишеш Patient("Ivan", 42). Він не створює сам об'єкт (це робить Python "за кулісами" раніше), а лише налаштовує вже створений об'єкт — записує в нього передані значення.

#*Що означає self:
Patient("Ivan", 42)
#        ↑      ↑
#       name    age

def __init__(self, name, age):
#             ↑
#         це і є "ТОЙ САМИЙ" об'єкт, що зараз створюється
#         (Python передає його АВТОМАТИЧНО, ти НЕ пишеш його при виклику)

self — це посилання на конкретний об'єкт, який зараз створюється. Коли викликаєш Patient("Ivan", 42), Python сам підставляє новий об'єкт як self, а "Ivan" і 42 йдуть у name та age.

#*Що робить self.name = name:
self.name = name
#    ↑        ↑
# зберегти  У ЦЕ значення, яке прийшло
# В ОБ'ЄКТІ  як параметр функції

Без self. — name була б лише тимчасовою змінною всередині __init__, яка "зникає", щойно функція завершується. З self.name = name — значення прив'язується до конкретного об'єкта і залишається доступним після завершення __init__, через patient1.name.

#*Кожен об'єкт має СВОЇ ВЛАСНІ name/age — не спільні:
patient1 = Patient("Ivan", 42)
patient2 = Patient("Olena", 35)

patient1.name   # → "Ivan"    (СВІЙ атрибут)
patient2.name    # → "Olena"   (ІНШИЙ, ОКРЕМИЙ атрибут, той самий self, різні об'єкти)

Кожен виклик Patient(...) створює новий об'єкт (як у Task 1), і __init__ записує name/age саме в цей конкретний об'єкт — тому patient1.name і patient2.name — це два різних значення, збережені в двох різних місцях пам'яті.

#*Чому assert age > 0 — усередині __init__, а не окремою функцією (як parse_age з попереднього дня):
class Patient:
    def __init__(self, name, age):
        assert age > 0, f"..."   # ← перевірка ВІДРАЗУ при СТВОРЕННІ об'єкта
        self.name = name
        self.age = age

Це гарантує, що неможливо створити Patient із некоректним віком — об'єкт або створюється валідним, або взагалі не створюється (AssertionError зупиняє виконання до того, як self.age = age встигне спрацювати). Це той самий принцип, що вже застосовувався в MedicalMeasurement.__post_init__() — лише тут перевірка стоїть прямо в __init__, бо клас пишеться "вручну", без @dataclass.
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 3 — метод is_adult!

Додай:
def is_adult(self) -> bool:
    ...

Перевір:
15 → False
18 → True
42 → True
"""

class Patient:
    def __init__(self, name: str, age: int):
        assert age > 0, f"Вік має бути більшим за 0, отримано: {age}"
        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        """Перевіряє, чи пацієнту 18 років чи більше.

        self.age — звертаємось до ВЛАСНОГО атрибута ЦЬОГО об'єкта,
        а не до якогось параметра, переданого ЗОВНІ.
        """
        return self.age >= 18


# --- Перевірка за умовою завдання ---
test_cases = [
    Patient("Sofia", 15),
    Patient("Petro", 18),
    Patient("Ivan", 42),
]

lines = [f"{p.name} ({p.age} років).is_adult()  →  {p.is_adult()}" for p in test_cases]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  IS_ADULT()".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────────────────────┐
│                 IS_ADULT()              │
├─────────────────────────────────────────┤
│  Sofia (15 років).is_adult()  →  False  │
│  Petro (18 років).is_adult()  →  True   │
│  Ivan (42 років).is_adult()  →  True    │
└─────────────────────────────────────────┘
"""

"""
#*Пояснення методу is_adult(self):
def is_adult(self) -> bool:
    return self.age >= 18

#*Головна різниця між методом (як is_adult) і звичайною функцією (як is_adult(age) з попередніх днів):
# Звичайна функція (день 10, patient_utils.py) — приймає ДАНІ ЗОВНІ:
def is_adult(age: int) -> bool:
    return age >= 18

is_adult(42)   # ← явно ПЕРЕДАЄШ вік як аргумент

# Метод класу — БЕРЕ ДАНІ З self, нічого не треба передавати ззовні:
class Patient:
    def is_adult(self) -> bool:
        return self.age >= 18   # ← `self.age` вже ВСЕРЕДИНІ об'єкта

patient1.is_adult()   # ← НЕ треба передавати вік — метод сам знає
                         #   свій self.age, бо викликається НА ОБ'ЄКТІ

#*Як self "автоматично" підставляється при викликах методів:
patient1 = Patient("Ivan", 42)
patient1.is_adult()
#    ↑
# коли пишеш patient1.is_adult(), Python РОЗУМІЄ це як:
# Patient.is_adult(patient1)
#                    ↑
#              self = ЦЕЙ КОНКРЕТНИЙ patient1

# тому self.age всередині методу — це РІВНО те саме, що patient1.age ЗОВНІ

#*Чому це зручніше за окрему функцію — інкапсуляція логіки РАЗОМ із даними:
# Об'єкт "знає, як" відповідати на запитання ПРО СЕБЕ:
patient1.is_adult()      # ← "чи Я (цей конкретний пацієнт) повнолітній?"
patient2.is_adult()       # ← "а Я?"
patient3.is_adult()        # ← кожен об'єкт відповідає, використовуючи ВЛАСНІ дані

# Немає потреби ПАМ'ЯТАТИ й ПЕРЕДАВАТИ окремо patient1.age, patient2.age...
# Логіка "приліплена" безпосередньо до об'єкта, якому вона стосується

#*Перевірка по всіх трьох тестових випадках із завдання:
Patient("Sofia", 15).is_adult()   # self.age=15 → 15 >= 18? Ні → False   ✅
Patient("Petro", 18).is_adult()    # self.age=18 → 18 >= 18? Так → True    ✅ (межовий випадок!)
Patient("Ivan", 42).is_adult()      # self.age=42 → 42 >= 18? Так → True     ✅

Зверни увагу на межовий випадок 18 — тест навмисно включає саме порогове значення, щоб переконатись, що метод коректно використовує >= (включно), а не > (виключно), — той самий принцип "тестування меж", що вже застосовувався для is_adult() в patient_utils.py дня 10.
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 4 — BMI method!

Додай:
def calculate_bmi(
    self,
    weight: float,
    height: float,
) -> float:
    ...

Формула:
BMI = weight / height²

height — у метрах.
"""

class Patient:
    def __init__(self, name: str, age: int):
        assert age > 0, f"Вік має бути більшим за 0, отримано: {age}"
        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        return self.age >= 18

    def calculate_bmi(self, weight: float, height: float) -> float:
        """Обчислює BMI для ЦЬОГО пацієнта на основі переданих ваги/зросту.

        Формула: BMI = weight / height² (height у МЕТРАХ).
        Зверни увагу: weight/height НЕ зберігаються в self —
        це лише ТИМЧАСОВІ параметри для одноразового розрахунку.
        """
        assert weight > 0, f"weight має бути більше 0, отримано: {weight}"
        assert height > 0, f"height має бути більше 0, отримано: {height}"

        return weight / (height ** 2)


# --- Демонстрація ---
patients = [
    Patient("Ivan", 42),
    Patient("Olena", 35),
    Patient("Petro", 61),
]

measurements = [(82, 1.80), (55, 1.65), (95, 1.75)]

lines = []
for patient, (weight, height) in zip(patients, measurements):
    bmi = patient.calculate_bmi(weight, height)
    lines.append(f"{patient.name}.calculate_bmi({weight}, {height})  →  BMI {bmi:.1f}")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  CALCULATE_BMI()".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

# --- Демонстрація валідації ---
try:
    patients[0].calculate_bmi(-10, 1.80)
except AssertionError as e:
    print(f"\n❌ AssertionError: {e}")

"""
┌──────────────────────────────────────────────┐
│                CALCULATE_BMI()               │
├──────────────────────────────────────────────┤
│  Ivan.calculate_bmi(82, 1.8)  →  BMI 25.3    │
│  Olena.calculate_bmi(55, 1.65)  →  BMI 20.2  │
│  Petro.calculate_bmi(95, 1.75)  →  BMI 31.0  │
└──────────────────────────────────────────────┘

❌ AssertionError: weight має бути більше 0, отримано: -10
"""

"""
#*Ключова відмінність цього методу від is_adult() — параметри, а не лише self:
def is_adult(self) -> bool:
    return self.age >= 18                    # ← ЛИШЕ self, дані вже "всередині" об'єкта

def calculate_bmi(self, weight: float, height: float) -> float:
    return weight / (height ** 2)             # ← self ПЛЮС ДВА додаткових параметри,
                                                 #   передані ЗОВНІ при кожному викликові

#*Чому weight/height — параметри методу, а НЕ атрибути self:
patient1.calculate_bmi(82, 1.80)   # weight=82, height=1.80 — передаються ТУТ, щоразу

# self.weight / self.height НЕ ІСНУЮТЬ — Patient НЕ "пам'ятає" вагу/зріст постійно

Це навмисний дизайн, узгоджений із сигнатурою завдання: вага і зріст пацієнта можуть змінюватись при кожному візиті (сьогодні 82 кг, за місяць — 80 кг), тому логічніше передавати їх щоразу, коли потрібен розрахунок, а не "заморожувати" їх у момент створення об'єкта.

#*Порівняння з "альтернативним" дизайном (для розуміння, чому саме так):
# ❌ Якби weight/height БУЛИ в __init__ — вони "застигли" б назавжди:
class Patient:
    def __init__(self, name, age, weight, height):
        self.weight = weight
        self.height = height

    def calculate_bmi(self):        # без параметрів — читає self.weight/self.height
        return self.weight / (self.height ** 2)

patient1 = Patient("Ivan", 42, 82, 1.80)
patient1.calculate_bmi()             # завжди РАХУЄ для ОДНАКОВИХ 82/1.80

# Щоб перерахувати для НОВОЇ ваги, треба було б ЗМІНЮВАТИ атрибут:
patient1.weight = 80                  # оновлення "стану" об'єкта
patient1.calculate_bmi()               # тепер рахує для 80

# ✅ Наш підхід (за умовою завдання) — гнучкіше, БЕЗ потреби змінювати self:
patient1.calculate_bmi(82, 1.80)        # розрахунок ДЛЯ ЦИХ конкретних значень
patient1.calculate_bmi(80, 1.80)         # ІНШИЙ розрахунок, той самий пацієнт,
                                            # БЕЗ жодної зміни об'єкта patient1

#*self тут все одно потрібен — навіть якщо метод НЕ використовує self.щось у формулі:
def calculate_bmi(self, weight, height):
    return weight / (height ** 2)   # ← НАВІТЬ не звертається до self.name чи self.age!

Здавалось би, self тут "непотрібен" (формула не використовує self.age), але Python вимагає self першим параметром у будь-якому методі класу — це синтаксична умова того, щоб цю функцію можна було викликати як patient1.calculate_bmi(...), а не просто calculate_bmi(...). Без self метод перетворився б на звичайну функцію всередині класу, недоступну через patient1.calculate_bmi(...).
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 5 — validation!

Твій клас повинен не дозволяти створити очевидно некоректного пацієнта:
Patient("", 42)
Patient("Ivan", -5)

При невалідних значеннях:
raise ValueError(...)

Тут використай знання Дня 11.
"""

class Patient:
    def __init__(self, name: str, age: int):
        """Створює пацієнта з валідацією — зберігає ВСІ помилки одразу.

        Той самий collect-all підхід, що й у validate_patient() з Дня 11:
        перевіряємо ОБИДВА поля (name і age), НЕЗАЛЕЖНО від того, чи
        перше вже було невалідним, і піднімаємо ОДНЕ ValueError
        з повним списком проблем — а не зупиняємось на першій-ліпшій.

        Raises:
            ValueError: Якщо name порожнє АБО age <= 0 (чи ОБИДВА разом).
        """
        errors = []

        if not name or not name.strip():
            errors.append(f"name не може бути порожнім, отримано: {name!r}")

        if age <= 0:
            errors.append(f"age має бути більшим за 0, отримано: {age}")

        if errors:
            raise ValueError("Некоректні дані пацієнта: " + "; ".join(errors))

        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        return self.age >= 18

    def calculate_bmi(self, weight: float, height: float) -> float:
        assert weight > 0, f"weight має бути більше 0, отримано: {weight}"
        assert height > 0, f"height має бути більше 0, отримано: {height}"
        return weight / (height ** 2)


# --- Демонстрація ---
test_cases = [
    ("Ivan", 42),      # ✅ валідний
    ("", 42),           # ❌ порожнє ім'я
    ("Ivan", -5),        # ❌ невірний вік
    ("", -5),             # ❌❌ ОБИДВІ помилки одразу
]

results = []
for name, age in test_cases:
    try:
        patient = Patient(name, age)
        results.append((f"Patient({name!r}, {age})", f"✅ Створено: {patient.name}, {patient.age}"))
    except ValueError as e:
        results.append((f"Patient({name!r}, {age})", f"❌ {e}"))

# --- Вивід у рамці ---
lines = [f"{call}  →  {result}" for call, result in results]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ВАЛІДАЦІЯ PATIENT".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                           ВАЛІДАЦІЯ PATIENT                      │
│  Patient('Ivan', 42)  →  ✅ Створено: Ivan, 42                                                   │
│  Patient('', 42)  →  ❌ Некоректні дані пацієнта: name не може бути порожнім, отримано: ''       │
│  Patient('Ivan', -5)  →  ❌ Некоректні дані пацієнта: age має бути більшим за 0, отримано: -5    │
│  Patient('', -5)  →  ❌ Некоректні дані пацієнта: name не може бути порожнім, отримано: '';      │
│                           age має бути більшим за 0, отримано: -5                                │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
#*Ключова зміна порівняно з Task 2 (assert) — чому саме ValueError, а не assert:
# Task 2 (assert) — просте, але з ОБМЕЖЕННЯМ:
assert age > 0, f"..."
# ⚠️ assert МОЖНА вимкнути прапорцем python -O — тоді ВСЯ перевірка
#    просто ЗНИКАЄ, і об'єкт створиться навіть із некоректними даними!

# Task 5 (ValueError) — надійніше для "публічного" класу:
if age <= 0:
    errors.append(...)
raise ValueError(...)
# ✅ ЗАВЖДИ активне, незалежно від прапорців запуску Python

Це той самий висновок, що вже обговорювався в Практиці №2 попереднього дня ("Практика №2 — математичні функції") — assert годиться для внутрішньої логіки й навчальних прикладів, а raise ValueError — надійніший вибір для класу, що інші розробники будуть активно використовувати (як Patient у MedAssistant).

#*Пояснення collect-all у __init__ — точно той самий патерн, що в validate_patient():
errors = []                              # ① починаємо з ПОРОЖНЬОГО списку

if not name or not name.strip():           # ② перевіряємо name
    errors.append("...")                     #    якщо погано — ДОДАЄМО, НЕ зупиняємось

if age <= 0:                                # ③ ПРОДОВЖУЄМО перевіряти age,
    errors.append("...")                      #    незалежно від результату name

if errors:                                   # ④ ТІЛЬКИ НАПРИКІНЦІ — якщо щось назбиралось —
    raise ValueError(...)                       #    ОДНЕ повідомлення з УСІМ одразу

#*Демонстрація різниці для Patient("", -5) — ОБИДВІ помилки видно одразу:
Patient("", -5)
# name="" → not name → True → errors.append("name не може бути порожнім...")
# age=-5 → -5 <= 0 → True → errors.append("age має бути більшим за 0...")
# errors = ["name не може бути порожнім...", "age має бути більшим за 0..."]

# 💥 ValueError: Некоректні дані пацієнта:
#    name не може бути порожнім, отримано: ''; age має бути більшим за 0, отримано: -5

Якби перевірка зупинялась на першій помилці (fail-fast), ти побачив би лише проблему з name, і довелось би виправити її, запустити знову, щоб дізнатись про проблему з age — collect-all показує обидві проблеми за один запуск, точно як обговорювалось у Day 11 Challenge 3.

#*Чому важливо, що валідація стоїть у __init__ ПЕРЕД self.name = name:
if errors:
    raise ValueError(...)     # ← якщо ТУТ виникає помилка —

self.name = name                # ← ЦІ рядки НІКОЛИ не виконаються
self.age = age

#*Це гарантує: 
об'єкт Patient або створюється повністю валідним, або не створюється взагалі — ніколи не існує "напівготового" Patient із порожнім name, який хтось міг би випадково почати використовувати.
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 6 — __repr__!

Додай:
def __repr__(self) -> str:
    ...

Очікуваний стиль:
Patient(name='Ivan', age=42)
"""

class Patient:
    def __init__(self, name: str, age: int):
        errors = []

        if not name or not name.strip():
            errors.append(f"name не може бути порожнім, отримано: {name!r}")
        if age <= 0:
            errors.append(f"age має бути більшим за 0, отримано: {age}")

        if errors:
            raise ValueError("Некоректні дані пацієнта: " + "; ".join(errors))

        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        return self.age >= 18

    def calculate_bmi(self, weight: float, height: float) -> float:
        assert weight > 0, f"weight має бути більше 0, отримано: {weight}"
        assert height > 0, f"height має бути більше 0, отримано: {height}"
        return weight / (height ** 2)

    def __repr__(self) -> str:
        """Технічне представлення об'єкта — для розробника, для debug/консолі."""
        return f"Patient(name={self.name!r}, age={self.age})"


# --- Демонстрація ---
patients = [
    Patient("Ivan", 42),
    Patient("Olena", 35),
    Patient("Petro", 61),
]

lines = [
    f"repr(patient1) = {patients[0]!r}",
    f"print(patient1) = {patients[0]}",       # print() теж використовує __repr__, якщо немає __str__
    f"patients = {patients}",                    # list автоматично викликає __repr__ для КОЖНОГО елемента
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  __REPR__()".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                  __REPR__()                                               │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│  repr(patient1) = Patient(name='Ivan', age=42)                                                            │
│  print(patient1) = Patient(name='Ivan', age=42)                                                           │
│  patients = [Patient(name='Ivan', age=42), Patient(name='Olena', age=35), Patient(name='Petro', age=61)]  │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
#*Пояснення __repr__ — навіщо цей метод і що він робить:
patient1 = Patient("Ivan", 42)
print(patient1)

БЕЗ __repr__ цей print() вивів би щось незрозуміле, на кшталт:

<__main__.Patient object at 0x7f3a2c1d5f90>

Це "стандартне" представлення Python — просто адреса об'єкта в пам'яті (той самий id(), що вже неодноразово зустрічався), без жодної корисної інформації про вміст об'єкта.

#*З __repr__ — Python "запитує" у самого об'єкта, ЯК себе показати:
def __repr__(self) -> str:
    return f"Patient(name={self.name!r}, age={self.age})"

Коли Python потребує текстове представлення об'єкта (для print(), для показу в консолі, для елемента list), він автоматично викликає __repr__() на цьому об'єкті — і використовує те, що ти сам визначив, замість "сирої" адреси пам'яті.

#*Чому саме такий формат — Patient(name='Ivan', age=42):
f"Patient(name={self.name!r}, age={self.age})"
#                       ↑
#                    !r = repr() значення (з ЛАПКАМИ навколо рядка)

self.name!r    # "Ivan" → 'Ivan'   (з лапками — видно, що це РЯДОК)
self.age       # 42 → 42            (без !r — число без лапок)

Це навмисно написано у форматі, схожому на виклик конструктора — так, ніби можна скопіювати цей рядок і буквально створити такий самий об'єкт знову: Patient(name='Ivan', age=42). Це — офіційна рекомендація Python для __repr__: результат має бути однозначним і, за можливості, придатним для відтворення об'єкта.

#*Чому !r, а не просто {self.name}:
f"Patient(name={self.name}, age={self.age})"     # ← БЕЗ !r
# → "Patient(name=Ivan, age=42)"    ← Ivan БЕЗ лапок — виглядає, ніби це якась ЗМІННА,
#                                       а не рядкове ЗНАЧЕННЯ

f"Patient(name={self.name!r}, age={self.age})"    # ← З !r
# → "Patient(name='Ivan', age=42)"   ← ОЧЕВИДНО, що 'Ivan' — це РЯДОК (з лапками)

#*__repr__ спрацьовує автоматично в кількох контекстах:
print(patient1)         # print() шукає __str__; якщо його НЕМАЄ — використовує __repr__
repr(patient1)            # напряму викликає __repr__
patients_list = [patient1, patient2]
print(patients_list)       # ← list ЗАВЖДИ показує елементи через __repr__ КОЖНОГО,
                             #    НЕЗАЛЕЖНО від того, чи є __str__

#*Зв'язок із попередніми днями: 
цей самий принцип уже застосовувався у MedicalMeasurement.__str__() (день "MedAssistant модуль") — там __str__ давав людське, коротке представлення ("Ivan: BMI 25.4"), а __repr__ — саме технічне, орієнтоване на розробника й на можливість "відтворити" об'єкт. 
Якщо в класі є лише __repr__ (без окремого __str__, як тут) — Python використовує __repr__ скрізь, де потрібне текстове представлення об'єкта.
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 7 — клас і список!

Створи:
patients: list[Patient]
з п'яти пацієнтів.

За допомогою methods класу:
- порахуй кількість дорослих;
- знайди середній вік;
- виведи BMI кількох пацієнтів.
"""

class Patient:
    def __init__(self, name: str, age: int):
        errors = []

        if not name or not name.strip():
            errors.append(f"name не може бути порожнім, отримано: {name!r}")
        if age <= 0:
            errors.append(f"age має бути більшим за 0, отримано: {age}")

        if errors:
            raise ValueError("Некоректні дані пацієнта: " + "; ".join(errors))

        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        return self.age >= 18

    def calculate_bmi(self, weight: float, height: float) -> float:
        assert weight > 0, f"weight має бути більше 0, отримано: {weight}"
        assert height > 0, f"height має бути більше 0, отримано: {height}"
        return weight / (height ** 2)

    def __repr__(self) -> str:
        return f"Patient(name={self.name!r}, age={self.age})"


# --- Список із п'яти пацієнтів ---
patients: list[Patient] = [
    Patient("Ivan", 42),
    Patient("Olena", 35),
    Patient("Petro", 61),
    Patient("Sofia", 15),
    Patient("Mykola", 8),
]

# --- Виміри для BMI (weight у кг, height у метрах) — окремо від Patient ---
measurements = {
    "Ivan": (82, 1.80),
    "Olena": (58, 1.65),
    "Petro": (95, 1.72),
    "Sofia": (52, 1.60),
    "Mykola": (28, 1.30),
}

# --- 1. Кількість дорослих — використовуємо is_adult() кожного пацієнта ---
adult_count = sum(1 for p in patients if p.is_adult())

# --- 2. Середній вік — використовуємо p.age кожного пацієнта ---
average_age = sum(p.age for p in patients) / len(patients)

# --- 3. BMI кожного пацієнта — використовуємо calculate_bmi() ---
bmi_results = [
    (p.name, p.calculate_bmi(*measurements[p.name]))
    for p in patients
]

# --- Вивід у рамці ---
lines = ["Список пацієнтів:"]
lines += [f"  {p!r}" for p in patients]
lines.append("─" * 50)
lines.append(f"Кількість дорослих: {adult_count} з {len(patients)}")
lines.append(f"Середній вік: {average_age:.1f} років")
lines.append("─" * 50)
lines.append("BMI пацієнтів:")
for name, bmi in bmi_results:
    lines.append(f"  {name}: BMI {bmi:.1f}")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  СПИСОК ПАЦІЄНТІВ ТА СТАТИСТИКА".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌──────────────────────────────────────────────────────┐
│             СПИСОК ПАЦІЄНТІВ ТА СТАТИСТИКА           │
├──────────────────────────────────────────────────────┤
│  Список пацієнтів:                                   │
│    Patient(name='Ivan', age=42)                      │
│    Patient(name='Olena', age=35)                     │
│    Patient(name='Petro', age=61)                     │
│    Patient(name='Sofia', age=15)                     │
│    Patient(name='Mykola', age=8)                     │
│  ──────────────────────────────────────────────────  │
│  Кількість дорослих: 3 з 5                           │
│  Середній вік: 32.2 років                            │
│  ──────────────────────────────────────────────────  │
│  BMI пацієнтів:                                      │
│    Ivan: BMI 25.3                                    │
│    Olena: BMI 21.3                                   │
│    Petro: BMI 32.1                                   │
│    Sofia: BMI 20.3                                   │
│    Mykola: BMI 16.6                                  │
└──────────────────────────────────────────────────────┘
"""

"""
Це принципова відмінність від list[dict], з яким працювалось у Дні 9-11 (patient_utils.py, statistics_utils.py). Там доступ був через ключі: patient["age"]. Тут — через атрибути: patient.age. І, що найважливіше, кожен елемент має власну поведінку (методи is_adult(), calculate_bmi()), а не лише дані.

#*Кількість дорослих — виклик методу для КОЖНОГО об'єкта в списку:
adult_count = sum(1 for p in patients if p.is_adult())
#                                          ↑
#                              для КОЖНОГО пацієнта окремо ВИКЛИКАЄМО
#                              його ВЛАСНИЙ метод is_adult()

# Розгорнуто, крок за кроком:
# p=Ivan(42)   → p.is_adult() → True   → рахуємо 1
# p=Olena(35)   → p.is_adult() → True    → рахуємо 1
# p=Petro(61)    → p.is_adult() → True     → рахуємо 1
# p=Sofia(15)     → p.is_adult() → False     → НЕ рахуємо
# p=Mykola(8)      → p.is_adult() → False      → НЕ рахуємо
# sum([1,1,1]) = 3

#*Середній вік — доступ до p.age, той самий генераторний вираз, що вже застосовувався в statistics_utils.py:
average_age = sum(p.age for p in patients) / len(patients)
#                  ↑
#         замість p["age"] (як для dict) — ТУТ p.age (атрибут об'єкта)

#*Найцікавіший момент — *measurements[p.name] для передачі weight/height:
p.calculate_bmi(*measurements[p.name])
#                ↑
#           measurements["Ivan"] → (82, 1.80)   ← tuple з ДВОХ значень
#           * розпаковує tuple у ДВА окремих аргументи:
#           p.calculate_bmi(82, 1.80)

# Це РІВНОЦІННО написанню:
weight, height = measurements[p.name]
p.calculate_bmi(weight, height)

Це той самий оператор * (unpacking), що вже застосовувався в дні "модулі" (create_patient_summary(*p)) — тут використаний, щоб уникнути проміжних змінних weight/height і одразу передати розпакований tuple у метод.

#*Чому measurements — окремий словник, а НЕ атрибути Patient:
Це прямий наслідок дизайну з Task 4: calculate_bmi() навмисно приймає weight/height як параметри, а не зберігає їх у self — тому для демонстрації доводиться тримати ці дані зовні, окремо від самих об'єктів Patient, і "зв'язувати" їх через ім'я пацієнта (measurements[p.name]).
"""
