
## !🧠 Challenge №1 — знайди проблему!

#Що не так?
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / height_m ** 2
    print(bmi)

result = calculate_bmi(82, 180)
print(result)

"""
Питання: Що буде в result і чому?
Виправ функцію.
"""

#Відповідь: у result буде None.
#Чому саме None:

def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / height_m ** 2
    print(bmi)          # ← лише ДРУКУЄ значення на екран
    # немає return!     # ← функція нічого не ПОВЕРТАЄ

result = calculate_bmi(82, 180)
# Спершу виведеться: 25.30864197530864  (від print всередині)
# Потім: result = None  (бо функція неявно повертає None)

print(result)
# → None

"""
Головне правило Python: якщо у функції немає явного return, вона автоматично повертає None — незалежно від того, скільки всередині print(). 
Друк на екран і повернення значення — це дві абсолютно різні речі:

def f():
    print("щось")   # ← ЩОСЬ РОБИТЬ (side effect, видно людині)
    # немає return  # ← значення для коду НЕ передається

x = f()   # виведе "щось" на екран
print(x)  # None — бо f() нічого не return-ила

Це та сама помилка, яку ми розбирали в Практиці №1 ("не використовуй print() всередині функції") — тут вона проявляється на практиці й ламає подальший код.

Виправлена функція:
"""

def calculate_bmi(weight, height):
    """Обчислює BMI і ПОВЕРТАЄ число, а не друкує його."""
    height_m = height / 100
    bmi = weight / height_m ** 2
    return bmi          # ✅ тепер функція повертає значення


result = calculate_bmi(82, 180)
print(result)            # → 25.30864197530864 ✅ тепер працює правильно

"""
Чому це критично важливо на практиці — приклад "ланцюжка" помилок:

# Якщо хтось спробує ЩОСЬ ЗРОБИТИ з result у зіпсованій версії:
result = calculate_bmi(82, 180)   # спочатку надрукує число, result = None

if result > 25:          # 💥 TypeError: '>' not supported between 'NoneType' and 'int'
    print("Overweight")   # цей рядок НІКОЛИ не виконається через помилку вище

# У виправленій версії — все працює як очікується:
result = calculate_bmi(82, 180)     # result = 25.3...
if result > 25:                     # ✅ порівняння працює
    print("Overweight")             # ✅ виконується коректно

Підсумок — як розпізнати цю помилку в майбутньому: якщо десь у коді result неочікувано виявляється None, перша підозра — перевір, чи є return у відповідній функції, а не забув він там print() замість нього.
"""

# ==============================================================================
# ==============================================================================

## !🧠 Challenge №2 — mutable default argument!

"""
Не запускай код. Спрогнозуй:

def add_patient(name, patients=[]):
    patients.append(name)
    return patients


print(add_patient("Ivan"))
print(add_patient("Olena"))
print(add_patient("Petro"))

Який буде результат?
І головне: чому це небезпечний шаблон?
"""

"""
Прогноз результату:

['Ivan']
['Ivan', 'Olena']
['Ivan', 'Olena', 'Petro']

Це НЕ те, що очікує більшість новачків (вони думають, що буде ['Ivan'], ['Olena'], ['Petro'] — окремо кожного разу). Список накопичується між викликами!

Чому так відбувається — головна пастка Python:
Значення параметра за замовчуванням обчислюється РІВНО ОДИН РАЗ — у момент визначення функції, а не при кожному виклику:

def add_patient(name, patients=[]):   # ← [] створюється ОДИН РАЗ,
                                        #   коли Python читає def
    patients.append(name)
    return patients

Той самий об'єкт [] "прив'язується" до параметра patients назавжди, і кожен виклик без явного другого аргументу використовує один і той самий список у пам'яті:

add_patient("Ivan")    # patients — це список [X] (той самий об'єкт завжди)
                        # X.append("Ivan") → X = ['Ivan']
                        # повертає ['Ivan']

add_patient("Olena")   # patients — ЗНОВУ той самий об'єкт X!
                        # X.append("Olena") → X = ['Ivan', 'Olena']
                        # повертає ['Ivan', 'Olena']  ← Ivan досі тут!

Доказ через id() (з Практики №2 розділу "базові типи"):

def add_patient(name, patients=[]):
    print(id(patients))   # ← якщо додати цей рядок, побачиш ОДНАКОВЕ число
                            #   при КОЖНОМУ виклику — це підтверджує,
                            #   що це один і той самий об'єкт у пам'яті
    patients.append(name)
    return patients

print(add_patient("Ivan"))
print(add_patient("Olena"))
print(add_patient("Petro"))


['Ivan']
1973461418752
['Ivan', 'Olena']
1973461418752
['Ivan', 'Olena', 'Petro']


Чому це небезпечно на практиці:
Уявімо реальний сценарій:

def register_patient(name, history=[]):
    history.append(name)
    return history

morning_shift = register_patient("Ivan")     # ['Ivan']
evening_shift = register_patient("Olena")    # ['Ivan', 'Olena'] ← НЕСПОДІВАНО!

# morning_shift і evening_shift — це ОДИН І ТОЙ САМИЙ список!
print(morning_shift is evening_shift)   # True — оце вже серйозна проблема!
print(morning_shift)                     # ['Ivan', 'Olena'] — а мало бути тільки Ivan!

Це класична "прихована помилка" — код виглядає правильним, працює на перших тестах (де викликаєш функцію лише раз), але ламається в продакшн, коли функцію викликають багато разів — дані з різних викликів переплутуються між собою.

Правильне виправлення — None як прапорець:
"""
def add_patient(name, patients=None):
    if patients is None:
        patients = []          # ← НОВИЙ список створюється при КОЖНОМУ виклику
    patients.append(name)
    return patients


print(add_patient("Ivan"))    # ['Ivan']
print(add_patient("Olena"))   # ['Olena']  ✅ окремо, як і очікувалось
print(add_patient("Petro"))   # ['Petro']  ✅

"""
Чому None вирішує проблему: None — це незмінний (immutable) об'єкт, він не накопичує стан. При кожному виклику Python перевіряє if patients is None і, якщо так, створює новий, порожній список — саме тому кожен виклик отримує "чистий аркуш".

Правило "гарного тону" в Python: ніколи не використовуй змінні (mutable) типи — list, dict, set — як значення за замовчуванням у параметрах функції. Замість цього — None + перевірка всередині.
"""

# ==============================================================================
# ==============================================================================

## !🚀 Challenge №3 — Medical Text!

"""
Створи:
def normalize_medical_text(text: str) -> str:
    ...

Функція повинна:
-прибрати пробіли на початку/кінці;
-перевести текст у lowercase;
-замінити декілька пробілів одним;
-повернути очищений текст.

Наприклад:
"   Patient   has   fever   "
→
"patient has fever"

Підказка: можеш використати вже знайомі тобі strip(), split() і join().
"""

def normalize_medical_text(text: str) -> str:
    """Очищає та нормалізує медичний текст.

    Кроки:
    1. strip()  — прибирає пробіли з країв
    2. lower()  — переводить у нижній регістр
    3. split()+join() — схлопує кілька пробілів усередині в один
    """
    cleaned = text.strip()
    lowered = cleaned.lower()
    normalized = " ".join(lowered.split())
    return normalized


# --- Демонстрація роботи ---
test_cases = [
    "   Patient   has   fever   ",
    "ACUTE SINUSITIS",
    "  Cough\tand\n\nsore throat  ",
    "Normal text",
]

results = [(repr(text), repr(normalize_medical_text(text))) for text in test_cases]

# --- Вивід у рамці ---
label_width = max(len(label) for label, _ in results)
value_width = max(len(value) for _, value in results)
width = label_width + value_width + 5

print("\n┌" + "─" * width + "┐")
print("│" + "  NORMALIZE_MEDICAL_TEXT()".center(width) + "│")
print("├" + "─" * width + "┤")
for label, value in results:
    print(f"│  {label.ljust(label_width)} │ {value.ljust(value_width)} │")
print("└" + "─" * width + "┘")

"""
┌───────────────────────────────────────────────────────────┐
│                   NORMALIZE_MEDICAL_TEXT()                │
├───────────────────────────────────────────────────────────┤
│  '   Patient   has   fever   '   │ 'patient has fever'     │
│  'ACUTE SINUSITIS'               │ 'acute sinusitis'       │
│  '  Cough\tand\n\nsore throat  ' │ 'cough and sore throat' │
│  'Normal text'                   │ 'normal text'           │
└───────────────────────────────────────────────────────────┘
"""

"""
Пояснення кожного кроку (KISS — просто й читабельно):
text = "   Patient   has   fever   "

# Крок 1: strip() — прибирає пробіли ТІЛЬКИ з країв
cleaned = text.strip()
# → "Patient   has   fever"   (пробіли всередині лишились!)

# Крок 2: lower() — нижній регістр
lowered = cleaned.lower()
# → "patient   has   fever"

# Крок 3: split() без аргументів + join()
# split() розбиває по БУДЬ-ЯКІЙ кількості пробілів → список слів
lowered.split()
# → ['patient', 'has', 'fever']   ← подвійні пробіли зникли самі!

# join() збирає слова назад ЧЕРЕЗ РІВНО ОДИН пробіл
" ".join(['patient', 'has', 'fever'])
# → "patient has fever"   ✅ готово!

Чому саме split() + join(), а не .replace("  ", " "):
# ❌ replace() — крихкий підхід, не покриває всі випадки:

text.replace("  ", " ")   # замінює лише ПОДВІЙНИЙ пробіл на одинарний
"a   b".replace("  ", " ")   # → "a  b"  ← ще лишився подвійний! (3 пробіли → 2)
                              # треба було б викликати replace() кілька разів

# ✅ split() + join() — працює для БУДЬ-ЯКОЇ кількості пробілів одразу:
" ".join("a   b".split())   # → "a b"   ✅ незалежно від кількості пробілів

Це той самий трюк, що вже застосовувався у MedicalNote.__post_init__ — перевірена та надійна ідіома Python для нормалізації пробілів.

Це YAGNI в дії: функція робить рівно те, що просить завдання — 4 кроки, ніякого зайвого функціоналу (валідації, обробки спецсимволів, підтримки емодзі тощо), який "може знадобиться колись".
"""

# ==============================================================================
# ==============================================================================

## 🚀 Challenge №4 — MedAssistant

"""
Створи три окремі функції:

def calculate_bmi(weight: float, height: float) -> float:
    ...

def bmi_category(bmi: float) -> str:
    ...

def create_patient_summary(
    name: str,
    age: int,
    weight: float,
    height: float,
) -> str:
    ...

create_patient_summary() повинна використовувати перші дві функції, а не дублювати їхню логіку.

Приклад результату:
Patient: Ivan
Age: 42
BMI: 25.3
Category: Overweight

Це перше завдання, де ми свідомо тренуємо:
function
   ↓
function
   ↓
function
   ↓
final result
"""

"""
patient_summary.py

Three composable functions for MedAssistant, demonstrating function
composition: each function does ONE job, and the top-level function
orchestrates them without duplicating their logic.

    calculate_bmi()
          ↓  (returns a float)
    bmi_category()
          ↓  (returns a str)
    create_patient_summary()
          ↓  (returns the final formatted report)
    "Patient: Ivan / Age: 42 / BMI: 25.3 / Category: Overweight"
"""


def calculate_bmi(weight: float, height: float) -> float:
    """Calculate BMI from weight (kg) and height (cm).

    Args:
        weight: Patient's weight in kilograms. Must be > 0.
        height: Patient's height in centimeters. Must be > 0.

    Returns:
        float: The raw, unrounded BMI value.
    """
    assert weight > 0, "weight must be greater than 0"
    assert height > 0, "height must be greater than 0"

    height_m = height / 100
    return weight / (height_m ** 2)


def bmi_category(bmi: float) -> str:
    """Classify a BMI value into a standard category.

    Args:
        bmi: A BMI value, typically from calculate_bmi().

    Returns:
        str: "Underweight", "Normal", "Overweight", or "Obesity".
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def create_patient_summary(
    name: str,
    age: int,
    weight: float,
    height: float,
) -> str:
    """Build a formatted patient summary.

    Orchestrates calculate_bmi() and bmi_category() — it does NOT
    recompute BMI logic or reimplement category thresholds itself.
    This is the "function → function → function → final result"
    chain: each step's output becomes the next step's input.

    Args:
        name: Patient's name.
        age: Patient's age in years.
        weight: Patient's weight in kilograms.
        height: Patient's height in centimeters.

    Returns:
        str: A multi-line summary report.
    """
    bmi = calculate_bmi(weight, height)        # step 1 → float
    category = bmi_category(bmi)                # step 2 → str (uses step 1's output)

    return (                                     # step 3 → final formatted string
        f"Patient: {name}\n"
        f"Age: {age}\n"
        f"BMI: {bmi:.1f}\n"
        f"Category: {category}"
    )


# --- Demo ---
patients = [
    ("Ivan", 42, 82, 180),
    ("Olena", 35, 55, 165),
    ("Petro", 58, 95, 175),
]

summaries = [create_patient_summary(*p) for p in patients]

# --- Framed output ---
all_lines = []
for summary in summaries:
    all_lines.extend(summary.split("\n"))
    all_lines.append("─" * 20)
all_lines.pop()   # drop the trailing separator

width = max(len(line) for line in all_lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  PATIENT SUMMARIES".center(width) + "│")
print("├" + "─" * width + "┤")
for line in all_lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────────┐
│    PATIENT SUMMARIES   │
├────────────────────────┤
│  Patient: Ivan         │
│  Age: 42               │
│  BMI: 25.3             │
│  Category: Overweight  │
│  ────────────────────  │
│  Patient: Olena        │
│  Age: 35               │
│  BMI: 20.2             │
│  Category: Normal      │
│  ────────────────────  │
│  Patient: Petro        │
│  Age: 58               │
│  BMI: 31.0             │
│  Category: Obesity     │
└────────────────────────┘
"""

"""
Ланцюжок композиції, викладений явно:
def create_patient_summary(name, age, weight, height):
    bmi = calculate_bmi(weight, height)     # ① weight, height → float
    category = bmi_category(bmi)            # ② that float → str
    return f"...{bmi:.1f}...{category}..."  # ③ both combined → final string

Функція «create_patient_summary()» ніколи не перераховує значення «weight / (height/100)**2» і ніколи не перезаписує порогові значення < 18,5 / < 25 / < 30 — вона просто викликає дві функції, які вже вміють це робити, і передає дані між ними. Це DRY у найчистішому вигляді: формула ІМТ та порогові значення категорій існують саме в одному місці у всій програмі.

Чому це важливо — що станеться, якщо ви, навпаки, продублюєте цю логіку:

# ❌ ПОГАНО — дублювання логіки:
def create_patient_summary(name, age, weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)              # ← дублікат calculate_bmi()
    if bmi < 18.5:                              # ← дублікат bmi_category()
        category = "Underweight"
    # ...

# А тепер уявіть, що клініка вирішила, що для категорій BMI слід використовувати
# дещо інші порогові значення, запропоновані ВООЗ. Вам доведеться знайти й виправити цю
# логіку в КОЖНІЙ функції, де вона повторюється — легко пропустити одну,
# і тоді різні частини програми перестануть узгоджуватися між собою.

Чому *p у create_patient_summary(*p): 
p — це кортеж, наприклад, («Ivan», 42, 82, 180). 
Символ * розпаковує його на чотири окремі позиційні аргументи — це той самий механізм розпакування, що й у *args, тільки тут він використовується у зворотному напрямку 
(розподіляючи кортеж, а не об’єднуючи аргументи в один).
"""

# ==============================================================================
# ==============================================================================

## !🧠 Challenge №5 — рівень Junior+!

"""
Створи функцію:
def analyze_temperatures(
    temperatures: list[float],
) -> dict:
    ...

Вона повинна повернути:
{
    "normal": 3,
    "fever": 2,
    "high_fever": 1,
}

Використовуй окрему функцію:
classify_temperature()

яку ти вже створив у День 5.
Тобто цього разу ми починаємо перевикористовувати код із попередніх днів.
Це дуже важливий момент.
"""

def classify_temperature(temp: float) -> str:
    """Classify a single body temperature reading.

    (Same function as in the earlier MedAssistant temperature challenge —
    reused here, not duplicated.)
    """
    if temp < 37.5:
        return "Normal"
    elif temp < 39.0:
        return "Fever"
    else:
        return "High fever"


def analyze_temperatures(temperatures: list[float]) -> dict:
    """Count how many readings fall into each temperature category.

    Reuses classify_temperature() for the actual classification logic —
    this function's only job is counting, not re-deciding the thresholds.

    Args:
        temperatures: A list of body temperature readings in Celsius.

    Returns:
        dict: All three category keys always present (0 if unused):
            {"normal": int, "fever": int, "high_fever": int}
    """
    counts = {"normal": 0, "fever": 0, "high_fever": 0}

    for temp in temperatures:
        category = classify_temperature(temp)          # e.g. "High fever"
        key = category.lower().replace(" ", "_")        # → "high_fever"
        counts[key] += 1

    return counts


# --- Demo with a few test sets ---
test_sets = [
    ("Ward A", [36.6, 37.2, 38.1, 39.0, 37.8, 36.4]),
    ("Ward B", [36.1, 36.5, 36.9]),
    ("ICU",    [39.5, 40.1, 38.7, 39.2]),
]

results = [(label, analyze_temperatures(temps)) for label, temps in test_sets]

# --- Framed table output ---
header = f"{'Ward':<10} │ {'normal':>7} │ {'fever':>7} │ {'high_fever':>10}"
rows = [
    f"{label:<10} │ {counts['normal']:>7} │ {counts['fever']:>7} │ {counts['high_fever']:>10}"
    for label, counts in results
]

width = max(len(header), max(len(r) for r in rows)) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  TEMPERATURE ANALYSIS BY WARD".center(width) + "│")
print("├" + "─" * width + "┤")
print("│  " + header.ljust(width - 2) + "│")
print("│  " + "─" * (width - 4) + "│")
for row in rows:
    print("│  " + row.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌───────────────────────────────────────────────┐
│           TEMPERATURE ANALYSIS BY WARD        │
├───────────────────────────────────────────────┤
│  Ward       │  normal │   fever │ high_fever  │
│  ───────────────────────────────────────────│
│  Ward A     │       3 │       2 │          1  │
│  Ward B     │       3 │       0 │          0  │
│  ICU        │       0 │       1 │          3  │
└───────────────────────────────────────────────┘
"""

"""
Чому це — важливий момент перевикористання коду:

def analyze_temperatures(temperatures):
    counts = {"normal": 0, "fever": 0, "high_fever": 0}
    for temp in temperatures:
        category = classify_temperature(temp)   # ← ВИКЛИК готової функції,
        ...                                        #   а НЕ повторення її логіки

# ❌ ПОГАНО — дублювання порогів температури ВСЕРЕДИНІ analyze_temperatures():
def analyze_temperatures(temperatures):
    counts = {"normal": 0, "fever": 0, "high_fever": 0}
    for temp in temperatures:
        if temp < 37.5:              # ← та сама логіка, що вже є в classify_temperature()!
            counts["normal"] += 1
        elif temp < 39.0:
            counts["fever"] += 1
        else:
            counts["high_fever"] += 1
    return counts
    # ПРОБЛЕМА: якщо завтра пороги зміняться (напр. 37.5 → 37.8),
    # доведеться шукати і виправляти ДВА місця в коді — легко забути одне

Перетворення "High fever" → "high_fever":
"High fever".lower()               # → "high fever"
"high fever".replace(" ", "_")      # → "high_fever"

Це дозволяє не переписувати classify_temperature(), а лише "адаптувати" її результат під потрібний формат ключів словника — сама функція класифікації залишається недоторканою й однаковою скрізь, де вона використовується.

Чому всі три ключі — завжди в dict:
counts = {"normal": 0, "fever": 0, "high_fever": 0}   # ← ініціалізація ОДРАЗУ з усіма ключами

for temp in temperatures:
    counts[key] += 1   # тільки ЗБІЛЬШУЄМО існуючий ключ, ніколи не створюємо новий

Це зручніше для подальшого коду, який використає результат: не треба перевіряти if "high_fever" in counts — ключ гарантовано є, навіть якщо значення 0.
"""
