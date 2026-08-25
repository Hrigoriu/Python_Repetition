## Практика №1 — Базові умови
"""
Створи:
age = 42

Напиши програму, яка визначає:
< 18       → Minor
18–64      → Adult
65+        → Senior
"""

# Варіант 1 — класичний if/elif/else
age = 42

# if/elif/else — перевіряє умови зверху вниз,
# виконує перший блок, де умова True, решту ігнорує
if age < 18:
    category = "Minor"
elif age <= 64:            # сюди потрапляємо тільки якщо age >= 18
    category = "Adult"
else:                      # вік 65 і більше
    category = "Senior"

# --- Вивід у рамці ---
lines = [
    f"Вік:       {age}",
    f"Категорія: {category}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ВІКОВА КАТЕГОРІЯ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────┐
│   ВІКОВА КАТЕГОРІЯ │
├────────────────────┤
│  Вік:       42     │
│  Категорія: Adult  │
└────────────────────┘
"""

# Варіант 2 — match/case
age = 42

# match/case — Python 3.10+
# guard (if) у кожному case дозволяє перевіряти умови на діапазони
match age:
    case n if n < 18:
        category = "Minor"
    case n if n <= 64:
        category = "Adult"
    case _:                # _ — "за замовчуванням" (як else)
        category = "Senior"

print(f"Вік {age} → {category}")    # Вік 42 → Adult

#Варіант 3 — через функцію зі словником меж
age = 42

# Словник із межами категорій: (мінімум, максимум включно) → назва
age_categories = {
    (0, 17):  "Minor",
    (18, 64): "Adult",
    (65, 150): "Senior",
}

# Шукаємо першу пару меж, в яку потрапляє вік
category = next(
    label
    for (min_age, max_age), label in age_categories.items()
    if min_age <= age <= max_age
)

print(f"Вік {age} → {category}")    #Вік 42 → Adult
#==============================================================================

## Практика №2 — BMI

"""
Створи:
bmi = 27.4

Визнач категорію:

< 18.5       Underweight
18.5–24.9    Normal
25–29.9      Overweight
30+          Obesity

Важливо: зроби межі без перекриттів.
"""

#Варіант 1 — if/elif/else

bmi = 27.4

# Межі БЕЗ перекриттів: кожне значення потрапляє РІВНО в одну категорію
# < 18.5                → Underweight
# 18.5 <= bmi < 25.0   → Normal
# 25.0 <= bmi < 30.0   → Overweight
# 30.0 +               → Obesity

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25.0:      # сюди потрапляємо тільки якщо bmi >= 18.5
    category = "Normal"
elif bmi < 30.0:      # сюди — тільки якщо bmi >= 25.0
    category = "Overweight"
else:                 # bmi >= 30.0
    category = "Obesity"

# --- Вивід у рамці ---
lines = [
    f"BMI:       {bmi}",
    f"Категорія: {category}",
]
width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  BMI КАТЕГОРІЯ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────┐
│       BMI КАТЕГОРІЯ     │
├─────────────────────────┤
│  BMI:       27.4        │
│  Категорія: Overweight  │
└─────────────────────────┘
"""

#Варіант 2 — match/case

bmi = 27.4

# guard (if) у кожному case — перевірка діапазону
# _ (underscore) — "за замовчуванням", як else
match bmi:
    case n if n < 18.5:
        category = "Underweight"
    case n if n < 25.0:
        category = "Normal"
    case n if n < 30.0:
        category = "Overweight"
    case _:
        category = "Obesity"

print(f"BMI {bmi} → {category}")    # BMI 27.4 → Overweight

#==============================================================================

## Практика №3 — температура
"""
Користувач вводить температуру.

Програма повинна визначити:

< 36.0        Low
36.0–37.4     Normal
37.5–38.9     Fever
39+           High fever

Не забудь перетворити input() у float.
"""

# --- Отримання температури від користувача ---
while True:
    try:
        # input() завжди повертає str → float() перетворює на дробове число
        # якщо ввести "abc" замість числа — float() кине ValueError
        temp = float(input("Введіть температуру тіла (°C): "))

        # Додаткова перевірка: реалістичний діапазон для людини
        if not (25.0 <= temp <= 45.0):
            print("⚠ Введіть реалістичне значення (25.0–45.0 °C).\n")
            continue  # повертаємось на початок циклу

        break  # все гаразд — виходимо з циклу

    except ValueError:
        # float() кидає ValueError при нечисловому введенні (напр. "abc")
        print("⚠ Помилка: введіть число (наприклад: 36.6).\n")

# --- Визначення категорії (межі БЕЗ перекриттів) ---
if temp < 36.0:
    category = "Low"
    marker = "🔵"
elif temp < 37.5:      # Python вже знає: temp >= 36.0
    category = "Normal"
    marker = "🟢"
elif temp < 39.0:      # Python вже знає: temp >= 37.5
    category = "Fever"
    marker = "🟡"
else:                  # temp >= 39.0
    category = "High fever"
    marker = "🔴"

# --- Вивід у рамці ---
lines = [
    f"Температура: {temp:.1f} °C",
    f"Категорія:   {marker} {category}",
]
width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ТЕМПЕРАТУРНИЙ АНАЛІЗ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
Введіть температуру тіла (°C): 29.5
┌────────────────────────┐
│   ТЕМПЕРАТУРНИЙ АНАЛІЗ │
├────────────────────────┤
│  Температура: 29.5 °C  │
│  Категорія:   🔵 Low    │
└────────────────────────┘

Введіть температуру тіла (°C): 36
┌─────────────────────────┐
│    ТЕМПЕРАТУРНИЙ АНАЛІЗ │
├─────────────────────────┤
│  Температура: 36.0 °C   │
│  Категорія:   🟢 Normal  │
└─────────────────────────┘

Введіть температуру тіла (°C): 38
┌────────────────────────┐
│   ТЕМПЕРАТУРНИЙ АНАЛІЗ │
├────────────────────────┤
│  Температура: 38.0 °C  │
│  Категорія:   🟡 Fever  │
└────────────────────────┘

Введіть температуру тіла (°C): 42
┌─────────────────────────────┐
│      ТЕМПЕРАТУРНИЙ АНАЛІЗ   │
├─────────────────────────────┤
│  Температура: 42.0 °C       │
│  Категорія:   🔴 High fever  │
└─────────────────────────────┘
"""

#==============================================================================

## Практика №4 — логічні оператори

age = 42
has_id = True
is_banned = False

# --- Перевірка кожної умови окремо ---
cond_age     = age >= 18       # вік достатній?
cond_id      = has_id          # є ID?
cond_banned  = not is_banned   # НЕ заблокований?

# --- Фінальна умова: всі три мають бути True ---
# and повертає True ТІЛЬКИ якщо обидва операнди True
# not інвертує: not False → True, not True → False
access = cond_age and cond_id and cond_banned

# --- Збираємо список причин відмови (якщо є) ---
reasons = []
if not cond_age:
    reasons.append(f"❌ Вік {age} — менше 18 років")
if not cond_id:
    reasons.append("❌ Відсутній ID")
if not cond_banned:
    reasons.append("❌ Користувач заблокований")

# --- Формуємо рядки для виводу ---
lines = [
    f"Вік:          {age}",
    f"Є ID:         {has_id}",
    f"Заблокований: {is_banned}",
    "─" * 24,                          # розділювач всередині рамки
    f"Результат:    {'✅ Access granted' if access else '🚫 Access denied'}",
]

if reasons:
    lines.append("Причини відмови:")
    lines += [f"  {r}" for r in reasons]

# --- Вивід у рамці ---
width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ПЕРЕВІРКА ДОСТУПУ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
cond_banned  = not is_banned   # НЕ заблокований
┌──────────────────────────────────┐
│         ПЕРЕВІРКА ДОСТУПУ        │
├──────────────────────────────────┤
│  Вік:          42                │
│  Є ID:         True              │
│  Заблокований: False             │
│  ────────────────────────        │
│  Результат:    ✅ Access granted  │
└──────────────────────────────────┘

cond_banned  = is_banned   # Заблокований
┌─────────────────────────────────┐
│         ПЕРЕВІРКА ДОСТУПУ       │
├─────────────────────────────────┤
│  Вік:          42               │
│  Є ID:         True             │
│  Заблокований: True            │
│  ────────────────────────       │
│  Результат:    🚫 Access denied  │
│  Причини відмови:               │
│    ❌ Користувач заблокований    │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│         ПЕРЕВІРКА ДОСТУПУ       │
├─────────────────────────────────┤
│  Вік:          12               │
│  Є ID:         False            │
│  Заблокований: True            │
│  ────────────────────────       │
│  Результат:    🚫 Access denied  │
│  Причини відмови:               │
│    ❌ Вік 12 — менше 18 років    │
│    ❌ Відсутній ID               │
│    ❌ Користувач заблокований    │
└─────────────────────────────────┘
"""

#==============================================================================

## Практика №5 — медична логіка

"""
Створи:
temperature = 38.7
cough = True
sore_throat = True

Правило:
temperature >= 38
AND
cough == True
AND
sore_throat == True

→
Respiratory symptoms detected

Інакше:
Criteria not met
"""

temperature = 38.7
cough = True
sore_throat = True

# --- Перевірка кожної умови окремо ---
cond_temp        = temperature >= 38.0   # температура достатня?
cond_cough       = cough                 # є кашель?
cond_sore_throat = sore_throat           # є біль у горлі?

# --- Фінальна умова: ВСІ три мають бути True ---
# cough == True можна скоротити просто до cough
# (bool-змінна вже є True або False, == True зайве)
detected = cond_temp and cond_cough and cond_sore_throat

# --- Допоміжна функція: перетворює True/False на значок ---
def status(condition: bool) -> str:
    return "✅" if condition else "❌"

# --- Формуємо рядки для виводу ---
lines = [
    f"Температура:  {temperature} °C  {status(cond_temp)}  (потрібно >= 38.0)",
    f"Кашель:       {cough}        {status(cond_cough)}",
    f"Біль у горлі: {sore_throat}        {status(cond_sore_throat)}",
    "─" * 30,
    f"Результат: {'🔴 Respiratory symptoms detected' if detected else '🟢 Criteria not met'}",
]

# --- Вивід у рамці ---
width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  МЕДИЧНА ДІАГНОСТИКА".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────────────────────────────────┐
│               МЕДИЧНА ДІАГНОСТИКА              │
├────────────────────────────────────────────────┤
│  Температура:  38.7 °C  ✅  (потрібно >= 38.0)  │
│  Кашель:       True        ✅                   │
│  Біль у горлі: True        ✅                   │
│  ──────────────────────────────                │
│  Результат: 🔴 Respiratory symptoms detected    │
└────────────────────────────────────────────────┘
"""

#=============================================================================

## Практика №6 — match/case

"""
Створи:

severity = "moderate"

Використовуючи match/case, виведи:
mild     → Low priority
moderate → Medium priority
severe   → High priority
critical → Emergency
"""

severity = "moderate"

# --- Варіант 1: match/case (Python 3.10+) ---
# match перевіряє значення змінної проти конкретних "зразків" (patterns)
match severity:
    case "mild":
        priority = "Low priority"
        marker = "🟢"
    case "moderate":
        priority = "Medium priority"
        marker = "🟡"
    case "severe":
        priority = "High priority"
        marker = "🔴"
    case "critical":
        priority = "Emergency"
        marker = "🚨"
    case _:
        # _ — "wildcard": спрацьовує якщо жоден case вище не підійшов
        priority = "Unknown severity"
        marker = "⚪"

# --- Вивід у рамці ---
lines = [
    f"Severity: {severity}",
    f"Priority: {marker} {priority}",
]
width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  MEDICAL TRIAGE".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")


# --- Варіант 2: if/elif/else (будь-яка версія Python) ---
if severity == "mild":
    priority_2 = "Low priority"
elif severity == "moderate":
    priority_2 = "Medium priority"
elif severity == "severe":
    priority_2 = "High priority"
elif severity == "critical":
    priority_2 = "Emergency"
else:
    priority_2 = "Unknown severity"


"""
┌───────────────────────────────┐
│          MEDICAL TRIAGE       │
├───────────────────────────────┤
│  Severity: moderate           │
│  Priority: 🟡 Medium priority │
└───────────────────────────────┘
"""
