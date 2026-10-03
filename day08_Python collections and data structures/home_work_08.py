"""
## !🧠 Challenge №1!

Не запускаючи код:
a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)
print(a is b)

Що буде?
"""

"""
*Прогноз результату:
[1, 2, 3, 4]
[1, 2, 3, 4]
True

*Покрокове виконання:
a = [1, 2, 3]   # створюється список у пам'яті, a вказує на нього
b = a           # b НЕ копіює список — просто починає вказувати
                #   на ТОЙ САМИЙ об'єкт, що й a

b.append(4)     # append() ЗМІНЮЄ об'єкт "на місці" (in-place),
                #   а НЕ створює новий список

print(a)        # [1, 2, 3, 4]  ← a ТЕЖ бачить зміну!
print(b)        # [1, 2, 3, 4]
print(a is b)   # True — це доводить, що a і b — ОДИН і той самий об'єкт

*Чому так — пряме продовження Практики №8:
b = a
#     ↑
# це "друге ім'я" для ТОГО САМОГО об'єкта, а не копія
# (те саме, що b = a, а НЕ b = a.copy() і НЕ b = deepcopy(a))

append() — метод, який мутує (змінює вміст) список, а не створює новий. Оскільки a і b — це два імені, що вказують на один і той самий список у пам'яті, зміна через будь-яке з цих імен видно через обидва:
id(a) == id(b)   # True — той самий об'єкт

*Ключова відмінність від Challenge №1 попереднього дня (a = 5; b = a; b = 10):
# Той приклад — числа (immutable):
a = 5
b = a
b = 10          # ← ПЕРЕПРИЗНАЧЕННЯ b на НОВИЙ об'єкт 10
print(a)        # 5 — a НЕ змінився!

# Цей приклад — списки (mutable):
a = [1, 2, 3]
b = a
b.append(4)     # ← МУТАЦІЯ існуючого об'єкта, а НЕ перепризначення
print(a)        # [1, 2, 3, 4] — a ЗМІНИВСЯ!

Різниця не в тому, що "списки поводяться інакше за числа" загалом — різниця в тому, що саме відбувається: b = 10 створює новий об'єкт і переприв'язує до нього b, а b.append(4) змінює вміст об'єкта, на який b (і одночасно a) вказує, не створюючи нічого нового.

*Практичний висновок — та сама пастка, що й у mutable default argument (Challenge №2 з функцій):
# Якщо ти "думаєш", що робиш копію, а насправді просто передаєш посилання —
# зміни "просочуються" туди, де їх не очікували:

original_patients = ["Ivan", "Olena"]
temp_list = original_patients   # ← ЦЕ НЕ КОПІЯ!
temp_list.append("Petro")

print(original_patients)   # ["Ivan", "Olena", "Petro"] ← несподівано змінився!

# Правильно, якщо потрібна НЕЗАЛЕЖНА копія:
temp_list = original_patients.copy()   # або list(original_patients)
"""

# ==============================================================================
# ==============================================================================

"""
## !🧠 Challenge №2!

Що відбудеться?
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
print(b)
print(a is b)
"""

"""
*Прогноз результату:
[1, 2, 3]
[1, 2, 3, 4]
False

*Покрокове виконання:
a = [1, 2, 3]
b = a.copy()    # .copy() створює НОВИЙ, окремий список
                #   з тим самим ВМІСТОМ, що й у a

b.append(4)     # append() змінює лише b — новий, незалежний об'єкт

print(a)        # [1, 2, 3]     ← a НЕ ЗМІНИВСЯ!
print(b)        # [1, 2, 3, 4]  ← змінився тільки b
print(a is b)   # False — це РІЗНІ об'єкти в пам'яті

*Чому результат ІНШИЙ, ніж у Challenge №1:
# Challenge №1:
b = a            # b — ДРУГЕ ІМ'Я для ТОГО САМОГО об'єкта
id(a) == id(b)   # True

# Challenge №2:
b = a.copy()     # b — НОВИЙ, окремий об'єкт з копійованим вмістом
id(a) == id(b)   # False

*Різниця саме тут: 
a.copy() виділяє нову ділянку пам'яті для списку b, копіює туди значення з a (1, 2, 3), і від цього моменту a та b — це два цілком незалежні списки. append(4) на b більше ніяк не пов'язаний з a.

*Чому цей результат не суперечить "пастці" з Практики №8 (поверхневе копіювання):
# Практика №8 показувала ПАСТКУ для ВКЛАДЕНИХ списків:
a = [[1, 2], [3, 4]]
b = a.copy()
b[0][0] = 99       # ← ЗМІНА ВКЛАДЕНОГО елемента (мутація існуючого підсписку)
print(a)           # [[99, 2], [3, 4]]  ← a ТЕЖ змінився! (спільний вкладений об'єкт)

# Цей Challenge — ПЛОСКИЙ список чисел, append() на ЗОВНІШНЬОМУ рівні:
a = [1, 2, 3]
b = a.copy()
b.append(4)         # ← ЗМІНА ЗОВНІШНЬОГО списка b (append додає елемент у b)
print(a)             # [1, 2, 3]  ← a НЕ змінився (append не чіпає a взагалі)

*Ключове правило .copy() (поверхнева копія):
.copy() створює новий зовнішній контейнер. Усе, що відбувається на рівні цього контейнера (додавання/видалення елементів через append(), remove(), pop()) — не впливає на оригінал, бо контейнери різні. Пастка виникає лише тоді, коли елементи всередині — самі є mutable-об'єктами (списками, словниками), і ти змінюєш їхній вміст, а не сам зовнішній контейнер.

*Підсумкова таблиця для цих двох Challenge поспіль:
Дія	                b = a	              b = a.copy() (плоский список)
b.append(4)     	✅ впливає на a	    ❌ НЕ впливає на a
— додати елемент
a is b	            True	              False

Це підтверджує головний висновок Практики №8: .copy() достатньо безпечний для плоских (одновимірних) списків, і небезпечний лише для вкладених структур — де потрібен саме deepcopy().
"""

# ==============================================================================
# ==============================================================================

"""
## !🧠 Challenge №3!

Що буде?
data = {
    "patient": {
        "name": "Ivan",
        "age": 42,
    }
}

print(data["patient"]["name"])

Поясни, як Python знаходить "Ivan".
"""

"""
Результат: буде виведено: Ivan

*Як Python "знаходить" "Ivan" — покроково, шар за шаром:
data = {
    "patient": {
        "name": "Ivan",
        "age": 42,
    }
}

data["patient"]["name"]

*Python обробляє це зліва направо, кожні квадратні дужки — окрема, самостійна операція:
# Крок 1: data["patient"]
data["patient"]
# → Python шукає в data КЛЮЧ "patient"
# → знаходить значення: {"name": "Ivan", "age": 42}
# → це ЦІЛИЙ окремий словник (проміжний результат)

# Крок 2: [результат кроку 1]["name"]
{"name": "Ivan", "age": 42}["name"]
# → Python шукає в ЦЬОМУ словнику КЛЮЧ "name"
# → знаходить значення: "Ivan"

# Фінальний результат: "Ivan"

Візуально, "розбираючи" вираз по шарах:
data["patient"]["name"]
└──────┬──────┘└──┬───┘
   крок 1         крок 2
   (dict → dict)  (dict → str)

Це та сама механіка, яку ми розбирали в Практиці №7 (nested dictionary) — там patient["measurements"]["temperature"] працює точно так само: перші дужки дістають вкладений словник, другі дужки дістають значення всередині нього.

*Важливо розуміти: 
це НЕ "магічний одноразовий пошук у глибину" — це послідовність простих, незалежних кроків, де результат кожного кроку стає вхідними даними для наступного:

# Можна переписати "по кроках" з проміжними змінними —
# результат БУДЕ ТОЧНО ТАКИЙ САМИЙ:
step1 = data["patient"]         # {"name": "Ivan", "age": 42}
step2 = step1["name"]           # "Ivan"

print(step2)   # Ivan — те саме, що data["patient"]["name"]

*Що станеться, якщо один із ключів відсутній — де саме "зламається":
data["patient"]["diagnosis"]
# Крок 1: data["patient"] → {"name": "Ivan", "age": 42}  ✅ успішно
# Крок 2: {...}["diagnosis"] → 💥 KeyError: 'diagnosis'
#         (бо "diagnosis" немає в результаті кроку 1)

data["symptoms"]["name"]
# Крок 1: data["symptoms"] → 💥 KeyError: 'symptoms'
#         (навіть до кроку 2 не доходить — впаде одразу тут)

*Зв'язок із Практикою №4 (get()): 
саме тому для вкладених структур, де якийсь рівень може бути відсутнім, 
безпечніше писати ланцюжок через .get():

data.get("patient", {}).get("diagnosis", "Unknown")
# Крок 1: {"name": "Ivan", "age": 42}   (є "patient", тому продовжуємо)
# Крок 2: "Unknown"  (немає "diagnosis" — але ЗАМІСТЬ КРАХУ повертається дефолт)
"""

# ==============================================================================
# ==============================================================================

"""
## !🧠 Challenge №4!

Що буде?
symptoms = {"fever", "cough", "fever"}

print(len(symptoms))
Чому?
"""

"""
*Результат: буде виведено: 2

*Чому саме 2, а не 3:
symptoms = {"fever", "cough", "fever"}
#            ↑         ↑        ↑
#         елемент 1  елемент 2  ПОВТОР елемента 1

# set() (множина) НІКОЛИ не зберігає дублікати —
# навіть якщо ти "написав" однакове значення двічі при СТВОРЕННІ,
# Python автоматично залишає лише ОДНЕ входження

print(symptoms)   # → {"fever", "cough"}   ← лише 2 УНІКАЛЬНІ елементи
print(len(symptoms))   # → 2

*Це відбувається вже НА ЕТАПІ СТВОРЕННЯ множини, а не пізніше:
# Написати {"fever", "cough", "fever"} — те саме, що:
symptoms = set()
symptoms.add("fever")    # додано: {"fever"}
symptoms.add("cough")    # додано: {"fever", "cough"}
symptoms.add("fever")    # "fever" ВЖЕ Є → нічого не змінюється
# результат: {"fever", "cough"}

*Пряме продовження Практики №5 (Set):
# Той самий принцип, що вже бачив із list → set:
diagnoses = ["sinusitis", "rhinitis", "sinusitis", "otitis", "rhinitis"]
set(diagnoses)   # → {"sinusitis", "rhinitis", "otitis"}  (3 унікальних)

# Тут — те саме, лише синтаксис ІНШИЙ:
# фігурні дужки {} з елементами через кому СТВОРЮЮТЬ set НАПРЯМУ,
# без потреби спершу робити list і потім обгортати в set()
{"fever", "cough", "fever"}   # → {"fever", "cough"}  (2 унікальних)

*Важливий синтаксичний нюанс — не плутай із dict:
{"fever", "cough"}            # set — просто ЗНАЧЕННЯ через кому
{"fever": 1, "cough": 2}      # dict — ПАРИ ключ:значення через двокрапку
{}                            # ⚠️ ПОРОЖНІ фігурні дужки — це ЗАВЖДИ dict, НЕ set!
                               #    для порожнього set потрібно писати set()

*Ця остання деталь — часта пастка новачків: 
{} виглядає як "порожня множина", але Python інтерпретує його як порожній словник. Щоб створити порожню множину, обов'язково потрібен виклик set().

*Чому ЦЕ важливо на практиці — типовий сценарій:
# Якщо збираєш симптоми з кількох джерел (наприклад, від різних лікарів),
# і один симптом міг бути записаний ДВІЧІ — set() автоматично прибере дублі,
# і len() покаже РЕАЛЬНУ кількість УНІКАЛЬНИХ симптомів, а не записів:

reported_symptoms = {"fever", "cough", "fever", "pain", "cough"}
print(f"Унікальних симптомів: {len(reported_symptoms)}")   # 3, а не 5
"""

# ==============================================================================
# ==============================================================================

"""
🚀 Challenge №5 — MedAssistant

Створи:
patients = [
    {
        "name": "Ivan",
        "temperature": 36.6,
    },
    {
        "name": "Olena",
        "temperature": 38.2,
    },
    {
        "name": "Petro",
        "temperature": 39.1,
    },
]

За допомогою comprehension створи:
{
    "Ivan": "normal",
    "Olena": "fever",
    "Petro": "high_fever",
}

Використай твою функцію:
classify_temperature()

із попередніх днів.

Тут об'єднаються:
list
+
dict
+
dict comprehension
+
function
"""

"""patient_status_map.py

Combines list + dict + dict comprehension + function into a single
pipeline for MedAssistant: raw patient records → a name-to-status map.
"""


def classify_temperature(temp: float) -> str:
    """Classify a single body temperature reading.

    (Reused from earlier MedAssistant challenges — not duplicated.)
    """
    if temp < 37.5:
        return "normal"
    elif temp < 39.0:
        return "fever"
    else:
        return "high_fever"


patients = [
    {"name": "Ivan", "temperature": 36.6},
    {"name": "Olena", "temperature": 38.2},
    {"name": "Petro", "temperature": 39.1},
]

# --- Variant 1: one-line dict comprehension ---
status_map_v1 = {
    patient["name"]: classify_temperature(patient["temperature"])
    for patient in patients
}


# --- Variant 2: wrapped in a named function ---
def build_patient_status_map(patients: list[dict]) -> dict:
    """Build a {name: status} map from a list of patient records.

    Args:
        patients: A list of dicts, each with "name" and "temperature".

    Returns:
        dict: Patient name mapped to its temperature category.
    """
    return {
        patient["name"]: classify_temperature(patient["temperature"])
        for patient in patients
    }


status_map_v2 = build_patient_status_map(patients)

# --- Framed output ---
lines = [f"{name:<8} → {status}" for name, status in status_map_v1.items()]
width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  PATIENT STATUS MAP".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

print(f"\nstatus_map_v1 == status_map_v2: {status_map_v1 == status_map_v2}")

"""
┌─────────────────────────┐
│     PATIENT STATUS MAP  │
├─────────────────────────┤
│  Ivan     → normal      │
│  Olena    → fever       │
│  Petro    → high_fever  │
└─────────────────────────┘

status_map_v1 == status_map_v2: True
"""

"""
#*Розбір виразу dict comprehension — пояснення кожного елемента:
{
    patient["name"]: classify_temperature(patient["temperature"])
    for patient in patients
}
#  ↑                  ↑                                 ↑
# key                value                          iterate over
# (name field)   (call the function, using           the LIST of dicts
#                 the temperature field)

#*Усе, що тут поєднується, відповідає чотирьом елементам, зазначеним у назві завдання:
patients                                   # ← list of dicts (the LIST)
patients[0]                                # ← {"name": "Ivan", "temperature": 36.6}  (a DICT)
patient["temperature"]                     # ← reading a value OUT of that dict
classify_temperature(patient["temperature"])  # ← calling a FUNCTION with it
{k: v for ... in ...}                      # ← DICT COMPREHENSION building the final result

#*Покрокова інструкція для заданого вхідного значення:
patients = [
    {"name": "Ivan", "temperature": 36.6},
    {"name": "Olena", "temperature": 38.2},
    {"name": "Petro", "temperature": 39.1},
]

# Iteration 1: patient = {"name": "Ivan", "temperature": 36.6}
#   key   = patient["name"]                     → "Ivan"
#   value = classify_temperature(36.6)          → "normal"

# Iteration 2: patient = {"name": "Olena", "temperature": 38.2}
#   key   = "Olena"
#   value = classify_temperature(38.2)          → "fever"

# Iteration 3: patient = {"name": "Petro", "temperature": 39.1}
#   key   = "Petro"
#   value = classify_temperature(39.1)          → "high_fever"

# result:
{"Ivan": "normal", "Olena": "fever", "Petro": "high_fever"}

#*Чому функцію `classify_temperature()` використовують повторно, а не створюють її дублікат 
(за тим самим принципом DRY, що й у всіх попередніх завданнях):
{
    patient["name"]: classify_temperature(patient["temperature"])
    #                 ↑
    #     calls the SAME function that already knows the thresholds —
    #     this comprehension never rewrites "< 37.5 / < 39.0" itself
    for patient in patients
}

Якщо завтра поріг температури зміниться, редагувати потрібно лише у функції classify_temperature() — цей вираз (comprehension), функції analyze_patients(), classify_all() та всі інші функції, створені в рамках цих завдань, автоматично залишаться правильними.
"""

# ==============================================================================
# ==============================================================================

"""
## !🚀 Challenge №6 — Junior+!

Створи:
def group_patients_by_status(
    patients: list[dict],
) -> dict[str, list[str]]:
    ...

Вхід:
patients = [
    {"name": "Ivan", "temperature": 36.6},
    {"name": "Olena", "temperature": 38.2},
    {"name": "Petro", "temperature": 39.1},
    {"name": "Hanna", "temperature": 37.0},
]

Результат:
{
    "normal": ["Ivan", "Hanna"],
    "fever": ["Olena"],
    "high_fever": ["Petro"],
}

Не дублюй температурні пороги.

Використай:
classify_temperature()
"""

def classify_temperature(temp: float) -> str:
    """Classify a single body temperature reading.

    (Reused from earlier MedAssistant challenges — not duplicated.)
    """
    if temp < 37.5:
        return "normal"
    elif temp < 39.0:
        return "fever"
    else:
        return "high_fever"


def group_patients_by_status(patients: list[dict]) -> dict[str, list[str]]:
    """Group patient names by their temperature category.

    Reuses classify_temperature() for the classification logic —
    this function's only job is grouping names, not re-deciding
    the thresholds.

    Args:
        patients: A list of dicts, each with "name" and "temperature".

    Returns:
        dict[str, list[str]]: All three category keys always present
            (empty list if unused), each mapped to the names of
            patients that fall into it.
    """
    groups: dict[str, list[str]] = {"normal": [], "fever": [], "high_fever": []}

    for patient in patients:
        status = classify_temperature(patient["temperature"])   # ← reused, not duplicated
        groups[status].append(patient["name"])

    return groups


# --- Demo ---
patients = [
    {"name": "Ivan", "temperature": 36.6},
    {"name": "Olena", "temperature": 38.2},
    {"name": "Petro", "temperature": 39.1},
    {"name": "Hanna", "temperature": 37.0},
]

result = group_patients_by_status(patients)

# --- Framed table output ---
MARKER = {"normal": "🟢", "fever": "🟡", "high_fever": "🔴"}

lines = [
    f"{MARKER[status]} {status:<10} → {names}"
    for status, names in result.items()
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  PATIENTS GROUPED BY STATUS".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────────────────────┐
│      PATIENTS GROUPED BY STATUS    │
├────────────────────────────────────┤
│  🟢 normal     → ['Ivan', 'Hanna'] │
│  🟡 fever      → ['Olena']         │
│  🔴 high_fever → ['Petro']         │
└────────────────────────────────────┘
"""

"""
#*Чому функція group_patients_by_status() ніколи не створює дублікатів порогових значень температури:
def group_patients_by_status(patients):
    groups = {"normal": [], "fever": [], "high_fever": []}
    for patient in patients:
        status = classify_temperature(patient["temperature"])   # ← CALL, not reimplementation
        groups[status].append(patient["name"])
    return groups

Ця функція ніде не записує значення, якщо temp < 37,5 — вона лише запитує у функції classify_temperature(): «До якої категорії належить це значення?», і використовує відповідь як ключ словника, щоб визначити, до якого списку додати ім’я. Це відповідає принципу DRY, як і у функціях-побратимах analyze_patients() та group_patients_by_status() у всіх попередніх завданнях.

#*Порівняння цього завдання з попередньою функцією analyze_patients() (завдання №6, попередній набір):
# analyze_patients() — COUNTS how many per category:
groups["normal"] += 1        # → {"normal": 2, "fever": 1, "high_fever": 1}

# group_patients_by_status() — COLLECTS the actual NAMES per category:
groups["normal"].append(name)   # → {"normal": ["Ivan", "Hanna"], "fever": [...], ...}

Загальна структура така сама (ініціалізація словника з усіма трьома ключами, цикл, пошук ключа за допомогою функції classify_temperature()), але замість += 1 для цілочисельного лічильника використовується .append(name) для списку — адже цього разу мета полягає в тому, щоб дізнатися, хто входить до кожної групи, а не лише скільки людей у ній.

#*Чому всі три ключі попередньо ініціалізовано порожніми списками:
groups = {"normal": [], "fever": [], "high_fever": []}

Це гарантує, що групи[«high_fever»] завжди є дійсним списком — навіть [], якщо у жодного пацієнта не було високої температури, — тому код, що його викликає, ніколи не повинен перевіряти наявність значення «high_fever» у групах перед його використанням.
"""

# ==============================================================================
# ==============================================================================

"""
## !🚀 Challenge №7 — Junior+!

Створи:
def get_unique_symptoms(
    patients: list[dict],
) -> set[str]:
    ...

Вхід:
patients = [
    {
        "name": "Ivan",
        "symptoms": ["fever", "cough"],
    },
    {
        "name": "Olena",
        "symptoms": ["cough", "pain"],
    },
    {
        "name": "Petro",
        "symptoms": ["fever", "pain"],
    },
]

Результат:
{
    "fever",
    "cough",
    "pain",
}

Тут тренуємо:
nested structures
+
for
+
set
+
set.add()
"""

def get_unique_symptoms(patients: list[dict]) -> set[str]:
    """Збирає всі УНІКАЛЬНІ симптоми з усіх пацієнтів.

    Кожен пацієнт має ВКЛАДЕНИЙ список симптомів (nested structure).
    Проходимо по пацієнтах (зовнішній for), потім по симптомах
    КОЖНОГО пацієнта (внутрішній for), і додаємо кожен симптом
    у set через .add() — set сам подбає про унікальність.
    """
    unique_symptoms = set()   # порожня множина — стартова точка

    for patient in patients:            # зовнішній цикл: по кожному пацієнту
        for symptom in patient["symptoms"]:   # внутрішній цикл: по його симптомах
            unique_symptoms.add(symptom)       # додаємо в set (дублі ігноруються)

    return unique_symptoms


# --- Альтернативний, коротший варіант: set comprehension ---
def get_unique_symptoms_comprehension(patients: list[dict]) -> set[str]:
    """Той самий результат — одним рядком через nested set comprehension."""
    return {
        symptom
        for patient in patients
        for symptom in patient["symptoms"]
    }


# --- Демонстрація ---
patients = [
    {"name": "Ivan", "symptoms": ["fever", "cough"]},
    {"name": "Olena", "symptoms": ["cough", "pain"]},
    {"name": "Petro", "symptoms": ["fever", "pain"]},
]

result_for_loop = get_unique_symptoms(patients)
result_comprehension = get_unique_symptoms_comprehension(patients)

# --- Вивід у рамці ---
lines = [
    f"for + set.add():        {result_for_loop}",
    f"set comprehension:      {result_comprehension}",
    f"Однакові результати?    {result_for_loop == result_comprehension}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  УНІКАЛЬНІ СИМПТОМИ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌──────────────────────────────────────────────────────┐
│                   УНІКАЛЬНІ СИМПТОМИ                 │
├──────────────────────────────────────────────────────┤
│  for + set.add():        {'cough', 'pain', 'fever'}  │
│  set comprehension:      {'cough', 'pain', 'fever'}  │
│  Однакові результати?    True                        │
└──────────────────────────────────────────────────────┘
"""

"""
*Пояснення вкладених циклів (nested for) над вкладеною структурою:
patients = [
    {"name": "Ivan",  "symptoms": ["fever", "cough"]},
    {"name": "Olena", "symptoms": ["cough", "pain"]},
    {"name": "Petro", "symptoms": ["fever", "pain"]},
]

for patient in patients:                    # 1) для КОЖНОГО пацієнта (dict)
    for symptom in patient["symptoms"]:     # 2) для КОЖНОГО симптому ЦЬОГО пацієнта
        unique_symptoms.add(symptom)        # 3) додаємо ОДИН симптом у set

*Крок за кроком, що відбувається:
unique_symptoms = set()

# patient = {"name": "Ivan", "symptoms": ["fever", "cough"]}
#   symptom = "fever" → add("fever") → {"fever"}
#   symptom = "cough" → add("cough") → {"fever", "cough"}

# patient = {"name": "Olena", "symptoms": ["cough", "pain"]}
#   symptom = "cough" → add("cough") → вже Є, нічого не змінюється
#   symptom = "pain"  → add("pain")  → {"fever", "cough", "pain"}

# patient = {"name": "Petro", "symptoms": ["fever", "pain"]}
#   symptom = "fever" → вже Є
#   symptom = "pain"  → вже Є

# Фінал: {"fever", "cough", "pain"}

*Пояснення .add() — метод для ОДНОГО елемента:
unique_symptoms = set()
unique_symptoms.add("fever")   # додає ОДИН елемент
# порівняй з .update(), який додає ОДРАЗУ КІЛЬКА:
unique_symptoms.update(["cough", "pain"])   # додає ОДРАЗУ список елементів

Тут ми проходимо по одному симптому за раз (внутрішній for), тому .add() — правильний вибір; якби ми мали одразу цілий список симптомів пацієнта, простіше було б .update(patient["symptoms"]) замість внутрішнього циклу.

*Nested set comprehension — той самий подвійний for, компактніше:
{
    symptom                          # ← що зберігаємо
    for patient in patients          # ← зовнішній for (як у звичайному коді)
    for symptom in patient["symptoms"]  # ← внутрішній for (одразу після зовнішнього!)
}

Порядок for у comprehension точно повторює порядок вкладених циклів у звичайному коді — зовнішній for пишеться першим, внутрішній — другим, зліва направо, так само, як вони були б вкладені один в одного у класичному записі.

*Зв'язок із попередніми задачами: 
це поєднання трьох навичок одразу: 
- доступ до вкладеної структури (patient["symptoms"], як у Практиці №7 nested dict), 
- унікальність через set (Практика №5-6), 
- подвійна ітерація (нова навичка — цикл всередині циклу, коли кожен зовнішній елемент сам містить колекцію для обходу).
"""

# ==============================================================================
# ==============================================================================

"""
## !🔥 Challenge №8 — найважливіше сьогодні!

Зроби дві версії:
Version A
def group_patients_by_status(...)

через звичайний for.

Version B
Спробуй максимально використати:
dict;
setdefault();
comprehension там, де це справді читабельно.

Порівняй обидва варіанти.
Тут мене цікавитиме вже не лише "працює / не працює", а чому ти вибрав саме таку структуру даних.
"""

def classify_temperature(temp: float) -> str:
    """Класифікує одне значення температури."""
    if temp < 37.5:
        return "normal"
    elif temp < 39.0:
        return "fever"
    else:
        return "high_fever"


patients = [
    {"name": "Ivan", "temperature": 36.6},
    {"name": "Olena", "temperature": 38.2},
    {"name": "Petro", "temperature": 39.1},
    {"name": "Hanna", "temperature": 37.0},
]


# ═══════════════════════════════════════════
# VERSION A — звичайний for, dict з заготовленими ключами
# ═══════════════════════════════════════════
def group_patients_by_status_a(patients: list[dict]) -> dict[str, list[str]]:
    """Групує пацієнтів за статусом. Ключі dict — ЗАЗДАЛЕГІДЬ відомі."""
    groups = {"normal": [], "fever": [], "high_fever": []}

    for patient in patients:
        status = classify_temperature(patient["temperature"])
        groups[status].append(patient["name"])

    return groups


# ═══════════════════════════════════════════
# VERSION B — dict.setdefault(), без заздалегідь відомих ключів
# ═══════════════════════════════════════════
def group_patients_by_status_b(patients: list[dict]) -> dict[str, list[str]]:
    """Групує пацієнтів за статусом. Ключі dict СТВОРЮЮТЬСЯ по мірі появи."""
    groups: dict[str, list[str]] = {}

    for patient in patients:
        status = classify_temperature(patient["temperature"])
        # setdefault(ключ, дефолт) — якщо ключа НЕМАЄ, створює його
        # зі значенням дефолт і одразу ПОВЕРТАЄ це значення (готовий список)
        groups.setdefault(status, []).append(patient["name"])

    return groups


# --- Демонстрація ---
result_a = group_patients_by_status_a(patients)
result_b = group_patients_by_status_b(patients)

# --- Вивід у рамці ---
lines = [
    "Version A (for + заздалегідь готовий dict):",
    f"  {result_a}",
    "─" * 60,
    "Version B (for + setdefault()):",
    f"  {result_b}",
    "─" * 60,
    f"Результати однакові? {result_a == result_b}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  VERSION A vs VERSION B".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────────────────────────────────────────────────────────────────┐
│                              VERSION A vs VERSION B                            │
├────────────────────────────────────────────────────────────────────────────────┤
│  Version A (for + заздалегідь готовий dict):                                   │
│    {'normal': ['Ivan', 'Hanna'], 'fever': ['Olena'], 'high_fever': ['Petro']}  │
│  ────────────────────────────────────────────────────────────                  │
│  Version B (for + setdefault()):                                               │
│    {'normal': ['Ivan', 'Hanna'], 'fever': ['Olena'], 'high_fever': ['Petro']}  │
│  ────────────────────────────────────────────────────────────                  │
│  Результати однакові? True                                                     │
└────────────────────────────────────────────────────────────────────────────────┘
"""

"""
*Пояснення setdefault() — крок за кроком:
groups = {}
groups.setdefault("normal", []).append("Ivan")
#         ↑          ↑          ↑
#       ключ      дефолт    метод НА РЕЗУЛЬТАТІ setdefault()

# Що робить setdefault("normal", []):
# 1. Якщо "normal" ВЖЕ Є в groups → повертає ІСНУЮЧЕ значення (не чіпає його)
# 2. Якщо "normal" НЕМАЄ в groups → СТВОРЮЄ groups["normal"] = [] і повертає []

# В обох випадках повертається СПИСОК, на якому одразу викликається .append()

*Крок за кроком для наших даних:
groups = {}

# patient = Ivan, status = "normal"
groups.setdefault("normal", [])   # "normal" немає → створює groups = {"normal": []}
                                    # повертає []
groups["normal"].append("Ivan")    # groups = {"normal": ["Ivan"]}

# patient = Olena, status = "fever"
groups.setdefault("fever", [])     # "fever" немає → створює groups["fever"] = []
groups["fever"].append("Olena")     # groups = {"normal": ["Ivan"], "fever": ["Olena"]}

# patient = Petro, status = "high_fever"
groups.setdefault("high_fever", []) # створює новий ключ
groups["high_fever"].append("Petro")

# patient = Hanna, status = "normal"
groups.setdefault("normal", [])     # "normal" ВЖЕ Є → повертає ІСНУЮЧИЙ список ["Ivan"]
groups["normal"].append("Hanna")    # groups["normal"] = ["Ivan", "Hanna"]

*Порівняння Version A vs Version B — і чому я обрав структуру даних саме так
                        ###Головна структурна відмінність:###
	                    Version A	                      Version B
Ключі dict	            відомі заздалегідь 	              невідомі заздалегідь 
                        (normal/fever/high_fever)         (з'являються по ходу виконання)
Ініціалізація	        {"normal": [], "fever": [], "high_fever": []}	{} (порожній)
Метод додавання	        groups[status].append(...)	      groups.setdefault(status, []).append(...)
Гарантія всіх 3 ключів	✅ так, завжди, навіть з []	    ❌ ні — лише ті категорії, що реально зустрілись

*Чому це не просто "стилістична різниця", а важливий вибір ПІД ЗАДАЧУ:
    # Version A — коли ти ЗНАЄШ усі можливі категорії заздалегідь
# (наприклад, ІМТ завжди має рівно 4 категорії: Underweight/Normal/Overweight/Obesity)
groups = {"normal": [], "fever": [], "high_fever": []}
# ПЕРЕВАГА: код, що ВИКОРИСТОВУЄ результат, може СПОКІЙНО писати
# groups["high_fever"] БЕЗ перевірки на KeyError — ключ ГАРАНТОВАНО є

    # Version B — коли категорії НЕВІДОМІ заздалегідь
# (наприклад, групуємо за ДІАГНОЗОМ пацієнта — список діагнозів
# може бути БУДЬ-ЯКИМ і невідомим наперед)
groups = {}
groups.setdefault(diagnosis, []).append(name)
# ПЕРЕВАГА: не треба вручну перелічувати ВСІ можливі діагнози заздалегідь —
# dict сам "виростає" рівно настільки, скільки різних категорій зустрілось

*Мій вибір для ЦІЄЇ конкретної задачі (групування за температурним статусом):
        Я б обрав Version A для продакшн-коду цього конкретного випадку, тому що:

1. Категорій рівно три, і вони СТАЛІ — classify_temperature() завжди повертає одне з трьох фіксованих значень, воно ніколи "не вигадає" четверту категорію.
2. Гарантія повноти важливіша за гнучкість — код, що аналізує результат (result["high_fever"]), має завжди отримати список (навіть порожній), а не зіткнутись із KeyError, якщо раптом жоден пацієнт не мав високої температури.
3. Читабельність для нової людини в команді — побачивши {"normal": [], "fever": [], "high_fever": []} на початку функції, одразу видно всі можливі категорії, не читаючи всю логіку classify_temperature().

        Коли я обрав би Version B (setdefault) — якби категорії групування були динамічними й непередбачуваними наперед:
1. # Групування за ДІАГНОЗОМ — тут я НЕ знаю заздалегідь усі можливі діагнози:
diagnosis_groups = {}
for patient in patients:
    diagnosis_groups.setdefault(patient["diagnosis"], []).append(patient["name"])
2. # Немає сенсу заздалегідь писати {"sinusitis": [], "rhinitis": [], "otitis": [], ...}
# для КОЖНОГО можливого діагнозу, що коли-небудь зустрінеться

*Підсумок принципу вибору: 
- структура даних (і спосіб її ініціалізації) має відображати природу задачі, а не бути "звичкою" чи "тим, що коротше пишеться". 
- Фіксована, скінченна множина категорій → готуй dict заздалегідь. 
- Відкрита, непередбачувана множина → setdefault() (або collections.defaultdict, який робить те саме автоматично для кожного нового ключа).
"""
