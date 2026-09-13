"""
# !Task 1 — basic ValueError!

Створи:
def parse_age(value: str) -> int:
    ...

Функція повинна:
перетворити рядок у int;
повернути число;
якщо перетворення неможливе — підняти ValueError.
"""

def parse_age(value: str) -> int:
    """Перетворює рядок у вік (ціле, невід'ємне число).

    Raises:
        ValueError: Якщо рядок не є числом, АБО якщо число від'ємне.
    """
    age = int(value)   # природний ValueError, якщо value НЕ є цілим числом

    if age < 0:
        raise ValueError(f"Вік не може бути від'ємним: {age}")

    return age


# --- Демонстрація ---
test_values = ["42", "abc", "-5", "0", "17.5"]
results = []

for value in test_values:
    try:
        age = parse_age(value)
        results.append((value, f"✅ {age}"))
    except ValueError as e:
        results.append((value, f"❌ ValueError: {e}"))

# --- Вивід у рамці ---
lines = [f"parse_age({value!r})  →  {result}" for value, result in results]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  PARSE_AGE()".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                                      PARSE_AGE()                                     │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  parse_age('42')  →  ✅ 42                                                           │
│  parse_age('abc')  →  ❌ ValueError: invalid literal for int() with base 10: 'abc'   │
│  parse_age('-5')  →  ❌ ValueError: Вік не може бути від'ємним: -5                   │
│  parse_age('0')  →  ✅ 0                                                             │
│  parse_age('17.5')  →  ❌ ValueError: invalid literal for int() with base 10: '17.5' │
└──────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
#*Пояснення двох джерел ValueError в одній функції:
age = int(value)

Тут ValueError виникає природно, від самого int() — Python сам кидає цю помилку, якщо рядок неможливо перетворити на ціле число:

int("42")       # → 42       (успішно)
int("abc")      # → 💥 ValueError: invalid literal for int() with base 10: 'abc'
int("17.5")     # → 💥 ValueError: invalid literal for int() with base 10: '17.5'
#                    (int() НЕ округлює рядок з крапкою — просто НЕ розпізнає його як ціле)

if age < 0:
    raise ValueError(f"Вік не може бути від'ємним: {age}")

А тут ValueError кидається вручну, вже за нашою власною логікою — навіть якщо int("-5") успішно дає число -5 (жодної помилки перетворення немає!), ми самі вирішуємо, що від'ємний вік — це семантично некоректно, і кидаємо помилку навмисно.

#*Ключова відмінність цих двох ValueError:
	            int(value) 	                            raise ValueError(...) 
                кидає ValueError                        вручну
Причина	        рядок узагалі НЕ схожий 	            рядок ЦІЛКОМ валідний як число, 
                на ціле число                           але не має сенсу для нашої задачі
Хто вирішує	    Python 	                                ми (бізнес-логіка/сенс даних)
                (вбудована перевірка синтаксису)
Приклад	        "abc", "17.5"	                        "-5" (технічно ціле число, 
                                                        але вік не може бути від'ємним)

#*Чому не варто "ловити" ValueError від int() усередині самої parse_age():
# ❌ Якби ми "проковтнули" помилку тут:
def parse_age(value):
    try:
        age = int(value)
    except ValueError:
        return None   # ← тепер функція повертає None замість помилки!
    if age < 0:
        raise ValueError(...)
    return age

# Це порушило б ЧЕСНІСТЬ функції — сигнатура каже "повертає int",
# а насправді іноді повертає None. Викликач мусив би ЩОРАЗУ перевіряти
# і на None, і на можливий ValueError — заплутано і непослідовно.

#*Правильний підхід — дозволити ОБОМ типам помилок "спливати" назовні:
def parse_age(value):
    age = int(value)          # якщо тут помилка — вона сама "спливає" вгору
    if age < 0:
        raise ValueError(...)  # і ця теж
    return age
    # ФУНКЦІЯ ЗАВЖДИ: або повертає int, або кидає ValueError — нічого посередині

Це той самий принцип "чесної" функції з попереднього дня (divide(), calculate_bmi() з assert): або гарантований коректний результат, або явна, зрозуміла помилка — ніколи не "тихе" повернення чогось невизначеного.
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 2 — positive age!

Розшир функцію:
def parse_age(value: str) -> int:
    ...

Правила:
"42" → 42
"0" → ValueError
"-5" → ValueError
"abc" → ValueError

Тобто:
if age <= 0:
    raise ValueError(...)
"""

def parse_age(value: str) -> int:
    """Перетворює рядок у вік (ціле, СУВОРО додатне число, > 0).

    Raises:
        ValueError: Якщо рядок не є числом, АБО якщо число <= 0.
    """
    age = int(value)   # природний ValueError, якщо value НЕ є цілим числом

    if age <= 0:   # ← ЗМІНЕНО: було "< 0", тепер "<= 0"
        raise ValueError(f"Вік має бути більшим за 0, отримано: {age}")

    return age


# --- Демонстрація за правилами з умови ---
test_values = ["42", "0", "-5", "abc"]
results = []

for value in test_values:
    try:
        age = parse_age(value)
        results.append((value, f"✅ {age}"))
    except ValueError as e:
        results.append((value, f"❌ ValueError: {e}"))

# --- Вивід у рамці ---
lines = [f"parse_age({value!r})  →  {result}" for value, result in results]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  PARSE_AGE() — ТІЛЬКИ ДОДАТНІ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────────────────────────────────────────────────────────────────────┐
│                             PARSE_AGE() — ТІЛЬКИ ДОДАТНІ                           │
├────────────────────────────────────────────────────────────────────────────────────┤
│  parse_age('42')  →  ✅ 42                                                         │
│  parse_age('0')  →  ❌ ValueError: Вік має бути більшим за 0, отримано: 0          │
│  parse_age('-5')  →  ❌ ValueError: Вік має бути більшим за 0, отримано: -5        │
│  parse_age('abc')  →  ❌ ValueError: invalid literal for int() with base 10: 'abc' │
└────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
#*Що саме змінилось порівняно з Task 1:
# Task 1 — від'ємні заборонені, але 0 ДОЗВОЛЕНИЙ:
if age < 0:
    raise ValueError(...)
# parse_age("0") → ✅ 0   (нуль — валідний вік)

# Task 2 — і 0, і від'ємні заборонені:
if age <= 0:
    raise ValueError(...)
# parse_age("0") → ❌ ValueError   (нуль тепер НЕВАЛІДНИЙ вік)

#*Пояснення різниці < vs <= — одна змінена буква, кардинально інша поведінка:
age < 0     # True ЛИШЕ для: -1, -2, -3, ...           (0 НЕ входить)
age <= 0    # True для: -1, -2, -3, ... ТА для 0 ТЕЖ    (0 ВХОДИТЬ)

Це той самий тип "межової" помилки, що вже розбирався в BMI-задачах ("межі без перекриттів") — тут навпаки: одна зайва (чи відсутня) риска = повністю змінює, чи потрапляє межове значення (0) у "заборонену" зону.

#*Перевірка по всіх чотирьох правилах з умови:
parse_age("42")   # int("42")=42 → 42 <= 0? Ні  → повертає 42       ✅
parse_age("0")     # int("0")=0   → 0 <= 0? Так  → ValueError         ✅
parse_age("-5")     # int("-5")=-5 → -5 <= 0? Так → ValueError          ✅
parse_age("abc")     # int("abc") → 💥 ValueError ВІД int() одразу        ✅

Усі чотири випадки з умови задачі відповідають очікуваному результату.

Чому "вік = 0" тепер вважається некоректним — практичний сенс:

У медичному контексті (MedAssistant), для якого будується ця валідація, вік рівний 0 зазвичай означає відсутність даних (незаповнене поле, значення "за замовчуванням"), а не реальний вік немовляти — для новонароджених прийнято записувати вік у місяцях чи днях, а не "0 років". Тому age <= 0 — розумніше правило, ніж age < 0, якщо мета — відловити як явно помилкові, так і підозріло "порожні" значення.
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 3 — safe input!

Напиши:
def safe_parse_age(value: str) -> int | None:
    ...

Функція повинна:
використати try/except;
повернути число при успіху;
повернути None, якщо input неправильний.
"""

def parse_age(value: str) -> int:
    """Перетворює рядок у вік (ціле, СУВОРО додатне число, > 0).

    (Перевикористано з Task 2 — не дублюємо логіку валідації.)
    """
    age = int(value)
    if age <= 0:
        raise ValueError(f"Вік має бути більшим за 0, отримано: {age}")
    return age


def safe_parse_age(value: str) -> int | None:
    """Безпечна версія parse_age() — ловить помилку, повертає None.

    Перевикористовує parse_age() (DRY): уся логіка валідації
    залишається в ОДНОМУ місці, тут лише додається "запобіжник".
    """
    try:
        return parse_age(value)
    except ValueError as e:
        print(f"⚠ Попередження: не вдалося розпізнати вік ({e}). Повертаю None.")
        return None


# --- Демонстрація ---
test_values = ["42", "0", "-5", "abc", "17"]
results = [(value, safe_parse_age(value)) for value in test_values]

# --- Вивід у рамці ---
lines = [f"safe_parse_age({value!r})  →  {result}" for value, result in results]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  SAFE_PARSE_AGE()".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
⚠ Попередження: не вдалося розпізнати вік (Вік має бути більшим за 0, отримано: 0). Повертаю None.
⚠ Попередження: не вдалося розпізнати вік (Вік має бути більшим за 0, отримано: -5). Повертаю None.
⚠ Попередження: не вдалося розпізнати вік (invalid literal for int() with base 10: 'abc'). Повертаю None.

┌──────────────────────────────────┐
│          SAFE_PARSE_AGE()        │
├──────────────────────────────────┤
│  safe_parse_age('42')  →  42     │
│  safe_parse_age('0')  →  None    │
│  safe_parse_age('-5')  →  None   │
│  safe_parse_age('abc')  →  None  │
│  safe_parse_age('17')  →  17     │
└──────────────────────────────────┘
"""

"""
#*Пояснення, як safe_parse_age() "обгортає" parse_age():
def safe_parse_age(value):
    try:
        return parse_age(value)   # ← викликаємо ГОТОВУ функцію
    except ValueError as e:
        print(f"⚠ ...")
        return None

- parse_age() сама по собі — "сувора" функція: вона кидає ValueError, якщо щось не так, і ніколи не повертає нічого "проміжного". 
- safe_parse_age() не змінює цю поведінку — вона просто ловить цю помилку зовні й перетворює її на безпечний None.

#* Ключова архітектурна ідея — два рівні "суворості" над однією логікою:
# "Сувора" версія (Task 2) — для контексту, де помилка МАЄ зупинити програму:
age = parse_age(user_input)   # 💥 якщо невалідно — програма падає з ValueError

# "Безпечна" версія (Task 3) — для контексту, де хочеш ПРОДОВЖИТИ роботу:
age = safe_parse_age(user_input)   # None, якщо невалідно — програма ПРОДОВЖУЄ працювати
if age is not None:
    print(f"Вік: {age}")
else:
    print("Пропускаю запис через некоректні дані")

Це не два незалежних способи парсингу — це одна логіка (parse_age()), обгорнута в різні стратегії обробки помилок залежно від того, де саме її викликають:

# Наприклад, обробка ЦІЛОГО файлу з даними пацієнтів:
ages_raw = ["42", "0", "-5", "abc", "17"]

# Якщо ОДИН некоректний запис не повинен зупиняти обробку ВСІХ інших:
valid_ages = []
for raw in ages_raw:
    age = safe_parse_age(raw)   # ← "безпечна" версія — не падає
    if age is not None:
        valid_ages.append(age)

print(valid_ages)   # [42, 17]  — некоректні записи просто пропущені

#*Чому попередження виводиться саме в safe_parse_age(), а не в parse_age():
def parse_age(value):
    age = int(value)
    if age <= 0:
        raise ValueError(...)   # ← НЕ друкує нічого, лише кидає помилку
    return age

def safe_parse_age(value):
    try:
        return parse_age(value)
    except ValueError as e:
        print(f"⚠ ...")   # ← друк ТУТ, у "зовнішньому" шарі
        return None

parse_age() — "чиста" функція без побічних ефектів (не друкує нічого сама, лише обчислює або кидає помилку — той самий принцип, що вже застосовувався в patient_utils.py/statistics_utils.py). Відповідальність за те, як повідомити про проблему користувачу, лежить на "зовнішньому" шарі — safe_parse_age() — що дозволяє іншому коду викликати parse_age() напряму (наприклад, там, де попередження в консоль було б недоречним) без зайвого друку.
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 4 — several exceptions!

Створи:
def get_patient_age(patient: dict) -> int:
    ...

Протестуй:
{"name": "Ivan", "age": 42}
{"name": "Olena"}
{"name": "Petro", "age": "61"}

Оброби ситуації:
KeyError;
TypeError або ValueError, де це доречно.
"""

# --- Спільна логіка отримання поля "age" з обробкою KeyError ---
def _get_age_field(patient: dict):
    """Дістає сире значення 'age' з dict, з ЗРОЗУМІЛИМ повідомленням про KeyError."""
    try:
        return patient["age"]
    except KeyError:
        raise KeyError(f"У записі пацієнта відсутнє поле 'age': {patient}")


# ═══════════════════════════════════════════
# ВАРІАНТ A — СУВОРИЙ: age МАЄ БУТИ вже int, інакше TypeError
# ═══════════════════════════════════════════
def get_patient_age_strict(patient: dict) -> int:
    """Повертає вік пацієнта. Вимагає, щоб 'age' був САМЕ int."""
    age = _get_age_field(patient)

    if not isinstance(age, int):
        raise TypeError(
            f"'age' має бути int, отримано {type(age).__name__}: {age!r}"
        )

    return age


# ═══════════════════════════════════════════
# ВАРІАНТ B — ПОБЛАЖЛИВИЙ: намагається конвертувати через int()
# ═══════════════════════════════════════════
def get_patient_age_flexible(patient: dict) -> int:
    """Повертає вік пацієнта. Намагається конвертувати age через int()."""
    age = _get_age_field(patient)

    try:
        return int(age)
    except TypeError:
        # int(None), int([1, 2]) — коли ТИП взагалі непридатний для конвертації
        raise TypeError(f"Неможливо перетворити age={age!r} у число (непридатний тип)")
    except ValueError:
        # int("abc") — коли це РЯДОК, але не схожий на число
        raise ValueError(f"Неможливо перетворити age={age!r} у число (не є числовим значенням)")


# --- Тестові дані ---
patients = [
    {"name": "Ivan", "age": 42},
    {"name": "Olena"},
    {"name": "Petro", "age": "61"},
    {"name": "Sofia", "age": "abc"},   # додатковий приклад для ValueError
    {"name": "Dmytro", "age": None},    # додатковий приклад для TypeError
]

# --- Демонстрація ОБОХ варіантів ---
def run_demo(func, patients):
    results = []
    for patient in patients:
        try:
            age = func(patient)
            results.append((patient, f"✅ {age}"))
        except KeyError as e:
            results.append((patient, f"❌ KeyError: {e}"))
        except TypeError as e:
            results.append((patient, f"❌ TypeError: {e}"))
        except ValueError as e:
            results.append((patient, f"❌ ValueError: {e}"))
    return results

results_strict = run_demo(get_patient_age_strict, patients)
results_flexible = run_demo(get_patient_age_flexible, patients)

# --- Вивід у рамці ---
lines = ["ВАРІАНТ A (strict):"]
for patient, result in results_strict:
    lines.append(f"  {patient}  →  {result}")
lines.append("─" * 60)
lines.append("ВАРІАНТ B (flexible):")
for patient, result in results_flexible:
    lines.append(f"  {patient}  →  {result}")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  GET_PATIENT_AGE()".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                     GET_PATIENT_AGE()   │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│  ВАРІАНТ A (strict):   │
│    {'name': 'Ivan', 'age': 42}  →  ✅ 42    │
│    {'name': 'Olena'}  →  ❌ KeyError: "У записі пацієнта відсутнє поле 'age': {'name': 'Olena'}"    │
│    {'name': 'Petro', 'age': '61'}  →  ❌ TypeError: 'age' має бути int, отримано str: '61'    │
│    {'name': 'Sofia', 'age': 'abc'}  →  ❌ TypeError: 'age' має бути int, отримано str: 'abc'    │
│    {'name': 'Dmytro', 'age': None}  →  ❌ TypeError: 'age' має бути int, отримано NoneType: None    │
│  ────────────────────────────────────────────────────────────   │
│  ВАРІАНТ B (flexible):   │
│    {'name': 'Ivan', 'age': 42}  →  ✅ 42    │
│    {'name': 'Olena'}  →  ❌ KeyError: "У записі пацієнта відсутнє поле 'age': {'name': 'Olena'}"    │
│    {'name': 'Petro', 'age': '61'}  →  ✅ 61    │
│    {'name': 'Sofia', 'age': 'abc'}  →  ❌ ValueError: Неможливо перетворити age='abc' у число (не є числовим значенням)  │
│    {'name': 'Dmytro', 'age': None}  →  ❌ TypeError: Неможливо перетворити age=None у число (непридатний тип)    │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
#*Пояснення різниці для трьох заданих тестів:
# Ivan: {"name": "Ivan", "age": 42}
get_patient_age_strict(...)     # age=42 — вже int → ✅ 42
get_patient_age_flexible(...)   # int(42)=42 → ✅ 42
# ОБИДВА варіанти дають однаковий результат — тут різниці немає

# Olena: {"name": "Olena"}  (немає ключа "age")
get_patient_age_strict(...)     # ❌ KeyError (в ОБОХ — це трапляється ДО перевірки типу)
get_patient_age_flexible(...)   # ❌ KeyError (те саме)
# КЛЮЧОВИЙ момент: KeyError обробляється ОДНАКОВО в обох варіантах,
# бо перевіряється до будь-якої логіки типу/конвертації

# Petro: {"name": "Petro", "age": "61"}  (age — РЯДОК)
get_patient_age_strict(...)     # ❌ TypeError: 'age' має бути int, отримано str: '61'
get_patient_age_flexible(...)   # ✅ 61  (int("61") успішно конвертується)
# ТУТ різниця найпомітніша!

#*Пояснення TypeError vs ValueError у Варіанті B — коли яка виникає:
int("61")    # → 61      успішно
int("abc")   # 💥 ValueError: invalid literal for int() with base 10: 'abc'
#              ↑ РЯДОК, але НЕ схожий на число — ValueError

int(None)    # 💥 TypeError: int() argument must be a string, a bytes-like object
#                            or a real number, not 'NoneType'
#              ↑ ТИП взагалі НЕПРИДАТНИЙ для int() — TypeError

int([1, 2])  # 💥 TypeError: int() argument must be a string, ...
#              ↑ те саме — список НЕ конвертується в число ЖОДНИМ чином

#*Загальне правило Python, яке тут проявляється:
Помилка	    Коли виникає
KeyError	шукаєш ключ, якого немає в dict
TypeError	операція застосована до непридатного типу (не рядок, не число)
ValueError	тип правильний (рядок), але значення всередині не має сенсу

#*Коли обирати Варіант A (strict) vs Варіант B (flexible):
# Варіант A — коли ДАНІ мають бути СУВОРО валідовані заздалегідь
# (наприклад, дані з БД, де тип уже гарантований схемою):
get_patient_age_strict(patient)   # ловить БУДЬ-ЯКЕ відхилення від int як помилку

# Варіант B — коли ДАНІ приходять із "неохайного" джерела
# (наприклад, CSV-файл чи форма введення, де все — рядки за замовчуванням):
get_patient_age_flexible(patient)   # толерантний до "61" замість 61
"""

# ==============================================================================
# ==============================================================================

"""
# !Task 5 — else!

Створи програму:
Enter age
    ↓
try int()
    ↓
except ValueError
    ↓
else → print valid age

Тут важливо побачити різницю між кодом, який може впасти, та кодом, який виконується після успішного виконання.
"""

#Варіант A — інтерактивний input():
age_input = input("Enter age: ")

try:
    age = int(age_input)   # ← код, який МОЖЕ впасти (ValueError)
except ValueError:
    print(f"⚠ '{age_input}' не є коректним віком.")
else:
    # else виконується ТІЛЬКИ якщо try завершився БЕЗ жодної помилки
    print(f"✅ Valid age: {age}")

"""
Enter age: 2.6
⚠ '2.6' не є коректним віком.

Enter age: 56
✅ Valid age: 56

Enter age: -5
✅ Valid age: -5

Enter age: 0
✅ Valid age: 0

Enter age: -0
✅ Valid age: 0

Enter age: boy
⚠ 'boy' не є коректним віком.
"""

test_inputs = ["42", "abc", "0", "-5", "17.5"]
results = []

for age_input in test_inputs:
    try:
        age = int(age_input)              # ← код, який МОЖЕ впасти
    except ValueError:
        results.append((age_input, "❌ Invalid age (not a number)"))
    else:
        # else — ТІЛЬКИ якщо try спрацював УСПІШНО, БЕЗ винятку
        results.append((age_input, f"✅ Valid age: {age}"))

# --- Вивід у рамці ---
lines = [f"Enter age: {inp!r:>8}  →  {result}" for inp, result in results]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  TRY / EXCEPT / ELSE".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────────────────────────────────────────┐
│                   TRY / EXCEPT / ELSE                  │
├────────────────────────────────────────────────────────┤
│  Enter age:     '42'  →  ✅ Valid age: 42               │
│  Enter age:    'abc'  →  ❌ Invalid age (not a number)  │
│  Enter age:      '0'  →  ✅ Valid age: 0                │
│  Enter age:     '-5'  →  ✅ Valid age: -5               │
│  Enter age:   '17.5'  →  ❌ Invalid age (not a number)  │
└────────────────────────────────────────────────────────┘
"""

"""
#*Головна ідея цього завдання — навіщо потрібен else:
try:
    age = int(age_input)   # блок, де МОЖЕ статись помилка
except ValueError:
    ...                     # виконується ТІЛЬКИ якщо ВИНИКЛА помилка
else:
    ...                     # виконується ТІЛЬКИ якщо ПОМИЛКИ НЕ БУЛО

#*Чому else, а не просто написати код "після" try/except:
# ❌ Без else — код ПІСЛЯ try/except виконається ЗАВЖДИ,
#    незалежно від того, була помилка чи ні:
try:
    age = int(age_input)
except ValueError:
    print("Помилка")
print(f"Valid age: {age}")   # 💥 NameError, якщо ValueError спрацював!
                               #    (age взагалі НЕ БУЛО присвоєно)

# ✅ З else — цей код ГАРАНТОВАНО виконається ЛИШЕ якщо age ІСНУЄ:
try:
    age = int(age_input)
except ValueError:
    print("Помилка")
else:
    print(f"Valid age: {age}")   # ✅ безпечно — age точно існує тут

Це і є ключова відмінність, про яку каже завдання:

"код, який може впасти" (усередині try) проти "код, який виконується після успішного виконання" (усередині else)

try:
    age = int(age_input)
    #     ↑ це "код, який МОЖЕ впасти"
    #       має бути МІНІМАЛЬНИМ — лише сама ризикована операція
except ValueError:
    ...
else:
    print(f"Valid age: {age}")
    #     ↑ це "код, який виконується ПІСЛЯ успіху"
    #       гарантовано працює з ВЖЕ валідним значенням

#*Практична перевага — try-блок стає "вузьким" і точним:
# ❌ Якщо покласти ЗАЙВИЙ код у try — можна ненавмисно "проковтнути"
#    помилку, яка НЕ стосується int():
try:
    age = int(age_input)
    process_patient(age)   # ← якщо ТУТ станеться ValueError з ІНШОЇ причини,
                              #    except все одно його "спіймає" — і ти НЕ ЗРОЗУМІЄШ,
                              #    що саме зламалось: перетворення чи обробка

#* ✅ else тримає "успішний" код ПОЗА try — except ловить ЛИШЕ те,
#    що дійсно стосується int():
try:
    age = int(age_input)
except ValueError:
    print("Помилка перетворення")
else:
    process_patient(age)   # ← якщо ТУТ станеться помилка — вона НЕ буде
                              #    помилково "приписана" до int()

*Зв'язок із for/else (попередній день): 
та сама філософія else, що вже зустрічалась у циклах — там else спрацьовував "якщо break НЕ трапився", тут — "якщо винятку НЕ трапилось". 
В обох випадках else відповідає на питання: "чи все пройшло без несподіванок?"
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 6 — finally!

Зроби демонстрацію:
try:
    ...
except ValueError:
    ...
finally:
    print("Validation finished")

Перевір обидва випадки:
correct input
incorrect input
"""

test_inputs = ["42", "abc"]   # correct input, incorrect input

for age_input in test_inputs:
    print(f"\n--- Enter age: '{age_input}' ---")

    try:
        age = int(age_input)
    except ValueError:
        print(f"❌ '{age_input}' — invalid age")
    else:
        print(f"✅ Valid age: {age}")
    finally:
        print("Validation finished")

"""
--- Enter age: '42' ---
✅ Valid age: 42
Validation finished

--- Enter age: 'abc' ---
❌ 'abc' — invalid age
Validation finished
"""

"""
*Пояснення повної конструкції try/except/else/finally — чотири блоки, чотири різні ролі:
try:
    age = int(age_input)      # ① код, який МОЖЕ впасти
except ValueError:
    print("...")                # ② виконується ТІЛЬКИ якщо БУЛА помилка
else:
    print("...")                 # ③ виконується ТІЛЬКИ якщо помилки НЕ БУЛО
finally:
    print("Validation finished")  # ④ виконується ЗАВЖДИ — незалежно від ①②③

*Головна унікальність finally — виконується у ВСІХ випадках, без винятку:
Сценарій                    except    else    finally
────────────────────────────────────────────────────────────────
"42"    (успіх)             ❌        ✅        ✅
"abc"    (ValueError)       ✅        ❌        ✅

finally — єдиний блок із цих чотирьох, що спрацьовує у обох рядках таблиці. Саме тому в результатах вище рядок "Validation finished" з'являється після кожного запису, незалежно від того, чи був вхід коректним.

*Практична демонстрація "непохитності" finally — навіть при непередбаченій помилці:
try:
    age = int("abc")
except TypeError:        # ⚠️ навмисно НЕПРАВИЛЬНИЙ тип винятку (не ValueError!)
    print("Це не спрацює")
finally:
    print("Все одно виконається")

# Результат:
# Все одно виконається
# 💥 ValueError: invalid literal for int()...  (програма ВСЕ ОДНО впаде,
#                                                  бо except ловив НЕ той тип)

Навіть якщо помилка не була "спіймана" відповідним except (і програма зрештою впаде), finally встигає виконатись першим, перш ніж помилка "вилетить" далі й зупинить програму. Це робить finally ідеальним місцем для гарантованого очищення ресурсів — наприклад, закриття файлу чи з'єднання з базою даних — незалежно від того, що саме сталось усередині try.

*Аналогія з with open() (попередній день) — навіщо це насправді потрібно на практиці:
# Це схоже на те, ЩО РОБИТЬ with open() "під капотом":
file = open("data.txt")
try:
    process(file)          # може впасти з будь-якою помилкою
finally:
    file.close()            # файл ЗАВЖДИ закриється — і при успіху, і при помилці

# Саме тому конструкція with (з Task 1 попереднього дня) —
# це, по суті, "готовий" try/finally, який Python пише за тебе автоматично

*Порядок виконання блоків — важливо запам'ятати:
try:       # завжди виконується першим
except:    # АБО else — виконується один з двох, залежно від результату try
else:      # (взаємовиключні між собою)
finally:   # ЗАВЖДИ виконується останнім, після try І (except АБО else)
"""
