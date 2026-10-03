"""
# !Практика №1 — List!

Створи:
patients = ["Ivan", "Olena", "Petro"]

Виконай:
append("Hanna")
insert(1, "Maria")
remove("Petro")
pop()

Після кожної операції виведи список.
"""

patients = ["Ivan", "Olena", "Petro"]

steps = []
steps.append(("Початковий список", None, list(patients)))

# 1. append() — додає елемент У КІНЕЦЬ списку
patients.append("Hanna")
steps.append(("append('Hanna')", None, list(patients)))

# 2. insert(index, value) — вставляє елемент НА КОНКРЕТНУ позицію,
#    решта елементів зсуваються ПРАВОРУЧ
patients.insert(1, "Maria")
steps.append(("insert(1, 'Maria')", None, list(patients)))

# 3. remove(value) — видаляє ПЕРШЕ входження вказаного ЗНАЧЕННЯ
#    (якщо однакових значень кілька — видалить лише перше)
patients.remove("Petro")
steps.append(("remove('Petro')", None, list(patients)))

# 4. pop() — видаляє й ПОВЕРТАЄ останній елемент
#    (pop(0) видалив би ПЕРШИЙ, за індексом)
removed = patients.pop()
steps.append(("pop()", removed, list(patients)))

# --- Вивід у рамці ---
lines = []
for operation, returned, current_list in steps:
    if operation == "Початковий список":
        lines.append(f"{operation}: {current_list}")
    else:
        if returned is not None:
            lines.append(f"{operation} → повернув: {returned!r}")
        else:
            lines.append(f"{operation}:")
        lines.append(f"  Список: {current_list}")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ОПЕРАЦІЇ ЗІ СПИСКОМ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌──────────────────────────────────────────────────────────┐
│                    ОПЕРАЦІЇ ЗІ СПИСКОМ                   │
├──────────────────────────────────────────────────────────┤
│  Початковий список: ['Ivan', 'Olena', 'Petro']           │
│  append('Hanna'):                                        │
│    Список: ['Ivan', 'Olena', 'Petro', 'Hanna']           │
│  insert(1, 'Maria'):                                     │
│    Список: ['Ivan', 'Maria', 'Olena', 'Petro', 'Hanna']  │
│  remove('Petro'):                                        │
│    Список: ['Ivan', 'Maria', 'Olena', 'Hanna']           │
│  pop() → повернув: 'Hanna'                               │
│    Список: ['Ivan', 'Maria', 'Olena']                    │
└──────────────────────────────────────────────────────────┘
"""

#*Пояснення кожного методу: 
patients = ["Ivan", "Olena", "Petro"]

# 1. append(value) — додає В КІНЕЦЬ, завжди один елемент
patients.append("Hanna")
# → ["Ivan", "Olena", "Petro", "Hanna"]

# 2. insert(index, value) — вставляє НА ПОЗИЦІЮ index,
#    елементи, що були там і далі, зсуваються праворуч
patients.insert(1, "Maria")
#                ↑
#         "Maria" встає на місце індексу 1,
#         "Olena" (був на 1) зсувається на 2, "Petro" на 3, і т.д.
# → ["Ivan", "Maria", "Olena", "Petro", "Hanna"]

# 3. remove(value) — шукає ЗНАЧЕННЯ і видаляє ПЕРШЕ знайдене входження
patients.remove("Petro")
# → ["Ivan", "Maria", "Olena", "Hanna"]
# ⚠️ Якби "Petro" було двічі — видалилось би тільки ПЕРШЕ входження

# 4. pop() — видаляє й ПОВЕРТАЄ останній елемент
removed = patients.pop()
# removed = "Hanna"
# → ["Ivan", "Maria", "Olena"]


"""
*Ключова відмінність remove() vs pop():
	                remove(value)	            pop(index)
Що шукає	        значення (напр. "Petro")	позицію (напр. 0, -1)
Що повертає	        нічого (None)	            видалений елемент
Якщо не знайдено	ValueError	                IndexError (якщо індекс за межами)
pop() без аргументів	—	                    видаляє останній елемент (як тут)

*Важливий нюанс — list(patients) для збереження "знімків":
steps.append(("append('Hanna')", None, list(patients)))
#                                        ↑
#                              КОПІЯ списку на цей момент,
#                              а не посилання на ОРИГІНАЛЬНИЙ patients

Якби я написав просто patients (без list(...)), усі "знімки" в steps вказували б на той самий список у пам'яті — і після всіх операцій усі записи в steps показували б однаковий, фінальний стан списку (бо list — mutable, той самий об'єкт просто змінюється). list(patients) створює новий, незалежний список із поточним вмістом — тому кожен крок зберігає справжній знімок того моменту.
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №2 — Tuple!

Створи:
patient = ("Ivan", 42, 180, 82)

Зроби unpacking:
name
age
height
weight

Після цього виведи всі чотири значення.
"""

patient = ("Ivan", 42, 180, 82)

# --- Unpacking: розпаковуємо tuple у 4 окремі змінні ---
# Кількість змінних ЗЛІВА має ТОЧНО збігатися з кількістю елементів tuple
name, age, height, weight = patient

# --- Вивід у рамці ---
lines = [
    f"name:   {name}",
    f"age:    {age}",
    f"height: {height}",
    f"weight: {weight}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  UNPACKING TUPLE".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

# --- Чому tuple незмінний (immutable) — наочна демонстрація ---
try:
    patient[0] = "Olena"   # спроба змінити перший елемент
except TypeError as e:
    print(f"\n❌ TypeError: {e}")

"""
┌────────────────┐
│  UNPACKING TUPLE│
├────────────────┤
│  name:   Ivan  │
│  age:    42    │
│  height: 180   │
│  weight: 82    │
└────────────────┘

❌ TypeError: 'tuple' object does not support item assignment
"""

"""
*Пояснення unpacking:
patient = ("Ivan", 42, 180, 82)

name, age, height, weight = patient
# ↑     ↑    ↑       ↑        ↑
# name = "Ivan"   (елемент 0)
# age = 42        (елемент 1)
# height = 180    (елемент 2)
# weight = 82     (елемент 3)

Python автоматично зіставляє кожну змінну зліва з елементом tuple на тій самій позиції — за умови, що кількість змінних точно дорівнює кількості елементів:

a, b, c = (1, 2, 3)         # ✅ 3 змінні = 3 елементи, працює
a, b = (1, 2, 3)            # ❌ ValueError: too many values to unpack
a, b, c, d = (1, 2, 3)      # ❌ ValueError: not enough values to unpack

*Чому tuple незмінний — вивід помилки:
❌ TypeError: 'tuple' object does not support item assignment
❌ TypeError: об’єкт «tuple» не підтримує присвоєння елементів

*Пояснення, чому саме так:
patient = ("Ivan", 42, 180, 82)

patient[0] = "Olena"   # 💥 TypeError

# Порівняй зі списком (list) — те саме, але ПРАЦЮЄ:
patients_list = ["Ivan", 42, 180, 82]
patients_list[0] = "Olena"   # ✅ Спрацює без помилок

*Головна ідея immutable (незмінності) tuple:

Tuple створюється як "заморожений" набір значень — після створення жоден елемент не можна змінити, додати чи видалити (на відміну від list, де є append(), insert(), remove(), pop() з минулої задачі).

*Навіщо це потрібно на практиці:
# Tuple ідеально підходить для ДАНИХ, що НЕ ПОВИННІ змінюватись
# випадково під час роботи програми — наприклад, "знімок" одного
# конкретного вимірювання пацієнта:

patient_snapshot = ("Ivan", 42, 180, 82)
# Якщо десь у великій програмі хтось СПРОБУЄ випадково змінити
# вік пацієнта прямо в цьому tuple — Python одразу зупинить це
# помилкою, а не дозволить тихо зіпсувати дані

# Для даних, які МАЮТЬ змінюватись (список пацієнтів, куди додають/
# видаляють) — використовуй list, як у Практиці №1

*Порівняння list vs tuple (підсумок двох останніх задач):
	                    list	                                tuple
Синтаксис	            [1, 2, 3]	                            (1, 2, 3)
Змінність	            ✅ mutable (append, remove, pop)	       ❌ immutable
Коли використовувати	дані, що змінюються	                    фіксований "знімок" даних
Приклад із курсу	    patients (список пацієнтів)	            patient (один запис)
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №3 — Dict!

Створи:
patient = {
    "name": "Ivan",
    "age": 42,
    "diagnosis": "Sinusitis",
}

Додай:
temperature
weight
height

Потім виведи всі key → value через .items().
"""

patient = {
    "name": "Ivan",
    "age": 42,
    "diagnosis": "Sinusitis",
}

# --- Додавання нових ключів ---
# Синтаксис однаковий для НОВОГО ключа і для ОНОВЛЕННЯ існуючого:
# якщо ключа ще немає — Python його СТВОРЮЄ
patient["temperature"] = 38.2
patient["weight"] = 82
patient["height"] = 180

# --- Вивід через .items() ---
# .items() повертає пари (ключ, значення) — те саме розпакування tuple,
# що ти вже бачив у enumerate() та zip()
lines = [f"{key} → {value}" for key, value in patient.items()]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ДАНІ ПАЦІЄНТА".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────┐
│       ДАНІ ПАЦІЄНТА     │
├─────────────────────────┤
│  name → Ivan            │
│  age → 42               │
│  diagnosis → Sinusitis  │
│  temperature → 38.2     │
│  weight → 82            │
│  height → 180           │
└─────────────────────────┘
"""

"""
*Пояснення додавання ключів у dict:
patient["temperature"] = 38.2
#         ↑                ↑
#      ключ (str)      значення

# Якщо ключа "temperature" ЩЕ НЕМАЄ в dict — Python його СТВОРЮЄ:
patient = {"name": "Ivan", "age": 42, "diagnosis": "Sinusitis"}
patient["temperature"] = 38.2
# → {"name": "Ivan", "age": 42, "diagnosis": "Sinusitis", "temperature": 38.2}

# Якщо ключ ВЖЕ Є — той самий синтаксис його ПЕРЕЗАПИШЕ:
patient["age"] = 43   # ← оновлює існуюче значення, а не додає новий ключ

*Пояснення .items():
patient.items()
# → dict_items([('name', 'Ivan'), ('age', 42), ('diagnosis', 'Sinusitis'), ...])
#                   ↑
#              список пар (ключ, значення) — кожна пара це tuple

for key, value in patient.items():
    #    ↑     ↑
    #  розпаковуємо кожен tuple на 2 змінні (як у zip()/enumerate())
    print(key, value)

*Три способи ітерації по dict — для порівняння:
patient = {"name": "Ivan", "age": 42}

# 1. Тільки КЛЮЧІ (за замовчуванням, якщо просто for x in dict):
for key in patient:
    print(key)              # → name, age

# 2. Тільки ЗНАЧЕННЯ:
for value in patient.values():
    print(value)             # → Ivan, 42

# 3. І КЛЮЧ, і ЗНАЧЕННЯ одразу (найчастіше потрібно):
for key, value in patient.items():
    print(key, value)        # → name Ivan / age 42

*Порядок ключів у dict — важлива деталь:
Починаючи з Python 3.7, словники гарантовано зберігають порядок вставки — тобто patient.items() поверне ключі саме в тому порядку, в якому вони були додані (name, age, diagnosis, потім temperature, weight, height), а не у випадковому чи алфавітному порядку.
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №4 — get()!

Спробуй отримати:
patient["allergy"]

Побачиш проблему.

Потім:
patient.get("allergy")
і:
patient.get("allergy", "Unknown")

Поясни різницю.
"""

patient = {
    "name": "Ivan",
    "age": 42,
    "diagnosis": "Sinusitis",
    "temperature": 38.2,
    "weight": 82,
    "height": 180,
}

# --- Спроба 1: доступ через квадратні дужки [] ---
try:
    value = patient["allergy"]
except KeyError as e:
    result_1 = f"❌ KeyError: {e}"
else:
    result_1 = str(value)

# --- Спроба 2: .get() БЕЗ значення за замовчуванням ---
result_2 = patient.get("allergy")

# --- Спроба 3: .get() ЗІ значенням за замовчуванням ---
result_3 = patient.get("allergy", "Unknown")

# --- Вивід у рамці ---
lines = [
    'patient["allergy"]                  →  ' + result_1,
    'patient.get("allergy")              →  ' + repr(result_2),
    'patient.get("allergy", "Unknown")   →  ' + repr(result_3),
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ПОРІВНЯННЯ [] ТА .get()".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────────────────────────────────────────────────┐
│                     ПОРІВНЯННЯ [] ТА .get()                    │
├────────────────────────────────────────────────────────────────┤
│  patient["allergy"]                  →  ❌ KeyError: 'allergy'  │
│  patient.get("allergy")              →  None                   │
│  patient.get("allergy", "Unknown")   →  'Unknown'              │
└────────────────────────────────────────────────────────────────┘
"""

"""
*Пояснення різниці — три підходи до відсутнього ключа:
# 1. Квадратні дужки [] — "жорсткий" доступ:
patient["allergy"]
# 💥 KeyError: 'allergy'
# Програма ЗУПИНЯЄТЬСЯ з помилкою, якщо ключа немає

# 2. .get() без другого аргументу — "м'який" доступ:
patient.get("allergy")
# → None
# НІЯКОЇ помилки, просто повертає None (як falsy-значення з Challenge №2)

# 3. .get() з другим аргументом — "м'який" доступ ЗІ ЗНАЧЕННЯМ ЗА ЗАМОВЧУВАННЯМ:
patient.get("allergy", "Unknown")
# → "Unknown"
# Замість None повертає ТЕ, що ти явно вказав

*Порівняльна таблиця:
	            patient["allergy"]	     patient.get("allergy")	    patient.get("allergy", "Unknown")
Ключ є	        повертає значення	     повертає значення	        повертає значення
Ключа НЕМАЄ	    💥 KeyError	            None	                    "Unknown"
Треба 	        ✅ так, якщо ключ 	   ❌ ні	                     ❌ ні
try/except?     може бути відсутній

*Коли що використовувати:
# ✅ Квадратні дужки [] — коли ти ВПЕВНЕНИЙ, що ключ ЗАВЖДИ є
#    (наприклад, "name" — обов'язкове поле кожного пацієнта):
name = patient["name"]   # якщо раптом немає — це РЕАЛЬНА помилка в даних,
                           # хочемо, щоб програма про це "голосно" сказала

# ✅ .get() — коли поле МОЖЕ бути відсутнім, і це НОРМАЛЬНО:
allergy = patient.get("allergy", "Unknown")   # не кожен пацієнт має
                                                 # записану алергію — це очікувано

*Чому .get() з дефолтним значенням часто зручніший за try/except:
# ❌ Громіздко:
try:
    allergy = patient["allergy"]
except KeyError:
    allergy = "Unknown"

# ✅ Те саме, одним рядком:
allergy = patient.get("allergy", "Unknown")

Зв'язок із минулими задачами: це той самий принцип, що й у divide() (Практика №2 функцій) — там ми обирали між "тихою" поведінкою (return 0.0) і "голосною" помилкою (raise ValueError). Тут аналогічний вибір: [] — голосно (помилка), .get() — тихо (значення за замовчуванням). Обирати варто залежно від того, чи відсутність значення — це реальна проблема (тоді []), чи нормальна, очікувана ситуація (тоді .get()).
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №5 — Set!

Є:
diagnoses = [
    "sinusitis",
    "rhinitis",
    "sinusitis",
    "otitis",
    "rhinitis",
]

Отримай список унікальних діагнозів через set.
"""

diagnoses = [
    "sinusitis",
    "rhinitis",
    "sinusitis",
    "otitis",
    "rhinitis",
]

# --- set() автоматично прибирає ВСІ дублікати ---
unique_diagnoses = set(diagnoses)

# --- Якщо потрібен саме list (а не set) на виході ---
unique_diagnoses_list = list(unique_diagnoses)

# --- Приклад union/intersection: два відділення лікарні ---
ward_a_diagnoses = {"sinusitis", "rhinitis", "otitis"}
ward_b_diagnoses = {"sinusitis", "pharyngitis", "rhinitis"}

# union() — ОБ'ЄДНАННЯ: усі діагнози з ОБОХ відділень, без повторів
all_diagnoses = ward_a_diagnoses | ward_b_diagnoses   # або .union()

# intersection() — ПЕРЕТИН: діагнози, що зустрічаються в ОБОХ відділеннях
common_diagnoses = ward_a_diagnoses & ward_b_diagnoses   # або .intersection()

# --- Вивід у рамці ---
lines = [
    f"Оригінальний список:  {diagnoses}",
    f"Кількість елементів:  {len(diagnoses)}",
    "─" * 40,
    f"Унікальні (set):       {unique_diagnoses}",
    f"Кількість унікальних: {len(unique_diagnoses)}",
    "─" * 40,
    f"Відділення A:          {ward_a_diagnoses}",
    f"Відділення B:          {ward_b_diagnoses}",
    f"Union (об'єднання):    {all_diagnoses}",
    f"Intersection (перетин): {common_diagnoses}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  УНІКАЛЬНІ ДІАГНОЗИ (SET)".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                                УНІКАЛЬНІ ДІАГНОЗИ (SET)                              │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  Оригінальний список:  ['sinusitis', 'rhinitis', 'sinusitis', 'otitis', 'rhinitis']  │
│  Кількість елементів:  5                                                             │
│  ────────────────────────────────────────                                            │
│  Унікальні (set):       {'otitis', 'sinusitis', 'rhinitis'}                          │
│  Кількість унікальних: 3                                                             │
│  ────────────────────────────────────────                                            │
│  Відділення A:          {'otitis', 'sinusitis', 'rhinitis'}                          │
│  Відділення B:          {'pharyngitis', 'sinusitis', 'rhinitis'}                     │
│  Union (об'єднання):    {'otitis', 'rhinitis', 'pharyngitis', 'sinusitis'}           │
│  Intersection (перетин): {'sinusitis', 'rhinitis'}                                   │
└──────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
*Пояснення set():
diagnoses = ["sinusitis", "rhinitis", "sinusitis", "otitis", "rhinitis"]

set(diagnoses)
# → {"sinusitis", "rhinitis", "otitis"}

set (множина) — це колекція, яка автоматично відкидає дублікати і не гарантує порядок елементів (на відміну від list, де порядок завжди зберігається). Просто "загорнувши" список у set(...), отримуємо лише унікальні значення — без циклів, без ручної перевірки "чи вже було це значення".

*Чому порядок у виводі set може відрізнятись:
print(set(["a", "b", "c"]))
# Може вивести: {'a', 'b', 'c'} або {'c', 'a', 'b'} — порядок НЕ гарантований

Це важлива відмінність від dict, який (з Python 3.7+) зберігає порядок вставки — а set ніколи цього не гарантував і не гарантує.

*Операції над множинами — union та intersection:
ward_a = {"sinusitis", "rhinitis", "otitis"}
ward_b = {"sinusitis", "pharyngitis", "rhinitis"}

# union (|) — ОБ'ЄДНАННЯ: усе з обох множин, без повторів
ward_a | ward_b
# → {"sinusitis", "rhinitis", "otitis", "pharyngitis"}

# intersection (&) — ПЕРЕТИН: лише те, що є В ОБОХ множинах
ward_a & ward_b
# → {"sinusitis", "rhinitis"}

*Практичне застосування в медичному контексті:
# "Які діагнози зустрічаються в обох відділеннях?" — типове аналітичне питання:
common = ward_a_diagnoses & ward_b_diagnoses
if common:
    print(f"Спільні патерни захворюваності: {common}")

# "Скільки РІЗНИХ діагнозів усього по лікарні?"
total_unique = len(ward_a_diagnoses | ward_b_diagnoses)

Зв'язок з попередньою задачею (Практика №1 у розділі "базові типи"): set уже з'являвся раніше як один із базових типів Python (unique_exchanges — множина бірж). Тут показано практичну причину, чому саме set існує: миттєве прибирання дублікатів і математичні операції над множинами (об'єднання, перетин), яких немає у list.
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №6 — Set operations!

Є:
patient_a = {"fever", "cough", "pain"}
patient_b = {"cough", "pain", "fatigue"}

Знайди:
всі симптоми;
спільні симптоми;
симптоми тільки patient_a;
симптоми тільки patient_b.

Використай:
|
&
-
"""

patient_a = {"fever", "cough", "pain"}
patient_b = {"cough", "pain", "fatigue"}

# | (union) — ОБ'ЄДНАННЯ: усі симптоми з ОБОХ пацієнтів разом
all_symptoms = patient_a | patient_b

# & (intersection) — ПЕРЕТИН: симптоми, що є В ОБОХ пацієнтів
common_symptoms = patient_a & patient_b

# - (difference) — РІЗНИЦЯ: симптоми, що є ЛИШЕ в одного, а в іншого немає
# ВАЖЛИВО: напрямок має значення! a - b ≠ b - a
only_a = patient_a - patient_b   # тільки у patient_a
only_b = patient_b - patient_a   # тільки у patient_b

# ^ (symmetric_difference) — усе, що НЕ СПІЛЬНЕ (протилежність до &)
unique_to_either = patient_a ^ patient_b

# --- Вивід у рамці ---
lines = [
    f"patient_a:              {patient_a}",
    f"patient_b:              {patient_b}",
    "─" * 45,
    f"Усі симптоми (|):        {all_symptoms}",
    f"Спільні (&):             {common_symptoms}",
    f"Тільки patient_a (-):    {only_a}",
    f"Тільки patient_b (-):    {only_b}",
    f"НЕ спільні (^):          {unique_to_either}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  SET OPERATIONS — СИМПТОМИ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌──────────────────────────────────────────────────────────────────┐
│                     SET OPERATIONS — СИМПТОМИ                    │
├──────────────────────────────────────────────────────────────────┤
│  patient_a:              {'fever', 'cough', 'pain'}              │
│  patient_b:              {'cough', 'pain', 'fatigue'}            │
│  ─────────────────────────────────────────────                   │
│  Усі симптоми (|):        {'cough', 'pain', 'fever', 'fatigue'}  │
│  Спільні (&):             {'cough', 'pain'}                      │
│  Тільки patient_a (-):    {'fever'}                              │
│  Тільки patient_b (-):    {'fatigue'}                            │
│  НЕ спільні (^):          {'fever', 'fatigue'}                   │
└──────────────────────────────────────────────────────────────────┘
"""

"""
*Пояснення кожної операції — крок за кроком на цих конкретних даних:
patient_a = {"fever", "cough", "pain"}
patient_b = {"cough", "pain", "fatigue"}

# | union — ВСЕ разом, дублікати НЕ повторюються:
patient_a | patient_b
# → {"fever", "cough", "pain", "fatigue"}
#     ↑                          ↑
#   з A                        з B
#   "cough" і "pain" — спільні, тому в результаті лише ОДИН раз кожен

# & intersection — ТІЛЬКИ те, що в ОБОХ множинах:
patient_a & patient_b
# → {"cough", "pain"}
#   "fever" є тільки в A, "fatigue" тільки в B — не входять

# - difference — те, що в ЛІВІЙ, але НЕ в ПРАВІЙ:
patient_a - patient_b
# → {"fever"}         ← є в A, немає в B
patient_b - patient_a
# → {"fatigue"}       ← є в B, немає в A

# ^ symmetric_difference — "виключне АБО": все, що НЕ спільне
patient_a ^ patient_b
# → {"fever", "fatigue"}   ← те саме, що (only_a) | (only_b)

*Наочна візуалізація (діаграма Венна словами):
       patient_a          patient_b
    ┌───────────┐      ┌───────────┐
    │   fever   │      │  fatigue  │
    │      ┌────┼──────┼────┐      │
    │      │  cough, pain   │      │
    │      └────┼──────┼────┘      │
    └───────────┘      └───────────┘

|  (union)               = усе коло цілком (fever, cough, pain, fatigue)
&  (intersection)        = лише перетин посередині (cough, pain)
-  (a - b)               = лише ліва частина БЕЗ перетину (fever)
^  (symmetric_difference) = обидва "хвостики" БЕЗ перетину (fever, fatigue)

*Чому важливий напрямок у - (difference):
patient_a - patient_b   # → {"fever"}     "що є в A, чого немає в B"
patient_b - patient_a   # → {"fatigue"}   "що є в B, чого немає в A"
# Результати РІЗНІ! На відміну від | і &, де порядок не має значення

*Практичне застосування: 
такий аналіз симптомів корисний для порівняння клінічних картин двох пацієнтів — & показує спільний патерн (можлива схожа інфекція), а - виявляє специфічні для кожного пацієнта прояви.
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №7 — nested dictionary!

Створи:
patient = {
    "name": "Ivan",
    "measurements": {
        "temperature": 38.2,
        "weight": 82,
        "height": 180,
    },
}

Отримай:
Name
Temperature
Weight
Height
"""

patient = {
    "name": "Ivan",
    "measurements": {
        "temperature": 38.2,
        "weight": 82,
        "height": 180,
    },
}

# --- Прямий доступ через [][] — "жорсткий" спосіб ---
name = patient["name"]
temperature = patient["measurements"]["temperature"]
weight = patient["measurements"]["weight"]
height = patient["measurements"]["height"]

# --- Безпечний доступ через .get() — "м'який" спосіб (як у Практиці №4) ---
# Якщо "allergy" немає у measurements — поверне "Unknown", а не KeyError
allergy = patient.get("measurements", {}).get("allergy", "Unknown")

# --- Вивід у рамці ---
lines = [
    f"Name:         {name}",
    f"Temperature:  {temperature}",
    f"Weight:       {weight}",
    f"Height:       {height}",
    f"Allergy:      {allergy}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ДАНІ ПАЦІЄНТА (nested dict)".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────┐
│  ДАНІ ПАЦІЄНТА (nested dict)│
├─────────────────────────┤
│  Name:         Ivan     │
│  Temperature:  38.2     │
│  Weight:       82       │
│  Height:       180      │
│  Allergy:      Unknown  │
└─────────────────────────┘
"""

"""
*Пояснення доступу до вкладеного словника:
patient = {
    "name": "Ivan",
    "measurements": {
        "temperature": 38.2,
        "weight": 82,
        "height": 180,
    },
}

patient["measurements"]
# → {"temperature": 38.2, "weight": 82, "height": 180}
#   ↑ це ЦІЛИЙ окремий словник — "вкладений" усередині patient

patient["measurements"]["temperature"]
#         ↑                  ↑
#   перший крок:         другий крок:
#   дістаємо ВНУТРІШНІЙ  дістаємо ЗНАЧЕННЯ
#   словник              ВСЕРЕДИНІ нього
# → 38.2

Читай справа наліво "по шарах": спочатку patient["measurements"] дає словник, а вже з нього береться ["temperature"].

*Безпечний доступ через .get() для вкладених структур:
patient.get("measurements", {}).get("allergy", "Unknown")
#            ↑              ↑        ↑           ↑
#      шукаємо          якщо НЕМАЄ   шукаємо   якщо НЕМАЄ
#      "measurements"   "measurements"  "allergy"  "allergy"
#                       → порожній dict {}         → "Unknown"

*Чому саме {} (порожній словник), а не просто None як дефолт для .get("measurements", ...):
# ❌ Якби дефолтом був None:
patient.get("measurements", None).get("allergy", "Unknown")
# Якщо "measurements" відсутній → None.get(...) → 💥 AttributeError!
# (у None немає методу .get())

# ✅ Дефолт — порожній dict {}:
patient.get("measurements", {}).get("allergy", "Unknown")
# Якщо "measurements" відсутній → {}.get("allergy", "Unknown") → "Unknown"
# (у порожнього dict МЕТОД .get() є — просто нічого не знайде і поверне дефолт)

Це важливий "ланцюжковий" патерн: коли треба безпечно дістатись кількох рівнів углиб, кожен .get() повинен мати дефолт того ж типу, який очікується на наступному кроці (тут — dict, бо далі викликається ще один .get()).

*Порівняння прямого доступу [] vs ланцюжка .get():
	                    patient["measurements"]["temperature"]	    patient.get("measurements", {}).get("temperature", "Unknown")
Якщо все є	            ✅ швидко, коротко	                       ✅ теж працює
Якщо "measurements" 	💥 KeyError	                                ✅ "Unknown", без падіння
відсутній
Коли використовувати	структура даних гарантовано повна	        дані можуть бути неповними (напр. з зовнішнього API)
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №8 — копіювання!

Продемонструй різницю між:
b = a
b = a.copy()
і:
b = deepcopy(a)

Використай вкладений список:
a = [[1, 2], [3, 4]]

і покажи, коли зміна b впливає на a.
"""

from copy import deepcopy

# --- Сценарій 1: b = a (просте присвоєння) ---
a1 = [[1, 2], [3, 4]]
b1 = a1

print("\n=== 1. b = a ===")
print(f"id(a1) == id(b1):        {id(a1) == id(b1)}")
print(f"id(a1[0]) == id(b1[0]):  {id(a1[0]) == id(b1[0])}")

b1[0][0] = 99   # змінюємо ВКЛАДЕНИЙ елемент через b1
print("Після b1[0][0] = 99:")
print(f"  a1 = {a1}")
print(f"  b1 = {b1}")


# --- Сценарій 2: b = a.copy() (поверхнева копія, shallow copy) ---
a2 = [[1, 2], [3, 4]]
b2 = a2.copy()

print("\n=== 2. b = a.copy() ===")
print(f"id(a2) == id(b2):        {id(a2) == id(b2)}")
print(f"id(a2[0]) == id(b2[0]):  {id(a2[0]) == id(b2[0])}")

b2[0][0] = 99   # змінюємо ВКЛАДЕНИЙ елемент через b2
print("Після b2[0][0] = 99:")
print(f"  a2 = {a2}")
print(f"  b2 = {b2}")


# --- Сценарій 3: b = deepcopy(a) (глибока копія) ---
a3 = [[1, 2], [3, 4]]
b3 = deepcopy(a3)

print("\n=== 3. b = deepcopy(a) ===")
print(f"id(a3) == id(b3):        {id(a3) == id(b3)}")
print(f"id(a3[0]) == id(b3[0]):  {id(a3[0]) == id(b3[0])}")

b3[0][0] = 99   # змінюємо ВКЛАДЕНИЙ елемент через b3
print("Після b3[0][0] = 99:")
print(f"  a3 = {a3}")
print(f"  b3 = {b3}")

# --- Підсумкова рамка ---
lines = [
    "b = a          → a ЗМІНЮЄТЬСЯ (той самий об'єкт повністю)",
    "b = a.copy()   → a ЗМІНЮЄТЬСЯ (вкладені списки — спільні!)",
    "b = deepcopy() → a НЕ змінюється (усе незалежне)",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ПІДСУМОК: КОПІЮВАННЯ СПИСКІВ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
=== 1. b = a ===
id(a1) == id(b1):        True
id(a1[0]) == id(b1[0]):  True
Після b1[0][0] = 99:
  a1 = [[99, 2], [3, 4]]
  b1 = [[99, 2], [3, 4]]

=== 2. b = a.copy() ===
id(a2) == id(b2):        False
id(a2[0]) == id(b2[0]):  True
Після b2[0][0] = 99:
  a2 = [[99, 2], [3, 4]]
  b2 = [[99, 2], [3, 4]]

=== 3. b = deepcopy(a) ===
id(a3) == id(b3):        False
id(a3[0]) == id(b3[0]):  False
Після b3[0][0] = 99:
  a3 = [[1, 2], [3, 4]]
  b3 = [[99, 2], [3, 4]]

┌──────────────────────────────────────────────────────────────┐
│                  ПІДСУМОК: КОПІЮВАННЯ СПИСКІВ                │
├──────────────────────────────────────────────────────────────┤
│  b = a          → a ЗМІНЮЄТЬСЯ (той самий об'єкт повністю)   │
│  b = a.copy()   → a ЗМІНЮЄТЬСЯ (вкладені списки — спільні!)  │
│  b = deepcopy() → a НЕ змінюється (усе незалежне)            │
└──────────────────────────────────────────────────────────────┘
"""

"""
*Пояснення трьох рівнів копіювання:
1. b = a — НЕ копія взагалі, а просто ДРУГИЙ ЯРЛИК на той самий об'єкт:
a = [[1, 2], [3, 4]]
b = a

id(a) == id(b)         # True — це ОДИН і той самий список у пам'яті!

b[0][0] = 99
# a = [[99, 2], [3, 4]]   ← a ТЕЖ змінився, бо a і b — це ОДНЕ й те саме

Це та сама ідея, що й у Challenge №1 попереднього дня (a = 5; b = a; b = 10) — тільки тут b[0][0] = 99 не перепризначає b на новий об'єкт, а змінює вміст об'єкта, на який вказують обидві змінні одночасно.

2. b = a.copy() — поверхнева копія (shallow copy), головна пастка:
a = [[1, 2], [3, 4]]
b = a.copy()   # або list(a), або a[:]

id(a) == id(b)          # False — ЗОВНІШНІ списки РІЗНІ об'єкти
id(a[0]) == id(b[0])    # True  — ⚠️ АЛЕ вкладені списки — ОДИН і той самий об'єкт!

b[0][0] = 99
# a = [[99, 2], [3, 4]]   ← a ЗМІНИВСЯ! Хоча ми копіювали...

.copy() копіює лише перший рівень — створює новий зовнішній список, але елементи всередині (тут — внутрішні списки [1, 2] і [3, 4]) залишаються посиланнями на ті самі об'єкти, що й в оригіналі. Тому зміна вкладеного елемента через b все одно "просочується" в a.

3. b = deepcopy(a) — глибока копія, повна незалежність:
from copy import deepcopy

a = [[1, 2], [3, 4]]
b = deepcopy(a)

id(a) == id(b)          # False
id(a[0]) == id(b[0])    # False — тепер і ВНУТРІШНІ списки теж РІЗНІ об'єкти!

b[0][0] = 99
# a = [[1, 2], [3, 4]]   ← a НЕ змінився! Повна незалежність

deepcopy() рекурсивно копіює абсолютно все — зовнішній список, кожен вкладений список, і так далі на будь-яку глибину вкладеності. Тому зміни в b ніколи не відображаються на a.

*Порівняльна таблиця:
	                                b = a	         b = a.copy()	   b = deepcopy(a)
Зовнішній список	                той самий	     новий	           новий
Вкладені списки	                    ті самі	⚠️      ті самі	          нові
Зміна b[0][0]       впливає на a?	✅ так	       ⚠️ так	        ❌ ні
Зміна b.append(...) впливає на a?	✅ так	       ❌ ні	           ❌ ні

*Головний висновок — зв'язок із Challenge №2 (mutable default argument): 
та сама небезпека "спільного mutable-об'єкта", яку ти вже бачив із patients=[] за замовчуванням, тут проявляється в поверхневому копіюванні. .copy() виглядає як безпечний спосіб уникнути зміни оригіналу, але для вкладених структур (списку списків, списку словників тощо) цього недостатньо — потрібен саме deepcopy().
"""
