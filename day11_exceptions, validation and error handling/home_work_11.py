"""
## !Challenge 1 — robust BMI!

Створи:
def calculate_bmi_safe(
    weight: float,
    height: float,
) -> float:
    ...

Правила:
weight <= 0 → ValueError
height <= 0 → ValueError
нечислові типи → TypeError

Повернення:
float
"""

# ═══════════════════════════════════════════
# ВАРІАНТ A — явні isinstance() перевірки
# ═══════════════════════════════════════════
def calculate_bmi_safe_explicit(weight: float, height: float) -> float:
    """Обчислює BMI з явною перевіркою типів ДО обчислення.

    Формула: BMI = weight / height² (height у МЕТРАХ).
    """
    if not isinstance(weight, (int, float)):
        raise TypeError(f"weight має бути числом, отримано {type(weight).__name__}")
    if not isinstance(height, (int, float)):
        raise TypeError(f"height має бути числом, отримано {type(height).__name__}")

    if weight <= 0:
        raise ValueError(f"weight має бути більше 0, отримано {weight}")
    if height <= 0:
        raise ValueError(f"height має бути більше 0, отримано {height}")

    return weight / (height ** 2)


# ═══════════════════════════════════════════
# ВАРІАНТ B — природний TypeError від арифметики
# ═══════════════════════════════════════════
def calculate_bmi_safe_natural(weight: float, height: float) -> float:
    """Те саме, але БЕЗ явних isinstance() — покладаємось на Python."""
    try:
        if weight <= 0:      # ← якщо weight не число, тут ВИНИКНЕ TypeError природно
            raise ValueError(f"weight має бути більше 0, отримано {weight}")
        if height <= 0:
            raise ValueError(f"height має бути більше 0, отримано {height}")

        return weight / (height ** 2)   # ← або тут, якщо перевірки вище пройшли,
                                          #    але типи все ж непридатні для арифметики
    except TypeError as e:
        raise TypeError(f"weight/height мають бути числами: {e}")


# --- Тестові дані ---
test_cases = [
    (82, 1.80),        # ✅ валідні числа
    (-5, 1.80),         # ❌ weight <= 0
    (82, 0),             # ❌ height <= 0
    ("82", 1.80),         # ❌ weight — рядок (не число)
    (82, None),            # ❌ height — None
]


def run_demo(func, cases):
    results = []
    for weight, height in cases:
        try:
            bmi = func(weight, height)
            results.append((weight, height, f"✅ BMI = {bmi:.1f}"))
        except ValueError as e:
            results.append((weight, height, f"❌ ValueError: {e}"))
        except TypeError as e:
            results.append((weight, height, f"❌ TypeError: {e}"))
    return results


results_explicit = run_demo(calculate_bmi_safe_explicit, test_cases)
results_natural = run_demo(calculate_bmi_safe_natural, test_cases)

# --- Вивід у рамці ---
lines = ["ВАРІАНТ A (explicit isinstance):"]
for weight, height, result in results_explicit:
    lines.append(f"  weight={weight!r}, height={height!r}  →  {result}")
lines.append("─" * 65)
lines.append("ВАРІАНТ B (natural TypeError):")
for weight, height, result in results_natural:
    lines.append(f"  weight={weight!r}, height={height!r}  →  {result}")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  CALCULATE_BMI_SAFE()".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
 ┌──────────────────────────────────────────────────────────────────────────────────────┐
│                                                             CALCULATE_BMI_SAFE()      │
├───────────────────────────────────────────────────────────────────────────────────────┤
│  ВАРІАНТ A (explicit isinstance):                                                     │
│    weight=82, height=1.8  →  ✅ BMI = 25.3                                            │
│    weight=-5, height=1.8  →  ❌ ValueError: weight має бути більше 0, отримано -5     │
│    weight=82, height=0  →    ❌ ValueError: height має бути більше 0, отримано 0      │
│    weight='82', height=1.8  →  ❌ TypeError: weight має бути числом, отримано str     │
│    weight=82, height=None  →   ❌ TypeError: height має бути числом, отримано NoneType│
│  ─────────────────────────────────────────────────────────────────                    │
│  ВАРІАНТ B (natural TypeError):                                                       │
│    weight=82, height=1.8  →  ✅ BMI = 25.3                                            │
│    weight=-5, height=1.8  →  ❌ ValueError: weight має бути більше 0, отримано -5     │
│    weight=82, height=0  →    ❌ ValueError: height має бути більше 0, отримано 0      │
│    weight='82', height=1.8  →  ❌ TypeError: weight/height мають бути числами: 
                            '<=' not supported between instances of 'str' and 'int'      │
│    weight=82, height=None  →  ❌ TypeError: weight/height мають бути числами: 
                            '<=' not supported between instances of 'NoneType' and 'int' │
└───────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
*Пояснення Варіанту A — явні isinstance() перевірки:
if not isinstance(weight, (int, float)):
    raise TypeError(...)

isinstance(x, (int, float)) перевіряє: "чи x є саме int або float?" — ще до того, як ми взагалі спробуємо щось із ним зробити. 
Якщо тип неправильний — помилка кидається одразу, з зрозумілим повідомленням ("weight має бути числом, отримано str").

*Пояснення Варіанту B — природний TypeError, "спійманий" і "переупакований":
if weight <= 0:   # якщо weight="82" (рядок) — Python сам кине TypeError ТУТ:
                    # TypeError: '<=' not supported between instances of 'str' and 'int'

Тут ми не перевіряємо тип заздалегідь — просто пробуємо виконати операцію, і якщо Python сам кидає TypeError 
(бо рядок не можна порівняти з числом через <=), ми ловимо цю "сиру" помилку й переоформлюємо її в більш зрозуміле повідомлення.

*Порівняння двох підходів:
	                            Варіант A (явний)	            Варіант B (природний)
Коли виявляється помилка	    до будь-яких обчислень	        під час обчислень 
                                                                (там, де Python першим
                                                                    "спіткнеться")
Читабельність повідомлення	    ✅ повне контроль 	           залежить від того, 
                                над текстом одразу               ЩО саме Python скаже природно
Кількість коду	                більше                           менше 
                                (явні перевірки                  (покладаємось на Python)
                                для кожного параметра)
Ризик "пропустити" перевірку	немає — усе явно	             ⚠️ якщо тип частково сумісний 
                                                                 (наприклад, bool — підклас int!), 
                                                                 Python може НЕ кинути помилку там, де очікуєш

*Важлива пастка, яку варто знати — bool є підкласом int у Python:
isinstance(True, int)   # → True !!! bool ЗАВЖДИ вважається int у Python

calculate_bmi_safe_explicit(True, 1.80)   # weight=True → isinstance(True, (int, float)) → True
                                             # ПРОЙДЕ перевірку типу!
                                             # Але True == 1, тому weight <= 0? 1 <= 0 → False
                                             # Функція ПОРАХУЄ якийсь BMI для weight=1 — 
                                             # це технічно "працює", але семантично дивно

Це нюанс, про який варто пам'ятати в обох варіантах — жоден із простих підходів (isinstance() чи природний TypeError) автоматично не захищає від логічно неправильних, але технічно "валідних" типів, як bool.

*Головний практичний висновок: 
Варіант A краще для публічних API (як MedAssistant), де важлива передбачувана, контрольована поведінка й зрозумілі повідомлення про помилки для будь-якого викликача. 
Варіант B коротший, але повідомлення про помилку залежить від того, що саме Python "скаже" на конкретному кроці обчислення — менш контрольовано, хоч і менш багатослівно.
"""

# ==============================================================================
# ==============================================================================
"""
# !Challenge 2 — safe JSON loader!

Створи:
def load_json_safe(
    path: str,
) -> dict | list | None:
    ...

Оброби:
FileNotFoundError
json.JSONDecodeError
OSError

Але не ховай усі можливі помилки під:
except Exception:
"""

import json
import os


def load_json_safe(path: str) -> dict | list | None:
    """Безпечно завантажує JSON-файл, обробляючи ТРИ конкретні типи помилок.

    Свідомо НЕ використовує `except Exception:` — кожен тип помилки
    обробляється ОКРЕМО, з власним, зрозумілим повідомленням.
    Це означає: якщо станеться помилка ІНШОГО типу (напр. MemoryError,
    KeyboardInterrupt) — вона НЕ буде "проковтнута" мовчки, а спливе
    назовні, як і має бути.

    Args:
        path: Шлях до JSON-файлу.

    Returns:
        dict | list | None: Дані з файлу, або None у разі помилки.
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

    except OSError as e:
        # OSError — ширший клас: PermissionError, IsADirectoryError тощо.
        # ВАЖЛИВО: цей except іде ПІСЛЯ FileNotFoundError, бо
        # FileNotFoundError є ПІДКЛАСОМ OSError — якби OSError стояв
        # ПЕРШИМ, він "перехопив" би FileNotFoundError раніше,
        # і той except ніколи б не спрацював.
        print(f"⚠ Помилка операційної системи при відкритті '{path}': {e}")
        return None


# --- Підготовка тестових сценаріїв ---

# 1. Валідний файл
with open("valid.json", "w", encoding="utf-8") as f:
    json.dump({"name": "Ivan", "age": 42}, f)

# 2. Пошкоджений JSON
with open("broken.json", "w", encoding="utf-8") as f:
    f.write('{"name": "Ivan", "age": }')

# 3. Папка замість файлу (IsADirectoryError — підклас OSError)
os.makedirs("a_directory", exist_ok=True)


# --- Демонстрація ВСІХ сценаріїв ---
test_cases = [
    ("valid.json", "валідний файл"),
    ("nonexistent.json", "файл не існує (FileNotFoundError)"),
    ("broken.json", "пошкоджений JSON (JSONDecodeError)"),
    ("a_directory", "це папка, не файл (OSError/IsADirectoryError)"),
]

results = []
for path, description in test_cases:
    result = load_json_safe(path)
    results.append((path, description, result))

# --- Вивід у рамці ---
lines = [f"{path!r} ({desc})  →  {result}" for path, desc, result in results]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  LOAD_JSON_SAFE()".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
⚠ Помилка: файл 'nonexistent.json' не знайдено.
⚠ Помилка: файл 'broken.json' містить некоректний JSON (Expecting value: line 1 column 25 (char 24)).
⚠ Помилка операційної системи при відкритті 'a_directory': [Errno 13] Permission denied: 'a_directory'

┌──────────────────────────────────────────────────────────────────────────┐
│                              LOAD_JSON_SAFE()                            │
├──────────────────────────────────────────────────────────────────────────┤
│  'valid.json' (валідний файл)  →  {'name': 'Ivan', 'age': 42}            │
│  'nonexistent.json' (файл не існує (FileNotFoundError))  →  None         │
│  'broken.json' (пошкоджений JSON (JSONDecodeError))  →  None             │
│  'a_directory' (це папка, не файл (OSError/IsADirectoryError))  →  None  │
└──────────────────────────────────────────────────────────────────────────┘
"""

"""
#*Чому НЕ можна ловити все через except Exception: — головна причина заборони в умові:
# ❌ ТАК НЕ ТРЕБА:
def load_json_bad(path):
    try:
        with open(path) as file:
            return json.load(file)
    except Exception as e:      # ← "ловить" АБСОЛЮТНО ВСЕ
        print(f"Помилка: {e}")
        return None

# Проблема: ЦЯ функція "проковтне" НАВІТЬ:
# - KeyboardInterrupt (Ctrl+C) — користувач НЕ зможе перервати програму!
# - MemoryError — програма ТИХО поверне None замість реальної проблеми з пам'яттю
# - SyntaxError у власному коді (якщо десь помилка в іншому місці) —
#   буде помилково "приписана" до проблеми з JSON, хоча причина зовсім інша

except Exception: — це як "спіймати БУДЬ-ЩО, що піде не так, і мовчки все виправити" — це приховує справжні проблеми замість того, щоб їх вирішувати, і робить налагодження набагато складнішим, бо незрозуміло, яка саме з десятків можливих причин викликала проблему.

#*Чому порядок except-блоків важливий — ключовий технічний нюанс:
try:
    with open(path) as file:
        return json.load(file)
except FileNotFoundError:   # ← має йти ПЕРШИМ
    ...
except OSError:               # ← має йти ПІСЛЯ, бо є "ширшим"
    ...

FileNotFoundError успадковується від OSError 
(це можна перевірити: issubclass(FileNotFoundError, OSError) → True). 

#*Python перевіряє except-блоки зверху вниз і зупиняється на першому, що підходить:
# ❌ НЕПРАВИЛЬНИЙ порядок — OSError "перехопить" ВСЕ раніше:
except OSError:          # ← спрацює НАВІТЬ для FileNotFoundError!
    ...
except FileNotFoundError:   # ← цей блок СТАНЕ НЕДОСЯЖНИМ (dead code)
    ...

# ✅ ПРАВИЛЬНИЙ порядок — від конкретного до загального:
except FileNotFoundError:   # ← спрацьовує для НАЙВУЖЧОГО, найточнішого випадку
    ...
except OSError:               # ← "запасний варіант" для всього ІНШОГО з класу OSError
    ...

#*Ієрархія винятків, яка тут задіяна:
Exception
  └── OSError
        ├── FileNotFoundError     (файл не знайдено)
        ├── PermissionError        (немає прав доступу)
        ├── IsADirectoryError       (очікувався файл, а це папка)
        └── ... (інші файлові помилки)

#*Пояснення json.JSONDecodeError — де саме він у ієрархії:
issubclass(json.JSONDecodeError, ValueError)   # → True!

#*Цікавий нюанс: 
JSONDecodeError насправді є підкласом ValueError, а не OSError — тому їхні except-блоки не конфліктують між собою і порядок цих двох (FileNotFoundError/OSError проти JSONDecodeError) не має значення, лише порядок всередині родини OSError критичний.
"""

# ==============================================================================
# ==============================================================================
"""
# !Challenge 3 — patient validator!

Створи:
def validate_patient(patient: dict) -> None:
    ...

Перевір:
id
name
age
temperature

Наприклад:
{
    "id": 1,
    "name": "Ivan",
    "age": 42,
    "temperature": 36.8,
}

Коректний patient → нічого не повертає.
Некоректний → raise ValueError(...).
"""

def validate_patient(patient: dict) -> None:
    """Перевіряє всі поля пацієнта, збираючи ВСІ помилки одразу.

    На відміну від fail-fast підходу (Task 4), ця функція НЕ зупиняється
    на першій-ліпшій помилці — вона перевіряє КОЖНЕ поле, накопичує
    всі знайдені проблеми в список, і лише НАПРИКІНЦІ піднімає ОДНЕ
    ValueError з повним переліком усього, що не так.

    Raises:
        ValueError: Якщо хоча б одне поле некоректне. Повідомлення
            містить ВСІ знайдені проблеми, а не лише першу.
    """
    errors = []   # ← накопичувач помилок

    # --- Перевірка "id": має бути ДОДАТНЄ ЦІЛЕ ---
    if "id" not in patient:
        errors.append("відсутнє поле 'id'")
    elif not isinstance(patient["id"], int) or isinstance(patient["id"], bool):
        errors.append(f"'id' має бути цілим числом, отримано {patient['id']!r}")
    elif patient["id"] <= 0:
        errors.append(f"'id' має бути додатним, отримано {patient['id']}")

    # --- Перевірка "name": має бути НЕПОРОЖНІЙ рядок ---
    if "name" not in patient:
        errors.append("відсутнє поле 'name'")
    elif not isinstance(patient["name"], str):
        errors.append(f"'name' має бути рядком, отримано {patient['name']!r}")
    elif not patient["name"].strip():
        errors.append("'name' не може бути порожнім")

    # --- Перевірка "age": має бути ЦІЛЕ ЧИСЛО > 0 ---
    if "age" not in patient:
        errors.append("відсутнє поле 'age'")
    elif not isinstance(patient["age"], int) or isinstance(patient["age"], bool):
        errors.append(f"'age' має бути цілим числом, отримано {patient['age']!r}")
    elif patient["age"] <= 0:
        errors.append(f"'age' має бути більшим за 0, отримано {patient['age']}")

    # --- Перевірка "temperature": число в діапазоні 25.0–45.0 ---
    if "temperature" not in patient:
        errors.append("відсутнє поле 'temperature'")
    elif not isinstance(patient["temperature"], (int, float)) or isinstance(patient["temperature"], bool):
        errors.append(f"'temperature' має бути числом, отримано {patient['temperature']!r}")
    elif not (25.0 <= patient["temperature"] <= 45.0):
        errors.append(f"'temperature' має бути в діапазоні 25.0–45.0, отримано {patient['temperature']}")

    # --- Якщо ХОЧА Б ОДНА помилка була знайдена — піднімаємо ОДНУ ValueError з УСІМА ---
    if errors:
        raise ValueError("Некоректні дані пацієнта: " + "; ".join(errors))


# --- Тестові дані ---
test_patients = [
    {"id": 1, "name": "Ivan", "age": 42, "temperature": 36.8},           # ✅ коректний
    {"id": 1, "name": "Ivan", "age": 42},                                  # ❌ немає temperature
    {"id": -1, "name": "", "age": -5, "temperature": 99.0},                 # ❌ ЧОТИРИ помилки одразу
    {"id": "1", "name": "Olena", "age": 35, "temperature": 36.6},            # ❌ id — рядок
]

results = []
for patient in test_patients:
    try:
        validate_patient(patient)
        results.append((patient, "✅ Валідний пацієнт"))
    except ValueError as e:
        results.append((patient, f"❌ {e}"))

# --- Вивід у рамці ---
lines = [f"{patient}\n    → {result}" for patient, result in results]

width = max(len(line) for line in "\n".join(lines).split("\n")) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  VALIDATE_PATIENT()".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    for sub_line in line.split("\n"):
        print("│  " + sub_line.ljust(width - 2) + "│")
    print("├" + "─" * width + "┤")
print("└" + "─" * width + "┘")

"""
┌────────────────────────────────────────────────────────────────────
│                                           VALIDATE_PATIENT()      │
├──────────────────────────────────────────────────────────────────────
│  {'id': 1, 'name': 'Ivan', 'age': 42, 'temperature': 36.}         │
│      → ✅ Валідний пацієнт                                       │
├──────────────────────────────────────────────────────────────────┤
│  {'id': 1, 'name': 'Ivan', 'age': 42}                               │
│      → ❌ Некоректні дані пацієнта: відсутнє поле 'temperature'    │
├─────────────────────────────────────────────────────────────────────┤
│  {'id': -1, 'name': '', 'age': -5, 'temperature': 99.0}             │
│      → ❌ Некоректні дані пацієнта: 'id' має бути додатним, отримано -1; 'name' не може бути порожнім; 
            'age' має бути більшим за 0, отримано -5; 'temperature' має бути в діапазоні 25.0–45.0, отримано 99.0  │
├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│  {'id': '1', 'name': 'Olena', 'age': 35, 'temperature': 36.6}                 │
│      → ❌ Некоректні дані пацієнта: 'id' має бути цілим числом, отримано '1'  │
├───────────────────────────────────────────────────────────────────────────────┤
└───────────────────────────────────────────────────────────────────────────────┘
"""

"""
#*Пояснення накопичувального підходу (collect-all) — ключова ідея завдання:
errors = []                      # ① починаємо з ПОРОЖНЬОГО списку

if "id" not in patient:
    errors.append("...")          # ② якщо ПРОБЛЕМА — ДОДАЄМО в список,
                                    #    але НЕ зупиняємось тут!

if "name" not in patient:          # ③ ПРОДОВЖУЄМО перевіряти НАСТУПНЕ поле,
    errors.append("...")            #    незалежно від того, що було з "id"

# ... і так для КОЖНОГО поля ...

if errors:                          # ④ ТІЛЬКИ НАПРИКІНЦІ — якщо щось назбиралось —
    raise ValueError(...)            #    піднімаємо ОДНЕ повідомлення з УСІМ одразу

#*Порівняння з fail-fast підходом (Task 4 попереднього завдання):
# ❌ Fail-fast (як у get_patient_age) — зупиняється на ПЕРШІЙ помилці:
def validate_fail_fast(patient):
    if "id" not in patient:
        raise ValueError("немає id")   # ← ЗУПИНКА тут, "name"/"age"/"temperature"
                                          #   навіть НЕ перевіряються!
    if "name" not in patient:
        raise ValueError("немає name")
    ...

# Результат для {"id": -1, "name": "", "age": -5, "temperature": 99.0}:
# → ValueError("id має бути додатним")   ← бачиш ЛИШЕ ОДНУ з ЧОТИРЬОХ проблем!

# ✅ Collect-all (це завдання) — перевіряє ВСЕ, показує ВСЕ одразу:
def validate_patient(patient):
    errors = []
    # перевіряємо КОЖНЕ поле, накопичуємо ВСІ проблеми
    if errors:
        raise ValueError(...)

# Результат для {"id": -1, "name": "", "age": -5, "temperature": 99.0}:
# → ValueError("'id' має бути додатним, отримано -1; 'name' не може бути порожнім;
#                'age' має бути більшим за 0, отримано -5;
#                'temperature' має бути в діапазоні 25.0–45.0, отримано 99.0")
#   ← ВСІ чотири проблеми видно ОДРАЗУ, за ОДИН запуск!

#*Чому collect-all — краще саме для валідації ФОРМ/ЗАПИСІВ (на відміну від parse_age):

Уяви, що людина заповнює форму реєстрації пацієнта і одночасно припустилась кількох помилок (порожнє ім'я, від'ємний вік, неправильна температура). З fail-fast підходом користувач побачив би лише першу помилку, виправив би її, натиснув "зберегти" знову — і одразу побачив би наступну помилку, і так кілька разів поспіль. З collect-all підходом він одразу бачить весь список того, що треба виправити — набагато зручніше на практиці.

#*Захист від bool (пастка з Challenge 1):
isinstance(patient["id"], int) or isinstance(patient["id"], bool)
#                                   ↑
# ЯВНО виключаємо bool, бо isinstance(True, int) → True (небажаний побічний ефект)

Це той самий нюанс, що обговорювався в Challenge 1 цього дня — без цього додаткового виключення id: True пройшов би перевірку isinstance(id, int), хоча логічно True/False — це не той тип значення, який очікується для id пацієнта.
"""

# ==============================================================================
# ==============================================================================
"""
## !Challenge 4 — controlled errors!

Зроби:
def find_patient(
    patients: list[dict],
    name: str,
) -> dict:
    ...

На відміну від Дня 10, ця версія повинна:
пацієнта знайдено → return patient
не знайдено → raise ValueError

Потім окремо оброби помилку в main().

Це дозволить тобі побачити два різні API-підходи:
dict | None
та:
dict + exception
"""

# ═══════════════════════════════════════════
# ВЕРСІЯ A (День 10) — dict | None
# ═══════════════════════════════════════════
def find_patient_optional(patients: list[dict], name: str) -> dict | None:
    """Знаходить пацієнта за іменем. Повертає None, якщо не знайдено."""
    for patient in patients:
        if patient["name"].lower() == name.lower():
            return patient
    return None


# ═══════════════════════════════════════════
# ВЕРСІЯ B (цей Challenge) — dict + exception
# ═══════════════════════════════════════════
def find_patient(patients: list[dict], name: str) -> dict:
    """Знаходить пацієнта за іменем. Піднімає ValueError, якщо не знайдено.

    Raises:
        ValueError: Якщо жоден пацієнт не відповідає імені `name`.
    """
    for patient in patients:
        if patient["name"].lower() == name.lower():
            return patient
    raise ValueError(f"Пацієнта з ім'ям '{name}' не знайдено")


# --- Дані ---
patients = [
    {"name": "Ivan", "age": 42},
    {"name": "Olena", "age": 35},
    {"name": "Petro", "age": 61},
]


# ═══════════════════════════════════════════
# main() — обробка ОБОХ версій
# ═══════════════════════════════════════════
def main():
    results = []

    # --- Версія A (dict | None) — перевірка через if ---
    for name in ["Ivan", "Dmytro"]:
        patient = find_patient_optional(patients, name)
        if patient is not None:
            results.append(("A (Optional)", name, f"✅ {patient}"))
        else:
            results.append(("A (Optional)", name, "❌ None (не знайдено)"))

    # --- Версія B (exception) — перевірка через try/except ---
    for name in ["Ivan", "Dmytro"]:
        try:
            patient = find_patient(patients, name)
            results.append(("B (Exception)", name, f"✅ {patient}"))
        except ValueError as e:
            results.append(("B (Exception)", name, f"❌ ValueError: {e}"))

    return results


results = main()

# --- Вивід у рамці ---
lines = [f"{version:<15} find('{name}')  →  {result}" for version, name, result in results]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  DICT | NONE  vs  DICT + EXCEPTION".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                             DICT | NONE  vs  DICT + EXCEPTION                            │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│  A (Optional)    find('Ivan')  →  ✅ {'name': 'Ivan', 'age': 42}                          │
│  A (Optional)    find('Dmytro')  →  ❌ None (не знайдено)                                 │
│  B (Exception)   find('Ivan')  →  ✅ {'name': 'Ivan', 'age': 42}                          │
│  B (Exception)   find('Dmytro')  →  ❌ ValueError: Пацієнта з ім'ям 'Dmytro' не знайдено  │
└──────────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
#*Пояснення різниці — два способи сказати "результат може бути відсутнім":
# Версія A: РЕЗУЛЬТАТ типу — сам факт "не знайдено" ЗАКОДОВАНИЙ у поверненому ЗНАЧЕННІ
def find_patient_optional(patients, name) -> dict | None:
    ...
    return None            # ← "не знайдено" виглядає ЯК ЗВИЧАЙНЕ значення

patient = find_patient_optional(patients, "Dmytro")
if patient is not None:      # ← ВИКЛИКАЧ МУСИТЬ пам'ятати перевірити на None
    ...

# Версія B: РЕЗУЛЬТАТ типу — гарантовано ЗАВЖДИ dict, а "не знайдено" — ОКРЕМИЙ канал
def find_patient(patients, name) -> dict:
    ...
    raise ValueError(...)     # ← "не знайдено" — це ЗОВСІМ ІНШИЙ шлях виконання

patient = find_patient(patients, "Dmytro")   # 💥 якщо не обгорнути в try — програма ВПАДЕ

#*Ключова філософська різниця:
	                    Версія A (dict | None)	        Версія B (dict + ValueError)
Сигнатура	            чесно каже 	                    каже "завжди dict" — 
                        "може НЕ бути результату"       а помилка йде ОКРЕМИМ шляхом

Що станеться, 	        💥 TypeError пізніше, 	        💥 ValueError одразу, 
якщо ЗАБУТИ перевірку   коли спробуєш                   у місці ВИКЛИКУ — ще ДО того, 
                        patient["age"] на None          як None встиг би "поширитись" далі

Змушує обробити 	    ⚠️ НІ — Python НЕ змусить 	    ✅ ТАК — необроблений виняток 
помилку?                тебе перевірити на None         ЗУПИНИТЬ програму одразу

Коли природно	        "відсутність" — це нормальний, 	"відсутність" — це виняткова ситуація, 
                        очікуваний результат            що потребує явної реакції
                        (напр. пошук у списку)

#*Найважливіший практичний ризик Версії A — "тиха" пропущена перевірка:
# Версія A — код МОЖЕ "забути" перевірку і зламатись НЕ одразу, а ПІЗНІШЕ:
patient = find_patient_optional(patients, "Dmytro")
print(patient["age"])   # 💥 TypeError: 'NoneType' object is not subscriptable
                          #    Помилка ТУТ, а НЕ в місці, де насправді "загубився" пацієнт —
                          #    ускладнює діагностику "звідки взявся None"

# Версія B — Python СИЛОЮ зупиняє тебе РІВНО там, де сталась проблема:
patient = find_patient(patients, "Dmytro")   # 💥 ValueError ОДРАЗУ ТУТ
print(patient["age"])                          # цей рядок НІКОЛИ не виконається без обробки

#*Коли обирати кожен підхід:
-1.# dict | None — коли "не знайдено" ЦІЛКОМ НОРМАЛЬНА, ОЧІКУВАНА ситуація,
# і викликач, ймовірно, ХОЧЕ обробити її як звичайну гілку логіки:
patient = find_patient_optional(patients, search_input)
if patient is None:
    print("Такого пацієнта немає в базі — можливо, помилка вводу")
else:
    display(patient)

-2.# dict + exception — коли "не знайдено" Є СПРАВЖНЬОЮ ПРОБЛЕМОЮ,
# і продовжувати виконання БЕЗ обробки цієї ситуації — небезпечно/безглуздо:
try:
    patient = find_patient(patients, patient_id_from_database)
    # ЯКЩО пацієнт мав існувати (бо ID взято з надійного джерела),
    # а його НЕМАЄ — це сигнал про ЦІЛІСНІСТЬ ДАНИХ, а не звичайний "негативний" результат
except ValueError:
    log_critical_error("Розбіжність даних: пацієнт із БД відсутній у поточному списку")
"""

# ==============================================================================
# ==============================================================================
"""
🔥 Challenge 5 — MedAssistant Error Handling

Створи pipeline:
JSON
 ↓
load
 ↓
validate
 ↓
process
 ↓
report

При цьому:
missing file
      ↓
FileNotFoundError

invalid JSON
      ↓
JSONDecodeError

invalid patient
      ↓
ValueError

Програма не повинна падати неконтрольовано.

Приклад поведінки:

MEDASSISTANT
============
Loading patients...
✓ JSON loaded

Validating patients...
✓ Validation passed

Calculating statistics...
✓ Statistics calculated

Generating report...
✓ Report generated

або:

MEDASSISTANT
============
Loading patients...
✗ File not found:
  data/patients.json
"""

#data/medassistant_patients.json (valid sample data):
"""
[
  {
    "id": 1,
    "name": "Ivan",
    "age": 42,
    "temperature": 37.2
  },
  {
    "id": 2,
    "name": "Olena",
    "age": 35,
    "temperature": 36.7
  },
  {
    "id": 3,
    "name": "Petro",
    "age": 61,
    "temperature": 38.5
  }
]

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
"""

#patient_utils.py — завантаження, валідація для одного пацієнта та для декількох пацієнтів:
"""patient_utils.py

Loading and validating patient records for MedAssistant.

Deliberately does NOT swallow exceptions here — FileNotFoundError,
json.JSONDecodeError, and ValueError are all allowed to propagate to
the caller, so main() can catch each one at the right pipeline stage
and report a controlled, specific message instead of a crash.
"""

import json


def load_patients(path: str) -> list[dict]:
    """Load patient records from a JSON file.

    Deliberately does not catch anything — FileNotFoundError and
    json.JSONDecodeError propagate to the caller, which decides how
    to report each one.

    Args:
        path: Path to the JSON file.

    Returns:
        list[dict]: The patient records.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_patient(patient: dict) -> None:
    """Validate a single patient record, collecting ALL field errors.

    Checks every field regardless of earlier failures, then raises
    once with the full list of problems (not just the first one).

    Args:
        patient: A single patient record.

    Raises:
        ValueError: If any field is missing or invalid. The message
            lists every problem found for this patient.
    """
    errors = []

    if "id" not in patient:
        errors.append("missing 'id'")
    elif not isinstance(patient["id"], int) or isinstance(patient["id"], bool):
        errors.append(f"'id' must be an integer, got {patient['id']!r}")
    elif patient["id"] <= 0:
        errors.append(f"'id' must be positive, got {patient['id']}")

    if "name" not in patient:
        errors.append("missing 'name'")
    elif not isinstance(patient["name"], str):
        errors.append(f"'name' must be a string, got {patient['name']!r}")
    elif not patient["name"].strip():
        errors.append("'name' cannot be empty")

    if "age" not in patient:
        errors.append("missing 'age'")
    elif not isinstance(patient["age"], int) or isinstance(patient["age"], bool):
        errors.append(f"'age' must be an integer, got {patient['age']!r}")
    elif patient["age"] <= 0:
        errors.append(f"'age' must be greater than 0, got {patient['age']}")

    if "temperature" not in patient:
        errors.append("missing 'temperature'")
    elif not isinstance(patient["temperature"], (int, float)) or isinstance(patient["temperature"], bool):
        errors.append(f"'temperature' must be a number, got {patient['temperature']!r}")
    elif not (25.0 <= patient["temperature"] <= 45.0):
        errors.append(f"'temperature' must be in range 25.0-45.0, got {patient['temperature']}")

    if errors:
        raise ValueError("; ".join(errors))


def validate_patients(patients: list[dict]) -> tuple[list[dict], list[dict]]:
    """Split patients into valid and invalid, WITHOUT stopping the pipeline.

    Unlike a previous version that raised ValueError and halted
    everything, this now checks every patient and RETURNS both
    groups — the caller decides what to do (typically: proceed with
    the valid ones, report the invalid ones as skipped).

    Args:
        patients: A list of patient records.

    Returns:
        tuple[list[dict], list[dict]]: (valid_patients, invalid_entries).
            Each invalid_entries item is:
            {"index": int, "label": str, "reason": str}
    """
    valid_patients = []
    invalid_entries = []

    for index, patient in enumerate(patients):
        try:
            validate_patient(patient)
            valid_patients.append(patient)
        except ValueError as e:
            label = patient.get("name", f"unnamed (index {index})")
            invalid_entries.append({"index": index, "label": label, "reason": str(e)})

    return valid_patients, invalid_entries

#statistics_utils.py — без змін, суто обчислювальний код:
"""statistics_utils.py

Aggregate statistics over a list of patient records, for MedAssistant.
"""


def average_age(patients: list[dict]) -> float:
    """Compute the average age across all patients."""
    return sum(p["age"] for p in patients) / len(patients)


def average_temperature(patients: list[dict]) -> float:
    """Compute the average temperature across all patients."""
    return sum(p["temperature"] for p in patients) / len(patients)


def oldest_patient(patients: list[dict]) -> dict:
    """Find the oldest patient in the list."""
    return max(patients, key=lambda p: p["age"])

#report_utils.py — створення та збереження:
"""report_utils.py

Report generation and saving for MedAssistant.
"""


def generate_report(
    total_valid: int,
    avg_age: float,
    avg_temp: float,
    oldest: dict,
    invalid_entries: list[dict],
) -> str:
    """Build a human-readable text report, including skipped patients.

    Args:
        total_valid: Number of patients that passed validation.
        avg_age: Average age among valid patients.
        avg_temp: Average temperature among valid patients.
        oldest: The oldest valid patient.
        invalid_entries: Output of validate_patients()'s second value —
            patients that were skipped, with reasons.

    Returns:
        str: The full report text.
    """
    title = "MEDASSISTANT PATIENT REPORT"

    report = (
        f"{title}\n"
        f"{'=' * len(title)}\n\n"
        f"Total valid patients: {total_valid}\n"
        f"Average age: {avg_age:.1f}\n"
        f"Average temperature: {avg_temp:.1f}\n"
        f"Oldest patient: {oldest['name']} ({oldest['age']})\n"
    )

    if invalid_entries:
        report += f"\nSkipped invalid patients: {len(invalid_entries)}\n"
        for entry in invalid_entries:
            report += f"  - {entry['label']} (index {entry['index']}): {entry['reason']}\n"

    return report


def save_report(path: str, report: str) -> None:
    """Save a text report to disk."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(report)

#main.py — керована, поетапна обробка помилок:
"""main.py

MedAssistant Error Handling pipeline:
    load -> validate (skip invalid) -> process (statistics) -> report

Invalid patients no longer halt the whole pipeline: they are
reported as warnings, and the report is generated from the valid
patients only.
"""

import json

from patient_utils import load_patients, validate_patients
from report_utils import generate_report, save_report
from statistics_utils import average_age, average_temperature, oldest_patient


def run_pipeline(data_path: str, report_path: str) -> None:
    print("MEDASSISTANT")
    print("============\n")

    # ── STAGE 1: LOAD ──────────────────────────
    print("Loading patients...")
    try:
        patients = load_patients(data_path)
    except FileNotFoundError:
        print(f"✗ File not found:\n  {data_path}")
        return
    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON:\n  {e}")
        return
    print("✓ JSON loaded\n")

    # ── STAGE 2: VALIDATE (skip invalid, don't stop) ──
    print("Validating patients...")
    valid_patients, invalid_entries = validate_patients(patients)

    if invalid_entries:
        print(f"⚠ {len(invalid_entries)} invalid patient(s) skipped:")
        for entry in invalid_entries:
            print(f"  Patient #{entry['index']} ({entry['label']}): {entry['reason']}")

    if not valid_patients:
        print("✗ No valid patients remain — cannot continue.")
        return

    print(f"✓ Validation passed for {len(valid_patients)} patient(s)\n")

    # ── STAGE 3: PROCESS (statistics) — valid patients only ──
    print("Calculating statistics...")
    avg_age = average_age(valid_patients)
    avg_temp = average_temperature(valid_patients)
    oldest = oldest_patient(valid_patients)
    print("✓ Statistics calculated\n")

    # ── STAGE 4: REPORT ─────────────────────────
    print("Generating report...")
    report = generate_report(
        len(valid_patients), avg_age, avg_temp, oldest, invalid_entries
    )
    save_report(report_path, report)
    print("✓ Report generated")


if __name__ == "__main__":
    run_pipeline("data/patients.json", "data/report.txt")

"""
MEDASSISTANT
============

Loading patients...
✓ JSON loaded

Validating patients...
⚠ 3 invalid patient(s) skipped:
  Patient #0 (Ivan): 'temperature' must be in range 25.0-45.0, got 13.2
  Patient #3 (55): 'id' must be positive, got -4; 'name' must be a string, got 55; 'age' must be an integer, got '61'
  Patient #4 (Petro): 'temperature' must be in range 25.0-45.0, got 58.5
✓ Validation passed for 2 patient(s)

Calculating statistics...
✓ Statistics calculated

Generating report...
✓ Report generated
"""

"""
#report.txt
MEDASSISTANT PATIENT REPORT
===========================

Total valid patients: 2
Average age: 48.0
Average temperature: 37.6
Oldest patient: Petro (61)

Skipped invalid patients: 3
  - Ivan (index 0): 'temperature' must be in range 25.0-45.0, got 13.2
  - 55 (index 3): 'id' must be positive, got -4; 'name' must be a string, got 55; 'age' must be an integer, got '61'
  - Petro (index 4): 'temperature' must be in range 25.0-45.0, got 58.5

"""



"""
дивись нижче
"""

"""
#*Чому кожне виключення обробляється саме на одному конкретному етапі — і ніколи за допомогою універсального блоку catch:
try:
    patients = load_patients(data_path)   # can raise FileNotFoundError OR json.JSONDecodeError
except FileNotFoundError:
    ...
except json.JSONDecodeError as e:
    ...

# — separately, in a DIFFERENT try block —

try:
    validate_patients(patients)            # can raise ValueError
except ValueError as e:
    ...

Це той самий підхід, що й у функції `load_json_safe()` з Завдання 2 — кожен тип винятку має власний виділений блок `except` на тій стадії, де він може фактично виникнути. Немає загального блоку `except Exception: anywhere`, тому справді несподівана помилка (баг в іншому місці коду) все одно відобразиться як реальний трасбек, а не буде непомітно поглинена загальним повідомленням «щось пішло не так».

#*Чому функція `validate_patients()` збирає помилки з усього списку, перш ніж генерувати одне виключення:
for index, patient in enumerate(patients):
    try:
        validate_patient(patient)      # checks ALL 4 fields for THIS patient
    except ValueError as e:
        problems.append(f"Patient #{index} ({label}): {e}")
                                          # ← doesn't stop — keeps checking the REST
if problems:
    raise ValueError("\n".join(problems))   # ONE raise, with EVERY patient's issues

Це та сама філософія «зібрати все», що й у Завданні 3, застосована на рівень вище: validate_patient() збирає всі помилки полів для одного пацієнта; validate_patients() збирає всі помилки пацієнтів для всього списку. Один прохід конвеєра одразу виявляє всі проблеми у всьому наборі даних — а не лише першу, яку вдалося знайти.
"""

# ==============================================================================
# ==============================================================================
"""
# !🧠 Challenge 6 — централізований error handling!

Це вже складніше.

Зроби:
def main() -> None:
    try:
        ...
    except FileNotFoundError:
        ...
    except json.JSONDecodeError:
        ...
    except ValueError:
        ...

При цьому допоміжні функції повинні піднімати exceptions, а не друкувати повідомлення.

Тобто:
patient_utils.py
      ↓
raise ValueError
      ↓
main.py
      ↓
handle error

Це дуже важливий engineering pattern.
"""

"""
Ось окрема навчальна версія main_centralized.py, що демонструє централізований patern обробки помилок — зберігаючи skip-invalid поведінку, але з ValueError, що піднімається лише коли жоден пацієнт не пройшов валідацію.

patient_utils.py (доповнено — допоміжні функції лише піднімають, ніколи не друкують):
"""

#patient_utils.py
"""patient_utils.py

Loading and validating patient records for MedAssistant.

IMPORTANT (centralized error handling pattern): every function here
ONLY raises exceptions when something goes wrong — none of them ever
call print(). Deciding HOW to report a problem to the user belongs
entirely to the caller (main), not to these helpers.
"""

import json


def load_patients(path: str) -> list[dict]:
    """Load patient records from a JSON file.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_patient(patient: dict) -> None:
    """Validate a single patient record, collecting ALL field errors.

    Raises:
        ValueError: If any field is missing or invalid.
    """
    errors = []

    if "id" not in patient:
        errors.append("missing 'id'")
    elif not isinstance(patient["id"], int) or isinstance(patient["id"], bool):
        errors.append(f"'id' must be an integer, got {patient['id']!r}")
    elif patient["id"] <= 0:
        errors.append(f"'id' must be positive, got {patient['id']}")

    if "name" not in patient:
        errors.append("missing 'name'")
    elif not isinstance(patient["name"], str):
        errors.append(f"'name' must be a string, got {patient['name']!r}")
    elif not patient["name"].strip():
        errors.append("'name' cannot be empty")

    if "age" not in patient:
        errors.append("missing 'age'")
    elif not isinstance(patient["age"], int) or isinstance(patient["age"], bool):
        errors.append(f"'age' must be an integer, got {patient['age']!r}")
    elif patient["age"] <= 0:
        errors.append(f"'age' must be greater than 0, got {patient['age']}")

    if "temperature" not in patient:
        errors.append("missing 'temperature'")
    elif not isinstance(patient["temperature"], (int, float)) or isinstance(patient["temperature"], bool):
        errors.append(f"'temperature' must be a number, got {patient['temperature']!r}")
    elif not (25.0 <= patient["temperature"] <= 45.0):
        errors.append(f"'temperature' must be in range 25.0-45.0, got {patient['temperature']}")

    if errors:
        raise ValueError("; ".join(errors))


def validate_patients(patients: list[dict]) -> tuple[list[dict], list[dict]]:
    """Split patients into valid and invalid — does NOT stop on its own.

    Raises:
        ValueError: ONLY if every single patient is invalid (nobody
            left to process). If at least one patient is valid, this
            function returns normally — it does not raise for
            partial failures.

    Returns:
        tuple[list[dict], list[dict]]: (valid_patients, invalid_entries).
    """
    valid_patients = []
    invalid_entries = []

    for index, patient in enumerate(patients):
        try:
            validate_patient(patient)
            valid_patients.append(patient)
        except ValueError as e:
            label = patient.get("name", f"unnamed (index {index})")
            invalid_entries.append({"index": index, "label": label, "reason": str(e)})

    if not valid_patients:
        raise ValueError(
            f"All {len(patients)} patient(s) are invalid — nothing to process. "
            f"Details: {invalid_entries}"
        )

    return valid_patients, invalid_entries

"""
main_centralized.py — новий файл, один try/except, що охоплює весь pipeline:
"""

#main_centralized.py
"""main_centralized.py

Educational variant of MedAssistant's pipeline, demonstrating a
CENTRALIZED error-handling pattern:

    patient_utils.py
          |
      raise ValueError / FileNotFoundError / JSONDecodeError
          |
    main_centralized.py
          |
      ONE try/except block catches everything, at ONE place

Contrast this with the earlier main.py, where each stage had its
OWN try/except — here, ALL stages run inside a SINGLE try, and every
exception type is handled in ONE place, at the end.
"""

import json

from patient_utils import load_patients, validate_patients
from statistics_utils import average_age, average_temperature, oldest_patient
from report_utils import generate_report, save_report


def main() -> None:
    print("MEDASSISTANT (centralized error handling)")
    print("==========================================\n")

    try:
        # --- every stage lives here, with NO local try/except ---
        print("Loading patients...")
        patients = load_patients("data/patients.json")
        print("✓ JSON loaded\n")

        print("Validating patients...")
        valid_patients, invalid_entries = validate_patients(patients)
        if invalid_entries:
            print(f"⚠ {len(invalid_entries)} invalid patient(s) skipped:")
            for entry in invalid_entries:
                print(f"  Patient #{entry['index']} ({entry['label']}): {entry['reason']}")
        print(f"✓ Validation passed for {len(valid_patients)} patient(s)\n")

        print("Calculating statistics...")
        avg_age = average_age(valid_patients)
        avg_temp = average_temperature(valid_patients)
        oldest = oldest_patient(valid_patients)
        print("✓ Statistics calculated\n")

        print("Generating report...")
        report = generate_report(len(valid_patients), avg_age, avg_temp, oldest, invalid_entries)
        save_report("data/report.txt", report)
        print("✓ Report generated")

    # --- ONE place, at the end, handles EVERY exception type ---
    except FileNotFoundError as e:
        print(f"✗ File not found:\n  {e}")
    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON:\n  {e}")
    except ValueError as e:
        print(f"✗ Validation failed:\n  {e}")


if __name__ == "__main__":
    main()

"""
#*При відсутності файла про пацієнтів

MEDASSISTANT (centralized error handling)
==========================================

Loading patients...
✗ File not found:
  [Errno 2] No such file or directory: 'data/patients.json'
"""

"""
MEDASSISTANT (centralized error handling)
==========================================

Loading patients...
✓ JSON loaded

Validating patients...
⚠ 3 invalid patient(s) skipped:
  Patient #0 (Ivan): 'temperature' must be in range 25.0-45.0, got 13.2
  Patient #3 (55): 'id' must be positive, got -4; 'name' must be a string, got 55; 'age' must be an integer, got '61'
  Patient #4 (Petro): 'temperature' must be in range 25.0-45.0, got 58.5
✓ Validation passed for 2 patient(s)

Calculating statistics...
✓ Statistics calculated

Generating report...
✓ Report generated
"""

"""
#report.txt
MEDASSISTANT PATIENT REPORT
===========================

Total valid patients: 2
Average age: 48.0
Average temperature: 37.6
Oldest patient: Petro (61)

Skipped invalid patients: 3
  - Ivan (index 0): 'temperature' must be in range 25.0-45.0, got 13.2
  - 55 (index 3): 'id' must be positive, got -4; 'name' must be a string, got 55; 'age' must be an integer, got '61'
  - Petro (index 4): 'temperature' must be in range 25.0-45.0, got 58.5
"""

"""
#*Порівняння двох архітектур — те, що демонструє цей Challenge:
1.# Твій робочий main.py (розподілена обробка) — try/except НА КОЖНОМУ кроці:
try:
    patients = load_patients(...)
except FileNotFoundError:
    ...
    return                     # ← явний return після КОЖНОГО блоку
except json.JSONDecodeError:
    ...
    return

2.# ... (НАСТУПНИЙ try/except ОКРЕМО, для validate_patients) ...
python
# main_centralized.py (централізована обробка) — ОДИН try, ОДИН набір except:
try:
    patients = load_patients(...)          # ← усі кроки в ОДНОМУ блоці,
    valid, invalid = validate_patients(...)  #   без окремих try/except
    ...
    save_report(...)
except FileNotFoundError as e:
    ...
except json.JSONDecodeError as e:
    ...
except ValueError as e:
    ...

#*Ключова відмінність — де саме "живе" рішення, як обробити помилку:
	                    Розподілена (робочий main.py)	Централізована (main_centralized.py)
Скільки try блоків	    один на кожну стадію	        ОДИН на весь pipeline

Явний return 	        так, у кожному except	        НЕ потрібен — вихід із try автоматичний
після помилки

Легко бачити 	        ✅ дуже точно 	              ⚠️ менш точно — усі except в кінці, 
ЯКА стадія впала        (кожен except                   треба здогадатись за ТИПОМ помилки, 
                        "прив'язаний" до стадії)        яка саме стадія

Довжина коду	        більше (повторюваний шаблон 	коротше — один шаблон на весь файл
                        try/except/return)

Коли краще	            коли КОЖНА стадія 	            коли достатньо ЗАГАЛЬНОЇ реакції 
                        потребує УНІКАЛЬНОЇ,            за ТИПОМ помилки, незалежно від стадії
                        детальної реакції

#*Чому "raise ValueError лише якщо ВСІ невалідні" — важлива зміна логіки:
def validate_patients(patients):
    ...
    if not valid_patients:                 # ← НОВА умова: перевіряємо ЛИШЕ
        raise ValueError(...)                #   якщо СПИСОК ВАЛІДНИХ порожній

    return valid_patients, invalid_entries    # ← інакше — ЗАВЖДИ повертає нормально,
                                                 #   навіть якщо є ЧАСТКОВІ помилки

#*Це узгоджує обидва твої вимоги: 
skip-invalid behavior (частково невалідні пацієнти НЕ зупиняють роботу) та централізовану обробку через except ValueError (яка спрацює лише в дійсно критичному випадку — коли працювати взагалі нема з ким).

#*Головний висновок про "engineering pattern", який демонструє це завдання:

Допоміжні функції (patient_utils.py) відповідають лише за "ЩО сталося" (піднімають точний тип винятку з детальним повідомленням). 
"ЯК про це повідомити користувачу" (print, лог, GUI-діалог) — це відповідальність виключно коду, що викликає ці функції (main()). 
Це розділення дозволяє той самий patient_utils.py перевикористовувати в зовсім іншому контексті (веб-сервер, тестовий набір, інший CLI) без жодних змін — бо він ніколи "не нав'язує" СПОСІБ показу помилки, лише сам факт і причину.
"""
