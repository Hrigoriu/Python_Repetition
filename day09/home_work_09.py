"""
## !Challenge 1 — Patient Search from JSON!

Створи функцію:
def find_patient(
    patients: list[dict],
    name: str,
) -> dict | None:
    ...

Вона повинна знаходити пацієнта за ім'ям.

Наприклад:
patient = find_patient(patients, "Olena")

Результат:
{
    "id": 2,
    "name": "Olena",
    "age": 35
}

Якщо пацієнта немає:
None
"""

import json


def find_patient(patients: list[dict], name: str) -> dict | None:
    """Знаходить пацієнта за іменем (нечутливо до регістру).

    Version A — for + early return (класичний, найзрозуміліший підхід).
    """
    for patient in patients:
        if patient["name"].lower() == name.lower():
            return patient   # ЗНАЙШЛИ — одразу повертаємо, функція завершується ТУТ
    return None               # пройшли ВЕСЬ список, збігу не було


def find_patient_next(patients: list[dict], name: str) -> dict | None:
    """Той самий результат — через next() з генератором (Pythonic-спосіб)."""
    return next(
        (patient for patient in patients if patient["name"].lower() == name.lower()),
        None,   # значення за замовчуванням, якщо генератор нічого не дав
    )


# --- Завантаження даних ---
with open("data/patients.json", "r", encoding="utf-8") as file:
    patients = json.load(file)

# --- Демонстрація ---
result_a = find_patient(patients, "Olena")
result_b = find_patient_next(patients, "olena")   # навмисно малими літерами
result_missing = find_patient(patients, "Dmytro")

# --- Вивід у рамці ---
lines = [
    "find_patient(patients, 'Olena'):",
    f"  {result_a}",
    "─" * 45,
    "find_patient_next(patients, 'olena'):",
    f"  {result_b}",
    "─" * 45,
    "find_patient(patients, 'Dmytro'):",
    f"  {result_missing}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ПОШУК ПАЦІЄНТА".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────────────────────────────┐
│                   ПОШУК ПАЦІЄНТА                │
├─────────────────────────────────────────────────┤
│  find_patient(patients, 'Olena'):               │
│    {'id': 2, 'name': 'Olena', 'age': 35}        │
│  ─────────────────────────────────────────────  │
│  find_patient_next(patients, 'olena'):          │
│    {'id': 2, 'name': 'Olena', 'age': 35}        │
│  ─────────────────────────────────────────────  │
│  find_patient(patients, 'Dmytro'):              │
│    None                                         │
└─────────────────────────────────────────────────┘
"""

"""
*Пояснення Version A — for + early return:
def find_patient(patients, name):
    for patient in patients:
        if patient["name"].lower() == name.lower():
            return patient   # ← ЗУПИНЯЄ функцію одразу тут, повертає результат
    return None               # ← виконується ТІЛЬКИ якщо жоден return вище не спрацював

return усередині циклу — це негайний вихід не лише з циклу, а з усієї функції. Як тільки знайдено збіг — решта пацієнтів навіть не перевіряється, функція одразу повертає результат. Якщо for дійшов до кінця списку, жодного разу не викликавши return patient — виконується останній рядок return None.

*Пояснення Version B — next() з генератором:
next(
    (patient for patient in patients if patient["name"].lower() == name.lower()),
    None,
)

next() бере перший елемент із генератора і одразу зупиняється (не обчислює решту) — це та сама ідея short-circuit, що вже зустрічалась у any(). Другий аргумент next() — значення за замовчуванням, якщо генератор порожній (нічого не знайшов):


next(iter([1, 2, 3]))          # → 1  (перший елемент)
next(iter([]))                  # 💥 StopIteration! (порожньо, дефолту немає)
next(iter([]), "default")       # → "default"  (з дефолтом — безпечно)

*Порівняння двох підходів:
	                        for + early return	          next() + генератор
Читабельність для новачка	✅ найпростіше зрозуміти	     потребує знання генераторів
Кількість рядків	        4	                          1 (хоч і довший рядок)
Швидкість зупинки	        ✅ зупиняється на знахідці	✅ теж зупиняється на знахідці
"Pythonic"-стиль	        звичайний, зрозумілий	      компактний, часто в досвідчених розробників

*Пояснення нечутливості до регістру:
patient["name"].lower() == name.lower()
#              ↑                    ↑
#         "Olena" → "olena"    "olena" → "olena"

# Обидві сторони приводяться до нижнього регістру ПЕРЕД порівнянням —
# та сама техніка, що вже зустрічалась у Challenge №6 попереднього дня
# (пошук пацієнта нечутливо до регістру)

*Тип повернення dict | None — пояснення сигнатури:
def find_patient(patients: list[dict], name: str) -> dict | None:
    #                                                  ↑
    #                          функція повертає АБО dict, АБО None
    #                          (синтаксис Python 3.10+; у старіших версіях
    #                           писали б Optional[dict] з модуля typing)

Це чесно "документує" обидва можливі результати — той, хто викликає find_patient(), одразу бачить із сигнатури, що треба перевірити на None, перш ніж використовувати результат:


patient = find_patient(patients, "Dmytro")
if patient is not None:
    print(patient["age"])   # безпечно — ми ВЖЕ перевірили
else:
    print("Пацієнта не знайдено")
"""

# ==============================================================================
# ==============================================================================

"""
## !Challenge 2 — JSON update!

Завантаж:
patients.json

Зміни вік:
Ivan → 43

та збережи файл назад.

Тут важливий pipeline:
JSON file
    ↓
load
    ↓
Python objects
    ↓
modify
    ↓
dump
    ↓
JSON file
"""

import json


def find_patient(patients: list[dict], name: str) -> dict | None:
    """Знаходить пацієнта за іменем (нечутливо до регістру).

    (Перевикористано з Challenge 1 — не дублюємо логіку пошуку.)
    """
    for patient in patients:
        if patient["name"].lower() == name.lower():
            return patient
    return None


# ═══════════════════════════════════════════
# КРОК 1: load — JSON file → Python objects
# ═══════════════════════════════════════════
with open("data/patients.json", "r", encoding="utf-8") as file:
    patients = json.load(file)


# ═══════════════════════════════════════════
# КРОК 2: modify — Варіант A: через find_patient() (DRY, перевикористання)
# ═══════════════════════════════════════════
ivan = find_patient(patients, "Ivan")
if ivan is not None:
    ivan["age"] = 43   # ← ВАЖЛИВО: ivan — це ПОСИЛАННЯ на dict ВСЕРЕДИНІ patients,
                        #   тому ця зміна одразу відображається і в самому patients!


# ═══════════════════════════════════════════
# КРОК 2 (альтернатива): Варіант B — простий for без окремої функції
# ═══════════════════════════════════════════
# (закоментовано — це РІВНОЦІННА альтернатива Варіанту A, не виконуємо ОБИДВА
#  одночасно, інакше вік змінився б двічі поспіль без користі)
#
for patient in patients:
    if patient["name"].lower() == "ivan".lower():
        patient["age"] = 45
        break


# ═══════════════════════════════════════════
# КРОК 3: dump — Python objects → JSON file
# ═══════════════════════════════════════════
with open("data/patients.json", "w", encoding="utf-8") as file:
    json.dump(patients, file, indent=2, ensure_ascii=False)


# ═══════════════════════════════════════════
# Перевірка: читаємо файл ЗАНОВО, підтверджуючи, що зміна ЗБЕРЕГЛАСЬ на диску
# ═══════════════════════════════════════════
with open("data/patients.json", "r", encoding="utf-8") as file:
    reloaded_patients = json.load(file)

reloaded_ivan = find_patient(reloaded_patients, "Ivan")

# --- Вивід у рамці ---
lines = [
    f"Ivan['age'] після modify():        {ivan['age']}",
    f"Ivan['age'] після перечитання файлу: {reloaded_ivan['age']}",
    f"Збіглося? {ivan['age'] == reloaded_ivan['age'] == 43}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  JSON UPDATE PIPELINE".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌───────────────────────────────────────────┐
│             JSON UPDATE PIPELINE          │
├───────────────────────────────────────────┤
│  Ivan['age'] після modify():        43    │
│  Ivan['age'] після перечитання файлу: 43  │
│  Збіглося? True                           │
└───────────────────────────────────────────┘
"""

"""
#*Пояснення pipeline крок за кроком:

JSON file  →  load  →  Python objects  →  modify  →  dump  →  JSON file
# 1. load — читаємо ФАЙЛ, перетворюємо ТЕКСТ у Python-структуру
patients = json.load(file)
# patients = [{"id": 1, "name": "Ivan", "age": 42}, {"id": 2, ...}, ...]

# 2. modify — змінюємо дані В ПАМ'ЯТІ (файл поки що НЕ ЗМІНЕНИЙ на диску!)
ivan["age"] = 43
# У ЦЕЙ момент на диску ЩЕ старий файл (age: 42) — зміна лише в оперативній пам'яті

# 3. dump — перезаписуємо ФАЙЛ, беручи ЗМІНЕНУ структуру з пам'яті
json.dump(patients, file, ...)
# ТІЛЬКИ ТЕПЕР файл на диску оновлюється

#*Ключовий момент, чому ivan["age"] = 43 одразу змінює й patients:
ivan = find_patient(patients, "Ivan")
# ivan — це НЕ копія, а ПОСИЛАННЯ на ТОЙ САМИЙ dict, що лежить ВСЕРЕДИНІ patients

ivan["age"] = 43
# Змінюємо dict ЧЕРЕЗ посилання ivan — але оскільки ivan і елемент 
# всередині patients — це ОДИН і той самий об'єкт у пам'яті,
# зміна одразу видно і при зверненні через patients:

print(patients[0]["age"])   # 43 — теж змінилось! (навіть без окремого рядка коду)

Це та сама механіка "спільного mutable-об'єкта", яку ти вже бачив у Практиці №8 (b = a без .copy()) — тут вона працює на нашу користь: не потрібно вручну "класти зміну назад" у patients, бо find_patient() повертає посилання, а не копію.

#*Чому обов'язково потрібен КРОК 3 (dump) — найважливіший урок цього завдання:
patients = json.load(file)
ivan["age"] = 43
# ⚠️ Якщо ЗАБУТИ json.dump() — файл на диску ЗАЛИШИТЬСЯ старим (age: 42)!
# Зміна існує ЛИШЕ в оперативній пам'яті Python, поки програма виконується.
# Щойно програма завершиться — ця зміна БЕЗПОВОРОТНО зникне.

#*Чому перевірка через ПОВТОРНЕ читання файлу — важлива практика:
# Недостатньо перевірити ivan["age"] одразу після modify() —
# це лише підтверджує, що ЗМІННА В ПАМ'ЯТІ Python правильна.
# Справжня перевірка — ЗАКРИТИ файл, ВІДКРИТИ його ЗНОВУ і прочитати:

with open("data/patients.json", "r") as file:
    reloaded_patients = json.load(file)
# Якщо reloaded_ivan["age"] == 43 — це ДОКАЗ, що зміна РЕАЛЬНО збереглась на диску,
# а не лише "здається" правильною в пам'яті поточного запуску програми

#*Зв'язок із попередніми завданнями: 
# цей Challenge об'єднує весь день у один практичний робочий процес — find_patient() з Challenge 1 (пошук), розуміння mutable/reference з Практики №8 попереднього дня (чому зміна через посилання працює), і повний цикл load → modify → dump із Task 5-7 (JSON-операції).
"""

# ==============================================================================
# ==============================================================================

"""
## !Challenge 3 — filtering!

Знайди всіх пацієнтів:
age >= 44

Очікуваний результат:
[
    {"id": 1, "name": "Ivan", "age": 43},
    {"id": 3, "name": "Petro", "age": 51},
]
"""

import json

THRESHOLD = 44

# --- Завантаження актуальних даних (після Challenge 2, де Ivan → 43) ---
with open("data/patients.json", "r", encoding="utf-8") as file:
    patients = json.load(file)

# --- Варіант 1: list comprehension ---
older_patients_comprehension = [p for p in patients if p["age"] >= THRESHOLD]

# --- Варіант 2: filter() + lambda ---
older_patients_filter = list(filter(lambda p: p["age"] >= THRESHOLD, patients))

# --- Вивід у рамці ---
lines = [
    f"Усі пацієнти:              {patients}",
    "─" * 50,
    f"List comprehension (>= {THRESHOLD}):",
    f"  {older_patients_comprehension}",
    "─" * 50,
    f"filter() + lambda (>= {THRESHOLD}):",
    f"  {older_patients_filter}",
    "─" * 50,
    f"Однакові результати? {older_patients_comprehension == older_patients_filter}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ФІЛЬТРАЦІЯ ЗА ВІКОМ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                    ФІЛЬТРАЦІЯ ЗА ВІКОМ                                                  │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│  Усі пацієнти:                                                                                                          │
│   [{'id': 1, 'name': 'Ivan', 'age': 45}, {'id': 2, 'name': 'Olena', 'age': 35}, {'id': 3, 'name': 'Petro', 'age': 51}]  │
│  ──────────────────────────────────────────────────                                                                     │
│  List comprehension (>= 44):                                                                                            │
│    [{'id': 1, 'name': 'Ivan', 'age': 45}, {'id': 3, 'name': 'Petro', 'age': 51}]                                        │
│  ──────────────────────────────────────────────────                                                                     │
│  filter() + lambda (>= 44):                                                                                             │
│    [{'id': 1, 'name': 'Ivan', 'age': 45}, {'id': 3, 'name': 'Petro', 'age': 51}]                                        │
│  ──────────────────────────────────────────────────                                                                     │
│  Однакові результати? True                                                                                              │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
#*Пояснення list comprehension над списком словників:
[p for p in patients if p["age"] >= 44]
#  ↑                       ↑
# повертаємо ВЕСЬ dict     умова: заглядаємо ВСЕРЕДИНУ dict,
# (не окреме поле!)         перевіряємо саме ключ "age"

Це той самий патерн, що вже зустрічався в Challenge №7 попереднього дня (get_high_risk_patients) — там ми фільтрували за одним полем, повертали інше (temp → name). Тут же ми фільтруємо за одним полем (age), а повертаємо ВЕСЬ dict цілком — не лише ім'я чи вік окремо, а повний запис пацієнта.

#*Крок за кроком для наших даних:
patients = [
    {"id": 1, "name": "Ivan", "age": 45},
    {"id": 2, "name": "Olena", "age": 35},
    {"id": 3, "name": "Petro", "age": 51},
]

# p = {"id": 1, "name": "Ivan", "age": 45}  → 45 >= 44? True  → додаємо ВЕСЬ dict
# p = {"id": 2, "name": "Olena", "age": 35} → 35 >= 44? False → пропускаємо
# p = {"id": 3, "name": "Petro", "age": 51} → 51 >= 44? True  → додаємо ВЕСЬ dict

result = [
    {"id": 1, "name": "Ivan", "age": 45},
    {"id": 3, "name": "Petro", "age": 51},
]

#*Пояснення filter() — та сама логіка, інший синтаксис:
filter(lambda p: p["age"] >= 44, patients)
#      ↑                          ↑
#   функція-умова                послідовність для перевірки
#   (кожен p — окремий dict)

list(filter(...))   # ← filter() повертає "лінивий" ітератор, обгортаємо в list()

#*Порівняння двох підходів (продовження теми з Практики №1 попереднього дня):
	                        List comprehension	                  filter() + lambda
Синтаксис	                [p for p in patients if ...]	      filter(lambda p: ..., patients)
Читабельність	            ✅ прямо, без проміжної функції	     потребує обгортки list()
Складніша умова (and/or)	✅ легко дописати	                 ускладнює lambda

#*Зв'язок із Challenge 1 (find_patient()) — важлива відмінність у ПІДХОДІ:
# find_patient() — шукає ОДНОГО пацієнта, зупиняється на ПЕРШІЙ знахідці:
def find_patient(patients, name):
    for patient in patients:
        if patient["name"].lower() == name.lower():
            return patient   # ← ЗУПИНКА на першому збігу
    return None

# Фільтрація — збирає УСІХ, хто підходить, НЕ зупиняючись:
[p for p in patients if p["age"] >= 40]   # ← проходить ВЕСЬ список до кінця

#*Це принципова різниця в намірі: 
# "знайди ОДНОГО конкретного" (пошук) проти "збери УСІХ, хто підходить" (фільтрація) — обидва патерни працюють над одним і тим самим типом даних (list[dict]), але вирішують різні задачі.
"""

# ==============================================================================
# ==============================================================================

"""
## !Challenge 4 — statistics report!

Створи файл:
data/report.txt

Приблизний результат:
PATIENT REPORT
==============

Total patients: 3
Average age: 43.0
Oldest patient: Petro
Oldest age: 51
"""

import json

# --- Завантаження актуальних даних ---
with open("data/patients.json", "r", encoding="utf-8") as file:
    patients = json.load(file)

# --- Обчислення статистики (перевикористовуємо підхід з Task 7) ---
total_patients = len(patients)
average_age = sum(p["age"] for p in patients) / total_patients
oldest = max(patients, key=lambda p: p["age"])

# --- Формування тексту звіту ---
title = "PATIENT REPORT"
report = (
    f"{title}\n"
    f"{'=' * len(title)}\n\n"
    f"Total patients: {total_patients}\n"
    f"Average age: {average_age:.1f}\n"
    f"Oldest patient: {oldest['name']}\n"
    f"Oldest age: {oldest['age']}\n"
)

# --- Збереження звіту у файл ---
with open("data/report.txt", "w", encoding="utf-8") as file:
    file.write(report)

# --- Читання файлу назад для перевірки ---
with open("data/report.txt", "r", encoding="utf-8") as file:
    saved_report = file.read()

# --- Вивід у рамці ---
report_lines = saved_report.rstrip("\n").split("\n")
width = max(len(line) for line in report_lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  DATA/REPORT.TXT".center(width) + "│")
print("├" + "─" * width + "┤")
for line in report_lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────┐
│      DATA/REPORT.TXT    │
├─────────────────────────┤
│  PATIENT REPORT         │
│  ==============         │
│                         │
│  Total patients: 3      │
│  Average age: 43.7      │
│  Oldest patient: Petro  │
│  Oldest age: 51         │
└─────────────────────────┘
"""

"""
#*Пояснення динамічного заголовка "=" * len(title):
title = "PATIENT REPORT"
"=" * len(title)
#         ↑
#    рахує ДОВЖИНУ рядка "PATIENT REPORT" → 14 символів
# "=" * 14 → "=============="

Замість того, щоб вручну порахувати й вписати рівно 14 символів =, лінія розраховується автоматично на основі довжини заголовка. Якщо назву звіту завтра зміниш на щось довше чи коротше — розділювач сам підлаштується, без ризику помилитись у ручному підрахунку.

#*Пояснення формування багаторядкового тексту через конкатенацію f-string:
report = (
    f"{title}\n"                          # рядок 1: заголовок
    f"{'=' * len(title)}\n\n"               # рядок 2: розділювач + ПОРОЖНІЙ рядок
    f"Total patients: {total_patients}\n"    # рядок 3
    f"Average age: {average_age:.1f}\n"       # рядок 4
    f"Oldest patient: {oldest['name']}\n"      # рядок 5
    f"Oldest age: {oldest['age']}\n"            # рядок 6
)

Дужки ( ... ) навколо кількох рядків f-string автоматично склеюють їх в один рядок — це стандартний спосіб Python розбити довгий текст на кілька рядків коду для читабельності, не втрачаючи логіки об'єднання.

#*Перевикористання логіки статистики (DRY) — зв'язок із Task 7:
# Та сама формула, що вже застосовувалась у Task 7:
average_age = sum(p["age"] for p in patients) / len(patients)
oldest = max(patients, key=lambda p: p["age"])

Тут немає нової логіки обчислення — використано точно ті самі підходи (sum() з генератором, max() з key), лише результат форматується інакше: не для консольного виводу в рамці, а для збереження в текстовий файл у конкретному, наперед заданому форматі.

#*Чому дані беруться саме з patients.json (динамічно), а не вводяться вручну:
Це ключовий принцип, що проходить крізь усе заняття: report.txt завжди відображатиме актуальний стан даних. Якби числа (43, 3, Petro, 51) були "заший в код", після будь-якої зміни patients.json (як у Challenge 2, де вік Ivan змінився з 42 на 45) звіт застарів би й показував неправильну статистику — саме тому обчислення завжди йде від джерела даних (файлу), а не від захардкожених значень.
"""

# ==============================================================================
# ==============================================================================

"""
## !Challenge 5 — error handling!

Напиши функцію:
def load_json(path: str) -> dict | list | None:
    ...

Вона повинна коректно обробляти:
FileNotFoundError
JSONDecodeError

та повертати:
None
у випадку помилки.
"""

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
    file.write('{"name": "Ivan", "age": }')   # ← некоректний синтаксис (немає значення)


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

"""
⚠ Помилка: файл 'data/nonexistent.json' не знайдено.
⚠ Помилка: файл 'data/broken.json' містить некоректний JSON (Expecting value: line 1 column 25 (char 24)).

┌───────────────────────────────────────────────────────────────┐
│                  LOAD_JSON() — ОБРОБКА ПОМИЛОК                │
├───────────────────────────────────────────────────────────────┤
│  load_json('data/patients.json')   → list (дані завантажено)  │
│  load_json('data/nonexistent.json') → None                    │
│  load_json('data/broken.json')      → None                    │
└───────────────────────────────────────────────────────────────┘
"""

"""
#*Пояснення try/except з ДВОМА окремими блоками:
try:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
except FileNotFoundError:
    # спрацьовує, якщо ФАЙЛ ВЗАГАЛІ НЕ ІСНУЄ за таким шляхом
    ...
except json.JSONDecodeError:
    # спрацьовує, якщо файл ІСНУЄ, але його ВМІСТ — не валідний JSON
    ...

#*Це два різних типи проблем, що виникають на різних етапах:
# FileNotFoundError виникає ТУТ:
open(path, "r", ...)
#    ↑
#    якщо файлу немає — помилка ВІДРАЗУ, json.load() навіть не викликається

# JSONDecodeError виникає ТУТ:
json.load(file)
#    ↑
#    файл ВІДКРИВСЯ успішно, але текст усередині
#    не є коректним JSON (наприклад, пропущена лапка чи значення)

#*Чому важливо мати ОКРЕМІ except-блоки, а не один загальний:
# ❌ Один загальний except — втрачається інформація ПРО ЩО саме помилка:
try:
    ...
except Exception as e:
    print(f"Якась помилка: {e}")   # незрозуміло — файл відсутній чи JSON зламаний?

# ✅ Окремі except — точна діагностика для КОЖНОГО випадку:
except FileNotFoundError:
    print("Файл не існує")          # ← конкретна причина
except json.JSONDecodeError:
    print("JSON пошкоджений")        # ← інша конкретна причина

#*Демонстрація "зіпсованого" JSON — навмисна помилка синтаксису:
'{"name": "Ivan", "age": }'
#                        ↑
#            ПРОПУЩЕНЕ значення після двокрапки —
#            JSON вимагає ЩОСЬ тут (число, рядок, true/false/null),
#            порожнє місце — синтаксично некоректно

#*Тип повернення dict | list | None — чому саме така сигнатура:
def load_json(path: str) -> dict | list | None:

JSON-файл на верхньому рівні може бути або об'єктом ({...} → Python dict, як patient.json з Task 5), або масивом ([...] → Python list, як patients.json з Task 7). Функція не знає заздалегідь, який саме тип структури лежить у конкретному файлі — тому сигнатура чесно відображає всі три можливі результати: dict, list, або None (у разі помилки).

#*Зв'язок із попередніми задачами — "тиха" vs "голосна" обробка помилок:
Це продовження теми з divide() (функції, попередній день) і .get() (dict, цей день): там ми обирали між raise (голосно) і поверненням дефолту (тихо). 
Тут — комбінація обох підходів: помилка повідомляється (print, "голосно" для розробника), але сама функція не падає, а повертає None ("тихо" для коду, що її викликає) — так виклик load_json() можна безпечно перевірити через if result is None: замість обов'язкового try/except навколо кожного виклику функції.
"""

# ==============================================================================
# ==============================================================================

"""
## !🔥 Challenge 6 — MedAssistant Data Pipeline!

Це головне завдання дня.

Створи:
data/medassistant_patients.json

з пацієнтами:
[
    {
        "id": 1,
        "name": "Ivan",
        "age": 42,
        "diagnosis": "sinusitis",
        "temperature": 37.2
    },
    {
        "id": 2,
        "name": "Olena",
        "age": 35,
        "diagnosis": "rhinitis",
        "temperature": 36.7
    },
    {
        "id": 3,
        "name": "Petro",
        "age": 61,
        "diagnosis": "sinusitis",
        "temperature": 38.5
    }
]

Програма повинна:
load JSON
   ↓
calculate statistics
   ↓
filter patients
   ↓
generate report
   ↓
save report

Звіт повинен містити:
-кількість пацієнтів;
-середній вік;
-середню температуру;
-пацієнтів із температурою >= 38.0;
-пацієнтів із sinusitis.

🧩 Структура коду

Прагни поступово перейти до такої архітектури:
def load_patients(path):
    ...


def save_report(path, report):
    ...


def calculate_statistics(patients):
    ...


def filter_by_temperature(patients, threshold):
    ...


def main():
    ...


if __name__ == "__main__":
    main()
"""

"""medassistant_pipeline.py

Full patient data pipeline for MedAssistant:
    load JSON -> calculate statistics -> filter patients ->
    generate report -> save report

Architecture: each function has ONE responsibility (single
responsibility principle) — main() only orchestrates them.
"""

import json


# ═══════════════════════════════════════════
# LOAD
# ═══════════════════════════════════════════
def load_patients(path: str) -> list[dict] | None:
    """Load a list of patient records from a JSON file.

    Handles the two most common failure modes explicitly, so callers
    can rely on a clean None instead of an uncaught exception.

    Args:
        path: Path to the JSON file.

    Returns:
        list[dict] | None: The patient records, or None on failure.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"⚠ Error: file '{path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"⚠ Error: file '{path}' contains invalid JSON ({e}).")
        return None


# ═══════════════════════════════════════════
# CALCULATE
# ═══════════════════════════════════════════
def calculate_statistics(patients: list[dict]) -> dict:
    """Compute aggregate statistics over a list of patients.

    Args:
        patients: A list of patient dicts (must include "age" and
            "temperature").

    Returns:
        dict: total_patients, average_age, average_temperature.
    """
    total_patients = len(patients)
    average_age = sum(p["age"] for p in patients) / total_patients
    average_temperature = sum(p["temperature"] for p in patients) / total_patients

    return {
        "total_patients": total_patients,
        "average_age": average_age,
        "average_temperature": average_temperature,
    }


# ═══════════════════════════════════════════
# FILTER
# ═══════════════════════════════════════════
def filter_by_temperature(patients: list[dict], threshold: float) -> list[dict]:
    """Return patients whose temperature is at or above a threshold.

    Args:
        patients: A list of patient dicts (must include "temperature").
        threshold: Minimum temperature (inclusive) to be included.

    Returns:
        list[dict]: Matching patient records.
    """
    return [p for p in patients if p["temperature"] >= threshold]


def filter_by_diagnosis(patients: list[dict], diagnosis: str) -> list[dict]:
    """Return patients matching a given diagnosis (case-insensitive).

    Mirrors filter_by_temperature() for symmetry — same shape,
    different field.

    Args:
        patients: A list of patient dicts (must include "diagnosis").
        diagnosis: The diagnosis to match.

    Returns:
        list[dict]: Matching patient records.
    """
    return [p for p in patients if p["diagnosis"].lower() == diagnosis.lower()]


# ═══════════════════════════════════════════
# GENERATE REPORT — two formats, same source data
# ═══════════════════════════════════════════
def generate_text_report(
    stats: dict,
    high_temp_patients: list[dict],
    sinusitis_patients: list[dict],
) -> str:
    """Build a human-readable text report.

    Args:
        stats: Output of calculate_statistics().
        high_temp_patients: Output of filter_by_temperature().
        sinusitis_patients: Output of filter_by_diagnosis().

    Returns:
        str: The full report text.
    """
    title = "MEDASSISTANT PATIENT REPORT"

    high_temp_names = ", ".join(p["name"] for p in high_temp_patients) or "none"
    sinusitis_names = ", ".join(p["name"] for p in sinusitis_patients) or "none"

    return (
        f"{title}\n"
        f"{'=' * len(title)}\n\n"
        f"Total patients: {stats['total_patients']}\n"
        f"Average age: {stats['average_age']:.1f}\n"
        f"Average temperature: {stats['average_temperature']:.1f}\n\n"
        f"Patients with temperature >= 38.0: {high_temp_names}\n"
        f"Patients with sinusitis: {sinusitis_names}\n"
    )


def generate_json_report(
    stats: dict,
    high_temp_patients: list[dict],
    sinusitis_patients: list[dict],
) -> dict:
    """Build a machine-readable JSON-ready report.

    Args:
        stats: Output of calculate_statistics().
        high_temp_patients: Output of filter_by_temperature().
        sinusitis_patients: Output of filter_by_diagnosis().

    Returns:
        dict: The report data, ready for json.dump().
    """
    return {
        "total_patients": stats["total_patients"],
        "average_age": round(stats["average_age"], 1),
        "average_temperature": round(stats["average_temperature"], 1),
        "high_temperature_patients": [p["name"] for p in high_temp_patients],
        "sinusitis_patients": [p["name"] for p in sinusitis_patients],
    }


# ═══════════════════════════════════════════
# SAVE — one function, dispatches on report type
# ═══════════════════════════════════════════
def save_report(path: str, report: str | dict) -> None:
    """Save a report to disk, as plain text or JSON.

    A str report is written as-is; a dict report is serialized
    with json.dump(). This keeps ONE save function instead of two
    near-identical ones (DRY).

    Args:
        path: Destination file path.
        report: The report content — str for text, dict for JSON.
    """
    with open(path, "w", encoding="utf-8") as file:
        if isinstance(report, dict):
            json.dump(report, file, indent=2, ensure_ascii=False)
        else:
            file.write(report)


# ═══════════════════════════════════════════
# MAIN — orchestrates the pipeline, no logic of its own
# ═══════════════════════════════════════════
def main() -> None:
    patients = load_patients("data/medassistant_patients.json")
    if patients is None:
        return   # error already reported by load_patients()

    stats = calculate_statistics(patients)
    high_temp_patients = filter_by_temperature(patients, threshold=38.0)
    sinusitis_patients = filter_by_diagnosis(patients, diagnosis="sinusitis")

    text_report = generate_text_report(stats, high_temp_patients, sinusitis_patients)
    json_report = generate_json_report(stats, high_temp_patients, sinusitis_patients)

    save_report("data/medassistant_report.txt", text_report)
    save_report("data/medassistant_report.json", json_report)

    # --- Verify by reading both back and printing ---
    with open("data/medassistant_report.txt", "r", encoding="utf-8") as file:
        saved_text = file.read()

    lines = saved_text.rstrip("\n").split("\n")
    width = max(len(line) for line in lines) + 4

    print("\n┌" + "─" * width + "┐")
    print("│" + "  data/medassistant_report.txt".center(width) + "│")
    print("├" + "─" * width + "┤")
    for line in lines:
        print("│  " + line.ljust(width - 2) + "│")
    print("└" + "─" * width + "┘")

    print(f"\ndata/medassistant_report.json:\n{json.dumps(json_report, indent=2)}")


if __name__ == "__main__":
    main()

"""
┌────────────────────────────────────────────┐
│         data/medassistant_report.txt       │
├────────────────────────────────────────────┤
│  MEDASSISTANT PATIENT REPORT               │
│  ===========================               │
│                                            │
│  Total patients: 3                         │
│  Average age: 46.0                         │
│  Average temperature: 37.5                 │
│                                            │
│  Patients with temperature >= 38.0: Petro  │
│  Patients with sinusitis: Ivan, Petro      │
└────────────────────────────────────────────┘

data/medassistant_report.json:
{
  "total_patients": 3,
  "average_age": 46.0,
  "average_temperature": 37.5,
  "high_temperature_patients": [
    "Petro"
  ],
  "sinusitis_patients": [
    "Ivan",
    "Petro"
  ]
}
"""

"""
#*Чому процес побудовано саме так — пояснення кожного етапу:
load_patients()          → list[dict] | None    (зчитує файл, обробляє помилки вводу-виводу)
calculate_statistics()   → dict                 (чисті обчислення, без вводу-виводу, без виведення на екран)
filter_by_temperature()  → list[dict]           (чистий фільтр, шаблон, запозичений із Завдання 3)
filter_by_diagnosis()    → list[dict]           (така сама структура, як вище — симетрія, а не дублювання)
generate_text_report()   → str                  (чисте форматування, без доступу до файлів)
generate_json_report()   → dict                 (чисте форматування, без доступу до файлів)
save_report()            → None                 (ЄДИНА функція, яка записує на диск)
main()                   → лише координує, сама не містить бізнес-логіки

#*Чому функція filter_by_diagnosis() повторює структуру filter_by_temperature(), замість того щоб написати вбудований вираз:
# Both follow the exact same shape:
def filter_by_temperature(patients, threshold):
    return [p for p in patients if p["temperature"] >= threshold]

def filter_by_diagnosis(patients, diagnosis):
    return [p for p in patients if p["diagnosis"].lower() == diagnosis.lower()]

Це не просто стиль — це означає, що будь-який майбутній фільтр (за іменем, за віковим діапазоном, за відділом) може дотримуватися того самого, передбачуваного однорядкового шаблону. Читач, який розуміє одну функцію фільтрації, одразу розуміє їх усі. Вбудований вираз у функції calculate_statistics() також працював би, але це розмило б єдину відповідальність цієї функції (обчислення статистики) з не пов’язаною з нею (фільтрування) — змішуючи аспекти, які згодом доведеться змінювати незалежно один від одного.

#*Чому save_report() є ОДНІЄЮ функцією, а не save_text_report() + save_json_report():
def save_report(path, report):
    with open(path, "w", encoding="utf-8") as file:
        if isinstance(report, dict):
            json.dump(report, file, ...)
        else:
            file.write(report)

Каркас завдання називає саме одну функцію save_report(path, report) — і обидва типи звітів мають одну й ту саму базову дію («відкрити цей шлях, записати цей вміст»). Використання розгалуження на основі функції isinstance() всередині однієї функції дозволяє зберегти цю єдину дію в одному місці (DRY), замість того, щоб дублювати шаблонний код with open(...) у двох майже ідентичних функціях.

#*Чому функція main() не містить жодної логіки обчислення чи форматування:
def main():
    patients = load_patients(...)
    if patients is None:
        return
    stats = calculate_statistics(patients)
    ...

Функція main() виконує роль змісту для всього конвеєра — будь-хто, хто вперше знайомиться з кодом, може прочитати ці вісім рядків і зрозуміти весь хід роботи програми, не заглиблюючись у деталі реалізації. Кожен фактичний обчислювальний процес реалізовано у функції, назва якої вже вказує на її призначення.
"""
