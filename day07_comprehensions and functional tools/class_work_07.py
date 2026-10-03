"""
# ! Практика №1 !

Створи:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

За допомогою list comprehension створи:
[2, 4, 6, 8, 10]
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# --- Варіант 1: list comprehension ---
# [вираз for елемент in список if умова]
even_comprehension = [n for n in numbers if n % 2 == 0]

# --- Варіант 2: звичайний for (те саме, довшим шляхом) ---
even_for_loop = []
for n in numbers:
    if n % 2 == 0:
        even_for_loop.append(n)

# --- Варіант 3: filter() + lambda ---
# filter(функція, послідовність) — залишає лише елементи,
# для яких функція повертає True
even_filter = list(filter(lambda n: n % 2 == 0, numbers))

# --- Вивід у рамці ---
results = [
    ("Оригінал",               str(numbers)),
    ("List comprehension",     str(even_comprehension)),
    ("Звичайний for",          str(even_for_loop)),
    ("filter() + lambda",      str(even_filter)),
]

label_width = max(len(label) for label, _ in results)
value_width = max(len(value) for _, value in results)
width = label_width + value_width + 5

print("\n┌" + "─" * width + "┐")
print("│" + "  ПАРНІ ЧИСЛА".center(width) + "│")
print("├" + "─" * width + "┤")
for label, value in results:
    print(f"│  {label.ljust(label_width)} │ {value.ljust(value_width)} │")
print("└" + "─" * width + "┘")

"""
┌──────────────────────────────────────────────────────┐
│                      ПАРНІ ЧИСЛА                     │
├──────────────────────────────────────────────────────┤
│  Оригінал           │ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] │
│  List comprehension │ [2, 4, 6, 8, 10]                │
│  Звичайний for      │ [2, 4, 6, 8, 10]                │
│  filter() + lambda  │ [2, 4, 6, 8, 10]                │
└──────────────────────────────────────────────────────┘
"""

"""
*Пояснення list comprehension:

[n for n in numbers if n % 2 == 0]
# ↑      ↑         ↑          ↑
# що     звідки   яке умова   зберігаємо
# додати брати    значення    в новий список

Читається зліва направо як речення: "[візьми n для кожного n у numbers, якщо n % 2 == 0]".


*Порівняння трьох підходів "рядок за рядком":
# --- Звичайний for — 4 рядки, потрібен порожній список заздалегідь ---
even_for_loop = []
for n in numbers:
    if n % 2 == 0:
        even_for_loop.append(n)

# --- List comprehension — 1 рядок, той самий результат ---
even_comprehension = [n for n in numbers if n % 2 == 0]

# --- filter() — теж компактно, але потребує list() навколо ---
even_filter = list(filter(lambda n: n % 2 == 0, numbers))
#                   ↑
#              filter() сам по собі повертає "лінивий" об'єкт-ітератор,
#              а не готовий список — тому обгортаємо в list()


*Коли що обирати:
	                        List comprehension	      filter()
Читабельність для новачка	✅ найпростіше	        ⚠️ потрібно знати lambda
Швидкість	                ✅ трохи швидше	        звичайно
Складна умова (and/or)	    ✅ легко дописати	    ⚠️ громіздкіше в lambda
Рекомендація Python-спільноти	✅ типовий вибір	    рідше, для простих фільтрів

Головне правило: list comprehension — це не "просунута фіча", а стандартний, найбільш Pythonic спосіб фільтрації та трансформації списків. Звичайний for з append() — робочий варіант, але досвідчені розробники Python майже завжди оберуть comprehension там, де це можливо без втрати читабельності.
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №2!

Створи:
numbers = [1, 2, 3, 4, 5]

отримай:
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25,
}

Використай dict comprehension.
"""

numbers = [1, 2, 3, 4, 5]

# --- Варіант 1: dict comprehension ---
# {ключ: значення for елемент in список}
squares_comprehension = {n: n ** 2 for n in numbers}

# --- Варіант 2: звичайний for (те саме, довшим шляхом) ---
squares_for_loop = {}
for n in numbers:
    squares_for_loop[n] = n ** 2

# --- Вивід у рамці ---
lines = [
    f"Оригінал:             {numbers}",
    f"Dict comprehension:   {squares_comprehension}",
    f"Звичайний for:        {squares_for_loop}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  КВАДРАТИ ЧИСЕЛ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌──────────────────────────────────────────────────────────┐
│                       КВАДРАТИ ЧИСЕЛ                     │
├──────────────────────────────────────────────────────────┤
│  Оригінал:             [1, 2, 3, 4, 5]                   │
│  Dict comprehension:   {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}  │
│  Звичайний for:        {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}  │
└──────────────────────────────────────────────────────────┘
"""

"""
*Пояснення dict comprehension:
{n: n ** 2 for n in numbers}
# ↑   ↑           ↑
# ключ значення  звідки беремо n

Читається як: "для кожного n у numbers створи пару: ключ — це n, значення — це n ** 2".

*Порівняння з list comprehension (минула задача):
# List comprehension — ОДНЕ значення на елемент:
[n ** 2 for n in numbers]
# → [1, 4, 9, 16, 25]

# Dict comprehension — ПАРА "ключ: значення" на елемент:
{n: n ** 2 for n in numbers}
# → {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

Головна відмінність у синтаксисі — квадратні дужки [] замінюються на фігурні {}, а замість одного виразу пишеться пара через двокрапку ключ: значення.


*Порівняння рядок за рядком зі звичайним for:
# --- Звичайний for — 3 рядки, потрібен порожній dict заздалегідь ---
squares_for_loop = {}
for n in numbers:
    squares_for_loop[n] = n ** 2

# --- Dict comprehension — 1 рядок, той самий результат ---
squares_comprehension = {n: n ** 2 for n in numbers}
#----------------------------------------------------------

*Практичний приклад — коли dict comprehension особливо зручний:
# Наприклад, побудова словника "ім'я → температура" з двох списків
# (тут природньо поєднати з zip(), який ти вже знаєш):
names = ["Ivan", "Olena", "Petro"]
temps = [36.6, 38.2, 37.4]

patient_temps = {name: temp for name, temp in zip(names, temps)}
# → {'Ivan': 36.6, 'Olena': 38.2, 'Petro': 37.4}
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №3!

Є:
names = [
    " Ivan ",
    "OLENA",
    " petro",
    "HANNA ",
]

Створи функцію:
def normalize_name(name: str) -> str:
    ...

і сформуй новий список нормалізованих імен.

Очікувано:
["Ivan", "Olena", "Petro", "Hanna"]
"""

names = [
    " Ivan ",
    "OLENA",
    " petro",
    "HANNA ",
]


def normalize_name(name: str) -> str:
    """Прибирає пробіли та приводить ім'я до формату 'Перша літера велика'."""
    # strip() — прибирає пробіли з країв
    # capitalize() — перша літера ВЕЛИКА, решта маленькі
    #   "OLENA" → "Olena", " petro" → "petro" → "Petro"
    return name.strip().capitalize()


# --- Варіант 1: list comprehension ---
normalized_comprehension = [normalize_name(name) for name in names]

# --- Варіант 2: звичайний for ---
normalized_for_loop = []
for name in names:
    normalized_for_loop.append(normalize_name(name))

# --- Вивід у рамці: порівняння До / Після ---
rows = [f"{repr(before)!s:<12} →  {after}" for before, after in zip(names, normalized_comprehension)]

width = max(len(row) for row in rows) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  НОРМАЛІЗАЦІЯ ІМЕН".center(width) + "│")
print("├" + "─" * width + "┤")
for row in rows:
    print("│  " + row.ljust(width - 2) + "│")
print("├" + "─" * width + "┤")
print("│  " + f"List comprehension: {normalized_comprehension}".ljust(width - 2) + "│")
print("│  " + f"Звичайний for:      {normalized_for_loop}".ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────┐
│     НОРМАЛІЗАЦІЯ ІМЕН   │
├─────────────────────────┤
│  ' Ivan '     →  Ivan   │
│  'OLENA'      →  Olena  │
│  ' petro'     →  Petro  │
│  'HANNA '     →  Hanna  │
├─────────────────────────┤
│  List comprehension: ['Ivan', 'Olena', 'Petro', 'Hanna']│
│  Звичайний for:      ['Ivan', 'Olena', 'Petro', 'Hanna']│
└─────────────────────────┘
"""

"""
*Пояснення normalize_name() крок за кроком:
name = "OLENA"
name.strip()          # → "OLENA"      (пробілів не було, нічого не змінилось)
name.strip().capitalize()   # → "Olena"    (перша літера ВЕЛИКА, решта — маленькі)

name = " petro"
name.strip()          # → "petro"     (пробіл зліва прибрано)
name.strip().capitalize()   # → "Petro"    (P — велика, решта — маленькі)

*Чому саме .capitalize(), а не .upper() чи .title():
"OLENA".upper()         # → "OLENA"       ❌ все ВЕЛИКЕ — не те, що треба
"OLENA".lower()          # → "olena"       ❌ все маленьке — теж не те
"OLENA".capitalize()     # → "Olena"       ✅ саме перша велика, решта маленькі
"OLENA".title()          # → "Olena"       ✅ теж підходить для ОДНОГО слова

#.capitalize() і .title() дають однаковий результат для одного слова, але відрізняються для кількох слів:
"jane doe".capitalize()   # → "Jane doe"   ← лише ПЕРШЕ слово з великої
"jane doe".title()        # → "Jane Doe"   ← КОЖНЕ слово з великої

#Для одного імені (як тут) обидва варіанти рівноцінні —  .capitalize(), це трохи "легший" та частіше вживаний варіант для одного слова.

*Порівняння двох підходів формування списку:
# --- List comprehension — 1 рядок ---
normalized = [normalize_name(name) for name in names]

# --- Звичайний for — 3 рядки, той самий результат ---
normalized = []
for name in names:
    normalized.append(normalize_name(name))

*Зверни увагу: 
-у обох варіантах усередині циклу викликається та сама функція normalize_name() — сама логіка нормалізації винесена окремо (DRY), 
-list comprehension чи for — це лише спосіб пройтись по списку й зібрати результати.
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №4!

Є:
temperatures = [
    36.6,
    37.2,
    38.1,
    39.0,
    37.8,
]

За допомогою comprehension створи список температур ≥ 38.0.

Очікувано:
[38.1, 39.0]
"""

temperatures = [
    36.6,
    37.2,
    38.1,
    39.0,
    37.8,
]

THRESHOLD = 38.0

# --- Варіант 1: list comprehension ---
high_temps_comprehension = [t for t in temperatures if t >= THRESHOLD]

# --- Варіант 2: filter() + lambda ---
high_temps_filter = list(filter(lambda t: t >= THRESHOLD, temperatures))

# --- Вивід у рамці ---
lines = [
    f"Оригінал:            {temperatures}",
    f"List comprehension:  {high_temps_comprehension}",
    f"filter() + lambda:   {high_temps_filter}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ВИСОКА ТЕМПЕРАТУРА (≥ 38.0)".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌───────────────────────────────────────────────────────┐
│               ВИСОКА ТЕМПЕРАТУРА (≥ 38.0)             │
├───────────────────────────────────────────────────────┤
│  Оригінал:            [36.6, 37.2, 38.1, 39.0, 37.8]  │
│  List comprehension:  [38.1, 39.0]                    │
│  filter() + lambda:   [38.1, 39.0]                    │
└───────────────────────────────────────────────────────┘
"""

"""
*Пояснення list comprehension з умовою:
[t for t in temperatures if t >= THRESHOLD]
# ↑         ↑             ↑
# що       звідки       умова фільтрації
# беремо   беремо      (залишаємо тільки ті, де True)

#Читається як: "[візьми t для кожного t у temperatures, якщо t >= 38.0]".

*Порівняння з filter():
# List comprehension — умова ВСЕРЕДИНІ квадратних дужок:
[t for t in temperatures if t >= THRESHOLD]

# filter() — умова як ОКРЕМА функція (lambda), передана аргументом:
list(filter(lambda t: t >= THRESHOLD, temperatures))
#            ↑                          ↑
#        функція-умова              послідовність для перевірки

*Різниця у "напрямку мислення":

	                List comprehension	                    filter()
Синтаксис	        "візьми X, якщо умова"	                "залиш елементи, для яких функція True"
Читабельність	    ✅ природна для простих умов	трохи      "нав'язана" через lambda
Розширюваність	    легко додати ще умову (and)	            доведеться ускладнювати lambda

# Легко розширити list comprehension додатковою умовою:
[t for t in temperatures if t >= 38.0 and t < 40.0]

# У filter() теж можливо, але lambda стає довшою:
list(filter(lambda t: t >= 38.0 and t < 40.0, temperatures))

*Ключовий висновок з цієї серії задач: 
-для фільтрації списку список comprehension ([x for x in ... if ...]) і filter() дають однаковий результат, 
-Python-спільнота зазвичай віддає перевагу comprehension за читабельність — саме тому в попередніх завданнях (Практика №1) comprehension показувався першим, а filter() — як альтернатива для ознайомлення.
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №5!

Використай any():
Чи є в списку температура ≥ 39.0?

temperatures = [
    36.6,
    37.2,
    38.1,
    39.0,
]
"""


temperatures = [
    36.6,
    37.2,
    38.1,
    39.0,
]

THRESHOLD = 39.0

# --- any() — True, якщо ХОЧА Б ОДИН елемент задовольняє умову ---
has_high_fever = any(t >= THRESHOLD for t in temperatures)

# --- all() — True, тільки якщо ВСІ елементи задовольняють умову ---
all_high_fever = all(t >= THRESHOLD for t in temperatures)

# --- Вивід у рамці ---
lines = [
    f"Список:  {temperatures}",
    f"Поріг:   >= {THRESHOLD}",
    "─" * 30,
    f"any() — хоча б одна:  {has_high_fever}",
    f"all() — усі відразу:  {all_high_fever}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ANY() ТА ALL()".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────────────────┐
│             ANY() ТА ALL()          │
├─────────────────────────────────────┤
│  Список:  [36.6, 37.2, 38.1, 39.0]  │
│  Поріг:   >= 39.0                   │
│  ──────────────────────────────     │
│  any() — хоча б одна:  True         │
│  all() — усі відразу:  False        │
└─────────────────────────────────────┘
"""

"""
*Пояснення all() — протилежна логіка:
all(t >= 39.0 for t in temperatures)
# 36.6 >= 39.0 → False  ← ОДРАЗУ False! all() зупиняється на ПЕРШОМУ False
# (37.2, 38.1, 39.0 навіть не перевіряються — сенсу немає)

*Round-up таблиця "коли True":
	                    any()	all()
Всі False	            False	False
Один True, решта False	True	False
Всі True	            True	True
Порожній список []	    False	True ⚠️

⚠️ Пастка з порожнім списком: all([]) повертає True (це называється vacuous truth — "істина за замовчуванням", бо "немає жодного елемента, який порушує умову"), а any([]) — False (бо "немає жодного елемента, який підтверджує умову"). Варто пам'ятати про це, якщо список температур може виявитись порожнім.

*Без круглих дужок замість квадратних — важлива деталь:
any(t >= 39.0 for t in temperatures)      # ✅ генераторний вираз (без зайвої пам'яті)
any([t >= 39.0 for t in temperatures])    # теж працює, але спершу будує ПОВНИЙ список,
                                             # а потім перевіряє — зайва витрата пам'яті

Для any()/all() краще писати без квадратних дужок — це називається generator expression, і він обчислює значення "на льоту", по одному, замість того щоб спочатку створити цілий список [True, False, False, True] у пам'яті.

*Практичне застосування в медичному контексті:
# any() — "чи є ХОЧА Б ОДИН критичний показник у пацієнта?"
if any(t >= 39.0 for t in patient_temps):
    print("⚠ Потрібна негайна увага!")

# all() — "чи ВСІ показники в нормі?"
if all(t < 37.5 for t in patient_temps):
    print("✅ Всі виміри в нормі")
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №6!

Використай all():
Чи всі температури нижчі за 37.5?
"""

temperatures = [
    36.6,
    37.2,
    38.1,
    39.0,
]

THRESHOLD = 37.5

# all() — True тільки якщо КОЖЕН елемент задовольняє умову
all_below_threshold = all(t < THRESHOLD for t in temperatures)

# --- Знаходимо, ЯКІ саме значення порушують умову (для наочності) ---
violations = [t for t in temperatures if t >= THRESHOLD]

# --- Вивід у рамці ---
lines = [
    f"Список:  {temperatures}",
    f"Умова:   < {THRESHOLD}",
    "─" * 30,
    f"all() — усі нижче порогу?  {all_below_threshold}",
    f"Порушники: {violations}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ALL() — ПЕРЕВІРКА ТЕМПЕРАТУР".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────────────────┐
│      ALL() — ПЕРЕВІРКА ТЕМПЕРАТУР   │
├─────────────────────────────────────┤
│  Список:  [36.6, 37.2, 38.1, 39.0]  │
│  Умова:   < 37.5                    │
│  ──────────────────────────────     │
│  all() — усі нижче порогу?  False   │
│  Порушники: [38.1, 39.0]            │
└─────────────────────────────────────┘
"""

"""
*Покрокове виконання all():
all(t < 37.5 for t in temperatures)

# 36.6 < 37.5 → True   ← перевіряємо далі
# 37.2 < 37.5 → True   ← перевіряємо далі
# 38.1 < 37.5 → False  ← ЗНАЙШЛИ порушника! all() ОДРАЗУ зупиняється тут
# (39.0 навіть не перевіряється — результат уже відомий: False)

# Підсумок: all_below_threshold = False

*Чому результат False, хоча дві перші температури — нормальні:
Це головна суть all() — потрібно, щоб абсолютно всі елементи задовольняли умову. Достатньо одного винятку (38.1 і 39.0 не менші за 37.5), щоб увесь результат став False — незалежно від того, скільки елементів пройшли перевірку успішно.

*Практичне застосування — типовий медичний сценарій:
if all(t < 37.5 for t in patient_temps):
    print("✅ Пацієнт стабільний, усі виміри в нормі")
else:
    print("⚠ Є відхилення — потрібна перевірка")
    # список тих, хто "провалив" умову — корисно показати ЩО саме не так
    print(f"Підвищені: {[t for t in patient_temps if t >= 37.5]}")

*Зв'язок із минулою задачею (any() vs all()):
Той самий список [36.6, 37.2, 38.1, 39.0], різні запитання — різні відповіді:
Питання	                                    Функція	    Результат
"Чи є хоча б одна ≥ 39.0?" (Практика №5)	any()	    True
"Чи всі < 37.5?" (ця задача)	            all()	    False

Обидва запитання про один і той самий список температур дають різні відповіді, бо перевіряють протилежні умови (наявність хоча б одного проти відсутності жодного винятку).
"""


# ==============================================================================
# ==============================================================================

"""
# !Практика №7!

Є:
patients = [
    ("Ivan", 42),
    ("Olena", 35),
    ("Petro", 58),
    ("Hanna", 29),
]

Відсортуй пацієнтів:
-за віком від молодшого до старшого;
-за віком від старшого до молодшого.

Використай sorted() + key.
"""

from operator import itemgetter

patients = [
    ("Ivan", 42),
    ("Olena", 35),
    ("Petro", 58),
    ("Hanna", 29),
]

# --- Варіант 1: lambda ---
youngest_first_lambda = sorted(patients, key=lambda p: p[1])
oldest_first_lambda = sorted(patients, key=lambda p: p[1], reverse=True)

# --- Варіант 2: operator.itemgetter() ---
youngest_first_itemgetter = sorted(patients, key=itemgetter(1))
oldest_first_itemgetter = sorted(patients, key=itemgetter(1), reverse=True)

# --- Вивід у рамці ---
lines = [
    f"Оригінал:                    {patients}",
    "─" * 30,
    f"Молодший→старший (lambda):   {youngest_first_lambda}",
    f"Старший→молодший (lambda):   {oldest_first_lambda}",
    "─" * 30,
    f"Молодший→старший (itemgetter): {youngest_first_itemgetter}",
    f"Старший→молодший (itemgetter): {oldest_first_itemgetter}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  СОРТУВАННЯ ЗА ВІКОМ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                                      СОРТУВАННЯ ЗА ВІКОМ                                     │
├──────────────────────────────────────────────────────────────────────────────────────────────┤
│  Оригінал:                    [('Ivan', 42), ('Olena', 35), ('Petro', 58), ('Hanna', 29)]    │
│  ──────────────────────────────                                                              │
│  Молодший→старший (lambda):   [('Hanna', 29), ('Olena', 35), ('Ivan', 42), ('Petro', 58)]    │
│  Старший→молодший (lambda):   [('Petro', 58), ('Ivan', 42), ('Olena', 35), ('Hanna', 29)]    │
│  ──────────────────────────────                                                              │
│  Молодший→старший (itemgetter): [('Hanna', 29), ('Olena', 35), ('Ivan', 42), ('Petro', 58)]  │
│  Старший→молодший (itemgetter): [('Petro', 58), ('Ivan', 42), ('Olena', 35), ('Hanna', 29)]  │
└──────────────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
*Пояснення sorted() + key:
sorted(patients, key=lambda p: p[1])
#       ↑              ↑
#   що сортуємо   ЗА ЧИМ сортувати (функція, що бере ОДИН елемент
#                  і повертає значення, за яким порівнювати)

*Крок за кроком, що робить key:
patients = [("Ivan", 42), ("Olena", 35), ("Petro", 58), ("Hanna", 29)]

# key=lambda p: p[1] застосовується до КОЖНОГО tuple окремо:
lambda p: p[1]   # p = ("Ivan", 42)  → повертає 42
lambda p: p[1]   # p = ("Olena", 35) → повертає 35
lambda p: p[1]   # p = ("Petro", 58) → повертає 58
lambda p: p[1]   # p = ("Hanna", 29) → повертає 29

# sorted() сортує ОРИГІНАЛЬНІ tuple, але порівнює саме ЦІ повернуті числа:
# 29, 35, 42, 58 → сортує → Hanna(29), Olena(35), Ivan(42), Petro(58)

*Два способи задати key — порівняння:
# --- lambda: універсальний, працює для будь-якої логіки ---
sorted(patients, key=lambda p: p[1])

# --- itemgetter: спеціалізований, ТІЛЬКИ для вибору елемента за індексом/ключем ---
from operator import itemgetter
sorted(patients, key=itemgetter(1))

	                lambda p: p[1]	                         itemgetter(1)
Що робить	        довільна функція	                     лише "візьми елемент за індексом 1"
Швидкість	        звичайна	                            ⚡ трохи швидша (написана на C)
Гнучкість	        ✅ можна складну логіку (p[1] + p[0])   ❌ тільки прямий доступ за індексом
Читабельність	    зрозуміліше новачку	                     коротше, "правильний" Python-стиль

*Чому reverse=True, а не сортувати "навпаки" вручну:
# ❌ Неправильно (і небезпечно) — інвертувати key:
sorted(patients, key=lambda p: -p[1])   # працює лише для ЧИСЕЛ (мінус)
                                          # зламається для рядків чи інших типів!

# ✅ Правильно — універсальний параметр reverse:
sorted(patients, key=lambda p: p[1], reverse=True)   # працює завжди

*Важливо: sorted() НЕ змінює оригінальний список:
patients   # досі [("Ivan", 42), ("Olena", 35), ("Petro", 58), ("Hanna", 29)]
# sorted() повертає НОВИЙ відсортований список, оригінал незмінний
# (на відміну від patients.sort(), який сортує "на місці")
"""

# ==============================================================================
# ==============================================================================

"""
# !Практика №8!

Створи функцію:

def apply_operation(
    value: float,
    operation: Callable[[float], float],
) -> float:
    ...

і застосуй:

double
square
"""

from collections.abc import Callable


def apply_operation(
    value: float,
    operation: Callable[[float], float],
) -> float:
    """Застосовує довільну функцію `operation` до `value`.

    Callable[[float], float] — тип-підказка, що означає:
    "функція, яка приймає ОДИН float і повертає float".
    Це не обмежує сам код (Python не перевіряє типи під час виконання),
    але допомагає IDE та іншим розробникам одразу зрозуміти,
    ЯКОГО виду функцію очікує цей параметр.
    """
    return operation(value)


def double(x: float) -> float:
    """Подвоює число."""
    return x * 2


def square(x: float) -> float:
    """Підносить число до квадрата."""
    return x ** 2


def celsius_to_fahrenheit(x: float) -> float:
    """Переводить температуру з Цельсія у Фаренгейт."""
    return x * 9 / 5 + 32


# --- Застосування ---
results = [
    ("apply_operation(5, double)",   apply_operation(5, double)),
    ("apply_operation(5, square)",   apply_operation(5, square)),
    ("apply_operation(37, celsius_to_fahrenheit)", apply_operation(37, celsius_to_fahrenheit)),
    ("apply_operation(10, lambda x: x + 100)", apply_operation(10, lambda x: x + 100)),
]

# --- Вивід у рамці ---
label_width = max(len(label) for label, _ in results)
value_width = max(len(str(v)) for _, v in results)
width = label_width + value_width + 5

print("\n┌" + "─" * width + "┐")
print("│" + "  APPLY_OPERATION()".center(width) + "│")
print("├" + "─" * width + "┤")
for label, value in results:
    print(f"│  {label.ljust(label_width)} │ {str(value).ljust(value_width)} │")
print("└" + "─" * width + "┘")

"""
┌───────────────────────────────────────────────────┐
│                  APPLY_OPERATION()                │
├───────────────────────────────────────────────────┤
│  apply_operation(5, double)                 │ 10   │
│  apply_operation(5, square)                 │ 25   │
│  apply_operation(37, celsius_to_fahrenheit) │ 98.6 │
│  apply_operation(10, lambda x: x + 100)     │ 110  │
└───────────────────────────────────────────────────┘
"""

"""
*Пояснення Callable[[float], float]:

from typing import Callable

Callable[[float], float]
#         ↑        ↑
#     аргументи  повертає
#     функції     (тип результату)

Читається як: "функція, що приймає один аргумент типу float і повертає float". 

*Загальний синтаксис:
Callable[[тип1, тип2, ...], тип_результату]

Callable[[float], float]             # f(x: float) -> float
Callable[[int, int], int]            # f(a: int, b: int) -> int
Callable[[str], bool]                # f(text: str) -> bool
Callable[[], None]                   # f() -> None  (без аргументів)

*Чому це краще, ніж просто operation без типу:
# ❌ Без типу — незрозуміло, ЩО саме очікує функція:
def apply_operation(value, operation):
    return operation(value)

# ✅ З Callable — IDE підказує, ЯКОЇ форми функцію передавати:
def apply_operation(value: float, operation: Callable[[float], float]) -> float:
    return operation(value)

# Якщо передати щось невідповідне — сучасні IDE (PyCharm, VS Code з Pylance)
# ПОПЕРЕДЯТЬ ще до запуску коду:
apply_operation(5, "не функція")   # ⚠️ підказка IDE: очікується Callable, не str

*Важливий нюанс: 
Callable — це підказка типу (type hint), а не перевірка часу виконання. 
Python не зупинить програму, якщо передати неправильний тип — це лише інформація для розробника й інструментів (IDE, mypy). 
Так само, як weight: float у calculate_bmi() з попередніх задач не забороняє передати рядок — просто "документує" очікування.

*Зв'язок із попереднім заняттям (передача функції як аргумент):
Це та сама ідея, що ти вже реалізовував раніше (Практика №8 "функція як аргумент") — тепер лише додано формальний тип Callable, що робить сигнатуру функції точнішою й зрозумілішою для читання, особливо у великих проєктах.
"""
