"""
# !🧠 Challenge №1 — comprehension!

Не запускаючи код, визнач результат:

numbers = [1, 2, 3, 4, 5]

result = [
    x * 2
    for x in numbers
    if x % 2 == 1
]
"""

# Прогноз результату: result = [2, 6, 10]

# *Покрокове виконання:
numbers = [1, 2, 3, 4, 5]

result = [x * 2 for x in numbers if x % 2 == 1]
#          ↑              ↑         ↑
#       що робимо      звідки     умова: ЛИШЕ непарні (x % 2 == 1)

# Крок 1: x = 1 → 1 % 2 == 1? Так (непарне) → додаємо 1 * 2 = 2
# Крок 2: x = 2 → 2 % 2 == 1? Ні (парне)    → ПРОПУСКАЄМО
# Крок 3: x = 3 → 3 % 2 == 1? Так (непарне) → додаємо 3 * 2 = 6
# Крок 4: x = 4 → 4 % 2 == 1? Ні (парне)    → ПРОПУСКАЄМО
# Крок 5: x = 5 → 5 % 2 == 1? Так (непарне) → додаємо 5 * 2 = 10

result = [2, 6, 10]

"""
*Головна пастка цього завдання — порядок операцій:

if спочатку фільтрує, і лише потім застосовується вираз x * 2 до тих елементів, що пройшли фільтр:

[x * 2 for x in numbers if x % 2 == 1]
#  ↑                          ↑
#  застосовується ДРУГИМ    перевіряється ПЕРШИМ

Тобто це не "подвой усі числа, а потім залиш непарні" (це дало б інший результат: [2, 6, 10] для непарних подвоєних значень — тут випадково збігається, але логіка інша!). 
Насправді послідовність така: спочатку перевіряємо x (оригінальне, неподвоєне значення) на непарність, і тільки якщо умова true — рахуємо x * 2.
"""

# *Чому це важливо розуміти — контрприклад, де різниця стає очевидною:
numbers = [1, 2, 3, 4, 5]

# Варіант A (те, що в завданні): фільтруємо ОРИГІНАЛЬНІ числа, потім множимо:
[x * 2 for x in numbers if x % 2 == 1]
# → перевіряємо: 1(непарне), 2(парне), 3(непарне), 4(парне), 5(непарне)
# → [2, 6, 10]

# Варіант B (інша умова): фільтруємо ВЖЕ ПОДВОЄНІ числа:
[x * 2 for x in numbers if (x * 2) % 2 == 1]
# → 2%2=0(парне), 4%2=0, 6%2=0, 8%2=0, 10%2=0 → УМОВА НІКОЛИ НЕ TRUE
# → []  (порожній список! бо подвоєне число ЗАВЖДИ парне)

"""
Цей контрприклад показує: if у comprehension перевіряє той вираз, який у ньому написаний — і важливо чітко розуміти, до якого саме значення (оригінального x чи вже трансформованого x * 2) застосовується умова.

*Багаторядковий запис — те саме, що й один рядок:

# Це:
result = [
    x * 2
    for x in numbers
    if x % 2 == 1
]

# Повністю ідентично цьому (просто розбито на рядки для читабельності):
result = [x * 2 for x in numbers if x % 2 == 1]

Python дозволяє розбивати comprehension на кілька рядків усередині квадратних дужок — це часто роблять, коли вираз, for чи if довгі й не влазять в один рядок.
"""

# ==============================================================================
# ==============================================================================

"""
# !🧠 Challenge №2 — any()!

Що буде?

values = [2, 4, 6, 8]
result = any(x > 5 for x in values)
print(result)

Поясни чому.
"""

# Відповідь: буде виведено: True

# *Покрокове виконання:
values = [2, 4, 6, 8]

result = any(x > 5 for x in values)
#            ↑
#     генераторний вираз — перевіряє КОЖНЕ значення по черзі

# Крок 1: x = 2 → 2 > 5? False  → any() продовжує перевіряти далі
# Крок 2: x = 4 → 4 > 5? False  → any() продовжує перевіряти далі
# Крок 3: x = 6 → 6 > 5? True   → ЗНАЙШЛИ! any() ОДРАЗУ зупиняється тут

result = True  # 8 навіть НЕ перевіряється — сенсу вже немає

"""
*Чому саме True — головне правило any():

any() повертає True, щойно знаходить перший елемент, для якого умова істинна, і одразу припиняє перевірку решти. Достатньо одного 6 > 5, щоб весь результат став True — навіть якщо 8 теж задовольнило б умову, воно вже не перевіряється.

Це називається short-circuit evaluation (лінива/скорочена перевірка) — та сама логіка, що ти вже бачив у операторі and (Практика №4 з логічними операторами):

# and зупиняється на ПЕРШОМУ False:
True and False and True   # ← зупиняється на другому, третій не перевіряє

# any() зупиняється на ПЕРШОМУ True:
any(x > 5 for x in [2, 4, 6, 8])   # ← зупиняється на 6, восьмий не перевіряє

*Чому важливо, що це генераторний вираз (без квадратних дужок):
any(x > 5 for x in values)      # ✅ генератор — перевіряє ПО ОДНОМУ, зупиняється одразу
any([x > 5 for x in values])    # ⚠️ спочатку будує ПОВНИЙ список [False, False, True, True],
                                   #    а ЛИШЕ ПОТІМ перевіряє його — зайва робота

Для короткого списку з чотирьох елементів різниця непомітна, але уяви список з мільйона температур: генератор зупиниться на першому знайденому "гарячому" значенні, а версія зі списком спершу порахує умову для всього мільйона елементів, і лише потім почне перевіряти — тобто виконає значно більше зайвої роботи.

Практичний висновок: для any()/all() завжди пиши генераторний вираз (без []), а не спочатку будуй список і потім передавай його — це і швидше, і Pythonic-стиль, який побачиш у якісному коді.
"""

# ==============================================================================
# ==============================================================================

"""
# !🧠 Challenge №3 — all()!

values = [2, 4, 6, 8]
result = all(x % 2 == 0 for x in values)
print(result)
"""


# Відповідь: буде виведено: True

# *Покрокове виконання:
values = [2, 4, 6, 8]

result = all(x % 2 == 0 for x in values)
#             ↑
#     умова: чи ділиться на 2 без остачі (тобто чи парне)

# Крок 1: x = 2 → 2 % 2 == 0? True  → all() продовжує перевіряти далі
# Крок 2: x = 4 → 4 % 2 == 0? True  → all() продовжує перевіряти далі
# Крок 3: x = 6 → 6 % 2 == 0? True  → all() продовжує перевіряти далі
# Крок 4: x = 8 → 8 % 2 == 0? True  → перевірили ВСІ елементи, жодного False не було

result = True

"""
*Чому саме True — головне правило all():
all() повертає True тільки якщо кожен без винятку елемент задовольняє умову. 
На відміну від any() з попереднього завдання (де досить одного True, щоб зупинитись), all() мусить дійти до кінця послідовності — і лише переконавшись, що жодного False не трапилось, повертає True.

*Якби хоч ОДНЕ число було непарним — результат був би False:
values = [2, 4, 5, 8]   # ← 5 — непарне число

result = all(x % 2 == 0 for x in values)
# 2 % 2 == 0 → True
# 4 % 2 == 0 → True
# 5 % 2 == 0 → False   ← ЗНАЙШЛИ порушника! all() ОДРАЗУ зупиняється тут
# (8 навіть не перевіряється)

result = False


*Порівняння any() та all() на тому самому принципі "зупинки":
	    Зупиняється на	Продовжує, якщо
any()	першому True	усі досі False
all()	першому False	усі досі True

Обидві функції використовують short-circuit evaluation — але дзеркально протилежно одна до одної: any() "шукає підтвердження", а all() "шукає спростування".


#*Підсумок трьох Challenge поспіль (важливий патерн для запам'ятовування):
# any(умова for x in список) → "чи є ХОЧА Б ОДИН, що підходить?"
# all(умова for x in список) → "чи ВСІ без винятку підходять?"

# Список [2, 4, 6, 8] — усі парні:
any(x % 2 == 0 for x in [2, 4, 6, 8])   # True  (є хоча б один парний — усі підходять)
all(x % 2 == 0 for x in [2, 4, 6, 8])   # True  (усі до одного парні)

# Але для непарної умови (> 5) результати вже різняться:
any(x > 5 for x in [2, 4, 6, 8])   # True  (6 і 8 підходять — досить одного)
all(x > 5 for x in [2, 4, 6, 8])   # False (2 і 4 НЕ підходять — руйнує "всі")
"""

# ==============================================================================
# ==============================================================================

"""
# !🧠 Challenge №4 — sorted()!

Що буде?

patients = [
    ("Ivan", 42),
    ("Olena", 35),
    ("Petro", 58),
]

result = sorted(
    patients,
    key=lambda patient: patient[1],
)

print(result)
"""


# Відповідь: буде виведено: [('Olena', 35), ('Ivan', 42), ('Petro', 58)]

# *Покрокове виконання:
patients = [
    ("Ivan", 42),
    ("Olena", 35),
    ("Petro", 58),
]

result = sorted(patients, key=lambda patient: patient[1])
#                          ↑
#              для кожного tuple беремо ЕЛЕМЕНТ З ІНДЕКСОМ 1 (вік)

# key застосовується до КОЖНОГО елемента окремо:
lambda patient: patient[1]  # ("Ivan", 42)  → 42
lambda patient: patient[1]  # ("Olena", 35) → 35
lambda patient: patient[1]  # ("Petro", 58) → 58

# sorted() порівнює ОТРИМАНІ числа: 42, 35, 58
# і сортує їх за замовчуванням від МЕНШОГО до БІЛЬШОГО: 35, 42, 58

# А потім розставляє ОРИГІНАЛЬНІ tuple у відповідному порядку:

"""
Оригінальний вік	Відсортований порядок
Ivan → 42	        2-ге місце
Olena → 35	        1-ше місце (найменше)
Petro → 58	        3-тє місце (найбільше)

*Головне правило, яке тут перевіряється: 
- sorted() за замовчуванням сортує за зростанням (від меншого до більшого), 
- і саме key визначає, за яким значенням усередині кожного елемента відбувається порівняння — а не сам елемент цілком.

*Чому не можна порівнювати tuple напряму без key (для розуміння, навіщо він потрібен):
sorted(patients)   # БЕЗ key — що станеться?

# Python порівнюватиме tuple ЦІЛКОМ:
# ("Ivan", 42) vs ("Olena", 35) vs ("Petro", 58)

# Спочатку порівнюються ПЕРШІ елементи (рядки): "Ivan" vs "Olena" vs "Petro"
# → результат був би АЛФАВІТНИМ за іменем, а НЕ за віком!
# → [('Ivan', 42), ('Olena', 35), ('Petro', 58)]  (вже алфавітний порядок імен)

Саме тому key=lambda patient: patient[1] — обов'язковий, якщо треба сортувати за віком, а не за іменем: він каже Python "ігноруй звичайне порівняння tuple, порівнюй лише те число, яке я тобі вкажу".

Зв'язок із Практикою №7 (сортування пацієнтів):

Це та сама конструкція sorted() + key, яку ти вже писав раніше — тут перевіряється розуміння без reverse=True, тобто типова, найпростіша форма сортування "від меншого до більшого" за замовчуванням.
"""

# ==============================================================================
# ==============================================================================

"""
# !🚀 Challenge №5 — MedAssistant!

Створи:

def classify_temperature(temp: float) -> str:
    ...

з уже знайомими правилами:

< 37.5 → normal
< 39.0 → fever
39+    → high_fever

Потім:

def classify_all(
    temperatures: list[float],
) -> list[str]:
    ...

Функція повинна використовувати classify_temperature().

Для:

[
    36.6,
    38.1,
    39.2,
    37.0,
]

повернути:

[
    "normal",
    "fever",
    "high_fever",
    "normal",
]
"""

"""temperature_batch_classifier.py

Batch temperature classification for MedAssistant, reusing the
single-reading classifier rather than duplicating its logic.
"""


def classify_temperature(temp: float) -> str:
    """Classify a single body temperature reading.

    Args:
        temp: Body temperature in degrees Celsius.

    Returns:
        str: "normal", "fever", or "high_fever".
    """
    if temp < 37.5:
        return "normal"
    elif temp < 39.0:  # already known: temp >= 37.5 here
        return "fever"
    else:  # temp >= 39.0
        return "high_fever"


def classify_all(temperatures: list[float]) -> list[str]:
    """Classify a whole list of temperature readings.

    Reuses classify_temperature() for each reading — this function's
    only job is mapping over the list, not re-deciding the thresholds.

    Args:
        temperatures: A list of body temperature readings in Celsius.

    Returns:
        list[str]: One category per input reading, same order.
    """
    return [classify_temperature(temp) for temp in temperatures]


# --- Demo ---
temperatures = [
    36.6,
    38.1,
    39.2,
    37.0,
]

categories = classify_all(temperatures)

# --- Framed table output ---
MARKER = {"normal": "🟢", "fever": "🟡", "high_fever": "🔴"}

rows = [
    f"{temp:<6.1f} →  {MARKER[cat]} {cat}"
    for temp, cat in zip(temperatures, categories)
]

width = max(len(row) for row in rows) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  BATCH TEMPERATURE CLASSIFICATION".center(width) + "│")
print("├" + "─" * width + "┤")
for row in rows:
    print("│  " + row.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

print(f"\nclassify_all({temperatures}) → {categories}")

"""
┌──────────────────────────┐
│  BATCH TEMPERATURE CLASSIFICATION│
├──────────────────────────┤
│  36.6   →  🟢 normal      │
│  38.1   →  🟡 fever       │
│  39.2   →  🔴 high_fever  │
│  37.0   →  🟢 normal      │
└──────────────────────────┘

classify_all([36.6, 38.1, 39.2, 37.0]) → ['normal', 'fever', 'high_fever', 'normal']
"""

"""
Це той самий принцип DRY, що й у попередньому завданні analyze_temperatures(): функція classify_temperature() є єдиним авторитетним джерелом інформації щодо того, що вважається  "normal", "fever", або "high_fever". Якщо клініка коли-небудь змінить поріг лихоманки з 37,5 на 37,8, у всьому коді потрібно буде редагувати лише одне місце — функція classify_all() (та всі інші, що її використовують) автоматично врахує цю зміну, і ризик того, що одна копія буде оновлена, а інша — пропущена, дорівнює нулю.

#*Розбір виразу:
[classify_temperature(temp) for temp in temperatures]
#  ↑                          ↑
#  що додати до              цикл по кожному
#  нового списку (виклик функції)   елементу вхідного списку

Для [36.6, 38.1, 39.2, 37.0]:

classify_temperature(36.6) → "normal"
classify_temperature(38.1) → "fever"
classify_temperature(39.2) → "high_fever"
classify_temperature(37.0) → "normal"

→ ["normal", "fever", "high_fever", "normal"] — точно відповідає очікуваному результату.
"""

# ==============================================================================
# ==============================================================================

"""
🚀 Challenge №6 — Junior+

Створи:
def analyze_patients(
    patients: list[tuple[str, float]],
) -> dict:
    ...

Вхід:
patients = [
    ("Ivan", 36.6),
    ("Olena", 38.2),
    ("Petro", 39.1),
    ("Hanna", 37.0),
]

Результат:
{
    "normal": 2,
    "fever": 1,
    "high_fever": 1,
}
Обов'язково:
analyze_patients() повинна використовувати:

classify_temperature()

а не дублювати логіку температурних меж.
"""


def classify_temperature(temp: float) -> str:
    """Classify a single body temperature reading.

    (Reused from the earlier MedAssistant challenge — not duplicated.)
    """
    if temp < 37.5:
        return "normal"
    elif temp < 39.0:
        return "fever"
    else:
        return "high_fever"


def analyze_patients(patients: list[tuple[str, float]]) -> dict[str, int]:
    """Count how many patients fall into each temperature category.

    Reuses classify_temperature() for the actual classification logic —
    this function's only job is counting, not re-deciding the thresholds.

    Args:
        patients: A list of (name, temperature) tuples.

    Returns:
        dict: All three category keys always present (0 if unused):
            {"normal": int, "fever": int, "high_fever": int}
    """
    counts = {"normal": 0, "fever": 0, "high_fever": 0}

    for name, temp in patients:
        category = classify_temperature(temp)  # ← reused, not reimplemented
        counts[category] += 1

    return counts


# --- Demo ---
patients = [
    ("Ivan", 36.6),
    ("Olena", 38.2),
    ("Petro", 39.1),
    ("Hanna", 37.0),
]

result = analyze_patients(patients)

# --- Framed output ---
MARKER = {"normal": "🟢", "fever": "🟡", "high_fever": "🔴"}

detail_rows = [
    f"{name:<8} {temp:<6.1f} →  {MARKER[classify_temperature(temp)]} {classify_temperature(temp)}"
    for name, temp in patients
]
summary_row = f"normal: {result['normal']}  |  fever: {result['fever']}  |  high_fever: {result['high_fever']}"

lines = detail_rows + ["─" * max(len(r) for r in detail_rows), summary_row]
width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  PATIENT TEMPERATURE ANALYSIS".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────────────────────────────┐
│         PATIENT TEMPERATURE ANALYSIS       │
├────────────────────────────────────────────┤
│  Ivan     36.6   →  🟢 normal               │
│  Olena    38.2   →  🟡 fever                │
│  Petro    39.1   →  🔴 high_fever           │
│  Hanna    37.0   →  🟢 normal               │
│  ───────────────────────────────           │
│  normal: 2  |  fever: 1  |  high_fever: 1  │
└────────────────────────────────────────────┘
"""

"""
#*Чому analyze_patients() не дублює межі температур:
def analyze_patients(patients):
    counts = {"normal": 0, "fever": 0, "high_fever": 0}
    for name, temp in patients:
        category = classify_temperature(temp)   # ← ВИКЛИК готової функції
        counts[category] += 1                     # ← лише РАХУЄМО результат
    return counts

Ця функція взагалі не знає, де саме проходять межі 37.5 чи 39.0 — вона лише запитує classify_temperature(): "до якої категорії належить ця температура?" і збільшує відповідний лічильник. Це та сама структура, що й у analyze_temperatures() з попередньої серії задач, лише тепер вхід — список пар (ім'я, температура), а не просто список чисел.

#*Ключова відмінність від analyze_temperatures() (тип входу):
# analyze_temperatures() — просто список чисел:
analyze_temperatures([36.6, 38.1, 39.2])

# analyze_patients() — список tuple (ім'я, температура):
analyze_patients([("Ivan", 36.6), ("Olena", 38.2)])
#                     ↑
#          розпаковуємо tuple: for name, temp in patients
#          ім'я тут НЕ використовується для підрахунку,
#          але зберігається в сигнатурі — бо це "патерн вхідних даних"

#*Зверни увагу: 
- name у цій функції навіть не бере участь у логіці підрахунку — він потрібен лише тому, що такий формат вхідних даних (list[tuple[str, float]]). 
Це нормально: не кожен параметр функції обов'язково "активно використовується" у кожному рядку тіла — головне, щоб сигнатура правильно відображала структуру вхідних даних.

#*Пряме використання ключа category без .lower().replace():
На відміну від Challenge №5 (де classify_temperature() повертав "High fever" з великої літери й пробілом), тут classify_temperature() одразу повертає "high_fever" у потрібному форматі — тому counts[category] += 1 працює напряму, без додаткового перетворення рядка.
"""

# ==============================================================================
# ==============================================================================

"""
# !🔥 Challenge №7 — рівень Junior+!

Створи:
def get_high_risk_patients(
    patients: list[tuple[str, float]],
) -> list[str]:
    ...

Вона повинна повернути імена пацієнтів із температурою >= 39.0.
Для:
[
    ("Ivan", 36.6),
    ("Olena", 38.2),
    ("Petro", 39.1),
    ("Hanna", 37.0),
    ("Dmytro", 39.5),
]

результат:
["Petro", "Dmytro"]

Постарайся використати list comprehension.
"""

THRESHOLD = 39.0


def get_high_risk_patients(patients: list[tuple[str, float]]) -> list[str]:
    """Повертає імена пацієнтів із температурою >= 39.0.

    Використовує list comprehension: одночасно фільтрує (if temp >= THRESHOLD)
    і трансформує (беремо лише name, відкидаючи temp).
    """
    return [name for name, temp in patients if temp >= THRESHOLD]


def get_high_risk_patients_for_loop(patients: list[tuple[str, float]]) -> list[str]:
    """Той самий результат, реалізований звичайним for — для порівняння."""
    result = []
    for name, temp in patients:
        if temp >= THRESHOLD:
            result.append(name)
    return result


# --- Демонстрація ---
patients = [
    ("Ivan", 36.6),
    ("Olena", 38.2),
    ("Petro", 39.1),
    ("Hanna", 37.0),
    ("Dmytro", 39.5),
]

high_risk_comprehension = get_high_risk_patients(patients)
high_risk_for_loop = get_high_risk_patients_for_loop(patients)

# --- Вивід у рамці ---
lines = [
    f"Пацієнти: {patients}",
    "─" * 30,
    f"List comprehension: {high_risk_comprehension}",
    f"Звичайний for:      {high_risk_for_loop}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ПАЦІЄНТИ ГРУПИ РИЗИКУ (≥ 39.0)".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    ПАЦІЄНТИ ГРУПИ РИЗИКУ (≥ 39.0)                                 │
├───────────────────────────────────────────────────────────────────────────────────────────────────┤
│  Пацієнти: [('Ivan', 36.6), ('Olena', 38.2), ('Petro', 39.1), ('Hanna', 37.0), ('Dmytro', 39.5)]  │
│  ──────────────────────────────                                                                   │
│  List comprehension: ['Petro', 'Dmytro']                                                          │
│  Звичайний for:      ['Petro', 'Dmytro']                                                          │
└───────────────────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
#*Пояснення list comprehension з розпакуванням tuple:
[name for name, temp in patients if temp >= THRESHOLD]
#  ↑          ↑                        ↑
#  що        розпаковуємо КОЖЕН        умова фільтрації
#  беремо    tuple одразу на 2 змінні  (перевіряє temp,
#  (лише name)                          не name!)

#*Крок за кроком, що відбувається:
patients = [
    ("Ivan", 36.6),
    ("Olena", 38.2),
    ("Petro", 39.1),
    ("Hanna", 37.0),
    ("Dmytro", 39.5),
]

# for name, temp in patients — розпаковує КОЖЕН tuple на 2 змінні:
("Ivan", 36.6)    → name="Ivan",   temp=36.6   → 36.6 >= 39.0? False → пропускаємо
("Olena", 38.2)   → name="Olena",  temp=38.2   → 38.2 >= 39.0? False → пропускаємо
("Petro", 39.1)   → name="Petro",  temp=39.1   → 39.1 >= 39.0? True  → додаємо "Petro"
("Hanna", 37.0)   → name="Hanna",  temp=37.0   → 37.0 >= 39.0? False → пропускаємо
("Dmytro", 39.5)  → name="Dmytro", temp=39.5   → 39.5 >= 39.0? True  → додаємо "Dmytro"

result = ["Petro", "Dmytro"]

#*Ключова особливість цього comprehension — фільтруємо за ОДНИМ значенням, повертаємо ІНШЕ:
[name for name, temp in patients if temp >= THRESHOLD]
#  ↑                                  ↑
#  ПОВЕРТАЄМО name                    ФІЛЬТРУЄМО за temp

Це трохи складніше за попередні приклади (де фільтрували і повертали той самий елемент) — тут ми дивимось на temp для прийняття рішення, а в результат кладемо зовсім інше значення — name. Це дуже поширений і корисний патерн: "фільтруй за однією ознакою, повертай іншу".

#*Порівняння з реалізацією через for:
# --- List comprehension — 1 рядок ---
result = [name for name, temp in patients if temp >= THRESHOLD]

# --- Звичайний for — 4 рядки, той самий результат ---
result = []
for name, temp in patients:
    if temp >= THRESHOLD:
        result.append(name)

Обидва варіанти роблять однакове — розпаковують tuple, перевіряють температуру, і якщо умова true, додають ім'я до результату. Comprehension просто записує ту саму логіку компактніше.

Зв'язок із попередніми задачами: це поєднання одразу трьох навичок з цього розділу — розпакування tuple (з enumerate()/zip() завдань), list comprehension з умовою (Практика №1, №4) та фільтрація за одним полем, повернення іншого (нова навичка цієї задачі).
"""
