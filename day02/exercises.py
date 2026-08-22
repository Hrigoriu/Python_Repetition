# Практика №1
"""
Напиши програму, яка:

створює змінні всіх базових типів;
виводить їх значення;
виводить їх тип через type().
"""

# --- Змінні всіх базових типів (крипто-тематика) ---
coin_name = "Bitcoin"  # str
price_usd = 64250.75  # float
active_wallets = 48_500_000  # int
is_bullish = True  # bool
top_coins = ["Bitcoin", "Ethereum", "Solana"]  # list
ath_date = (2021, 11, 10)  # tuple (рік, місяць, день)
coin_ranks = {"Bitcoin": 1, "Ethereum": 2, "Solana": 5}  # dict
unique_exchanges = {"Binance", "Kraken", "Coinbase"}  # set
last_hack_report = None  # NoneType

# --- Список для зручного виводу: (назва, значення, тип) ---
variables = [
    ("coin_name", coin_name),
    ("price_usd", price_usd),
    ("active_wallets", active_wallets),
    ("is_bullish", is_bullish),
    ("top_coins", top_coins),
    ("ath_date", ath_date),
    ("coin_ranks", coin_ranks),
    ("unique_exchanges", unique_exchanges),
    ("last_hack_report", last_hack_report),
]

# --- Вивід у вигляді таблиці ---
name_width = max(len(n) for n, _ in variables)
value_width = max(len(str(v)) for _, v in variables)
type_width = max(len(str(type(v))) for _, v in variables)

header = f"{'Змінна'.ljust(name_width)} │ {'Значення'.ljust(value_width)} │ Тип"
print(header)
print("─" * (name_width + value_width + type_width + 6))

for name, value in variables:
    print(f"{name.ljust(name_width)} │ {str(value).ljust(value_width)} │ {type(value)}")


"""
Змінна           │ Значення                                   │ Тип
──────────────────────────────────────────────────────────────────────────────────
coin_name        │ Bitcoin                                    │ <class 'str'>
price_usd        │ 64250.75                                   │ <class 'float'>
active_wallets   │ 48500000                                   │ <class 'int'>
is_bullish       │ True                                       │ <class 'bool'>
top_coins        │ ['Bitcoin', 'Ethereum', 'Solana']          │ <class 'list'>
ath_date         │ (2021, 11, 10)                             │ <class 'tuple'>
coin_ranks       │ {'Bitcoin': 1, 'Ethereum': 2, 'Solana': 5} │ <class 'dict'>
unique_exchanges │ {'Coinbase', 'Binance', 'Kraken'}          │ <class 'set'>
last_hack_report │ None                                       │ <class 'NoneType'>
"""
# ===============================================================================

# Практика №2
"""
Напиши програму:
patient_name = "Іван"
patient_age = 34
patient_weight = 82.5
patient_has_allergy = True

Виведи:
значення;
тип;
id().
"""

# --- Змінні зі зразка ---
patient_name = "Іван"
patient_age = 34
patient_weight = 82.5
patient_has_allergy = True

# --- Додаткові змінні для повноти ---
patient_diagnoses = ["гайморит", "риніт"]  # list
patient_vitals = {"pulse": 78, "pressure": "120/80"}  # dict

# --- Список для зручного виводу: (назва, значення) ---
variables = [
    ("patient_name", patient_name),
    ("patient_age", patient_age),
    ("patient_weight", patient_weight),
    ("patient_has_allergy", patient_has_allergy),
    ("patient_diagnoses", patient_diagnoses),
    ("patient_vitals", patient_vitals),
]

# --- Вивід у вигляді таблиці ---
name_width = max(len(n) for n, _ in variables)
value_width = max(len(str(v)) for _, v in variables)

header = f"{'Змінна'.ljust(name_width)} │ {'Значення'.ljust(value_width)} │ {'Тип'.ljust(14)} │ id()"
print(header)
print("─" * (len(header) + 5))

for name, value in variables:
    print(
        f"{name.ljust(name_width)} │ {str(value).ljust(value_width)} │ {str(type(value)).ljust(15)} │ {id(value)}"
    )


"""
Змінна              │ Значення                            │ Тип            │ id()
──────────────────────────────────────────────────────────────────────────────────────
patient_name        │ Іван                                │ <class 'str'>   │ 2477071898288
patient_age         │ 34                                  │ <class 'int'>   │ 140706526775448
patient_weight      │ 82.5                                │ <class 'float'> │ 2477072178320
patient_has_allergy │ True                                │ <class 'bool'>  │ 140706525874944
patient_diagnoses   │ ['гайморит', 'риніт']               │ <class 'list'>  │ 2477071762240
patient_vitals      │ {'pulse': 78, 'pressure': '120/80'} │ <class 'dict'>  │ 2477071955200
"""
# ===============================================================================

# Практика №3
"""
Покажи різницю між:
==
is

На прикладі:
list
str
None
"""


def show_comparison(title, a, b):
    "Показує порівняння == та is для двох об'єктів."
    equal = a == b
    same_object = a is b

    print(f"┌─ {title} " + "─" * (40 - len(title)))
    print(f"│  a = {a!r}")
    print(f"│  b = {b!r}")
    print(f"│")
    print(f"│  a == b  →  {equal}    (чи однакові ЗНАЧЕННЯ)")
    print(f"│  a is b  →  {same_object}    (чи це ОДИН і той самий об'єкт у пам'яті)")
    print(f"│  id(a) = {id(a)}")
    print(f"│  id(b) = {id(b)}")
    print("└" + "─" * 42 + "\n")


# --- 1. list: однаковий вміст, РІЗНІ об'єкти ---
portfolio_a = ["BTC", "ETH", "SOL"]
portfolio_b = ["BTC", "ETH", "SOL"]
show_comparison("list", portfolio_a, portfolio_b)

# --- 2. str: короткі рядки Python інтернує (кешує) ---
coin_a = "Bitcoin"
coin_b = "Bitcoin"
show_comparison("str", coin_a, coin_b)

# --- 3. None: завжди ОДИН єдиний об'єкт у всій програмі ---
last_trade_a = None
last_trade_b = None
show_comparison("None", last_trade_a, last_trade_b)

# --- 4. int: малі числа (-5..256) Python кешує ---
rank_a = 5
rank_b = 5
show_comparison("int (мале число)", rank_a, rank_b)

# --- 5. int: великі числа НЕ кешуються ---
price_a = 64250
price_b = 64250
show_comparison("int (велике число)", price_a, price_b)


"""
┌─ list ────────────────────────────────────
│  a = ['BTC', 'ETH', 'SOL']
│  b = ['BTC', 'ETH', 'SOL']
│
│  a == b  →  True    (чи однакові ЗНАЧЕННЯ)
│  a is b  →  False    (чи це ОДИН і той самий об'єкт у пам'яті)
│  id(a) = 1540458971968
│  id(b) = 1540457428288
└──────────────────────────────────────────

┌─ str ─────────────────────────────────────
│  a = 'Bitcoin'
│  b = 'Bitcoin'
│
│  a == b  →  True    (чи однакові ЗНАЧЕННЯ)
│  a is b  →  True    (чи це ОДИН і той самий об'єкт у пам'яті)
│  id(a) = 1540459622592
│  id(b) = 1540459622592
└──────────────────────────────────────────

┌─ None ────────────────────────────────────
│  a = None
│  b = None
│
│  a == b  →  True    (чи однакові ЗНАЧЕННЯ)
│  a is b  →  True    (чи це ОДИН і той самий об'єкт у пам'яті)
│  id(a) = 140706525875008
│  id(b) = 140706525875008
└──────────────────────────────────────────

┌─ int (мале число) ────────────────────────
│  a = 5
│  b = 5
│
│  a == b  →  True    (чи однакові ЗНАЧЕННЯ)
│  a is b  →  True    (чи це ОДИН і той самий об'єкт у пам'яті)
│  id(a) = 140706526774520
│  id(b) = 140706526774520
└──────────────────────────────────────────

┌─ int (велике число) ──────────────────────
│  a = 64250
│  b = 64250
│
│  a == b  →  True    (чи однакові ЗНАЧЕННЯ)
│  a is b  →  True    (чи це ОДИН і той самий об'єкт у пам'яті)
│  id(a) = 1540456624592
│  id(b) = 1540456624592
└──────────────────────────────────────────
"""
# ===============================================================================

# Практика №4
"""
Напиши програму, яка:

отримує:
зріст
вагу
як рядки (input()),
перетворює їх у числа,
обчислює BMI.
"""


def get_number(prompt, is_float=True):
    "Запитує число і перевіряє, чи введено коректне значення."
    while True:
        value = input(prompt)  # input() ЗАВЖДИ повертає рядок (str)
        try:
            number = float(value) if is_float else int(value)
            if number <= 0:
                print("⚠ Значення має бути більшим за нуль.\n")
                continue
            return number
        except ValueError:
            print("⚠ Помилка: введіть, будь ласка, число.\n")


def bmi_category(bmi):
    "Визначає категорію за ІМТ."
    if bmi < 18.5:
        return "недостатня вага"
    elif bmi < 25:
        return "норма"
    elif bmi < 30:
        return "надлишкова вага"
    else:
        return "ожиріння"


# --- Отримання даних як рядків через input(), з перетворенням у числа ---
height_str = input("Введіть зріст (см): ")  # тип str, напр. "178"
weight_str = input("Введіть вагу (кг): ")  # тип str, напр. "80.5"

height = float(height_str)  # перетворення str → float
weight = float(weight_str)  # перетворення str → float

# --- Обчислення BMI ---
height_m = height / 100
bmi = weight / (height_m**2)
category = bmi_category(bmi)

# --- Вивід у рамці ---
lines = [
    f"Зріст:  {height} см",
    f"Вага:   {weight} кг",
    f"ІМТ:    {bmi:.1f}",
    f"Статус: {category}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  РОЗРАХУНОК BMI".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")


"""
Введіть зріст (см): 183
Введіть вагу (кг): 86

┌───────────────────────────┐
│        РОЗРАХУНОК BMI     │
├───────────────────────────┤
│  Зріст:  183.0 см         │
│  Вага:   86.0 кг          │
│  ІМТ:    25.7             │
│  Статус: надлишкова вага  │
└───────────────────────────┘
"""
# ===============================================================================

# Практика №5
"""
Поясни, що буде надруковано.

a = 5
b = a
b = 10

print(a)
print(b)
"""


a = 5
b = a
b = 10

print(a)
print(b)
print(id(a))
print(id(b))

"""
5
10
140706526774520
140706526774680
#------------------------------------------------------------------
a = 5        # створюється об'єкт 5, змінна 'a' вказує на нього
b = a        # 'b' починає вказувати на ТОЙ САМИЙ об'єкт 5, що й 'a'
b = 10       # 'b' тепер вказує на НОВИЙ об'єкт 10, а 'a' продовжує вказувати на 5

print(a)     # 5  — 'a' не змінювалась
print(b)     # 10 — 'b' перепризначили новий об'єкт
print(id(a)) # 140706526774520
print(id(b)) # 140706526774680 — різні id, бо це різні об'єкти

"""
# ===============================================================================
