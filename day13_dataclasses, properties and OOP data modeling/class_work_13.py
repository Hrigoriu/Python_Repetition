"""
# !Task 1 — перший dataclass!

*Створи:
@dataclass
class Patient:
    name: str
    age: int

*Створи 4 пацієнти та покажи:
repr;
порівняння двох однакових пацієнтів;
порівняння двох різних пацієнтів.
"""

from dataclasses import dataclass


@dataclass
class Patient:
    name: str
    age: int


# --- Створюємо 4 пацієнти ---
patient1 = Patient("Ivan", 42)
patient2 = Patient("Olena", 35)
patient3 = Patient("Ivan", 42)      # ← ТІ САМІ значення, що й patient1!
patient4 = Patient("Petro", 61)

# --- 1. repr ---
lines = ["repr():"]
#lines.append(f"  patient1 = {repr(patient1)}")
#lines.append(f"  patient2 = {repr(patient2)}")
#lines.append(f"  patient3 = {repr(patient3)}")
#lines.append(f"  patient4 = {repr(patient4)}")

lines.append(f"  patient1 = {patient1!r}")
lines.append(f"  patient2 = {patient2!r}")
lines.append(f"  patient3 = {patient3!r}")
lines.append(f"  patient4 = {patient4!r}")

lines.append("─" * 55)

# --- 2. Порівняння ОДНАКОВИХ пацієнтів (однакові name/age) ---
lines.append("Порівняння ОДНАКОВИХ (patient1 vs patient3):")
lines.append(f"  patient1 == patient3: {patient1 == patient3}")
lines.append(f"  patient1 is patient3: {patient1 is patient3}")
lines.append(f"  id(patient1) = {id(patient1)}")
lines.append(f"  id(patient3) = {id(patient3)}")
lines.append("─" * 55)

# --- 3. Порівняння РІЗНИХ пацієнтів ---
lines.append("Порівняння РІЗНИХ (patient1 vs patient2):")
lines.append(f"  patient1 == patient2: {patient1 == patient2}")
lines.append(f"  patient1 is patient2: {patient1 is patient2}")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  DATACLASS PATIENT".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌───────────────────────────────────────────────────────────┐
│                      DATACLASS PATIENT                    │
├───────────────────────────────────────────────────────────┤
│  repr():                                                  │
│    patient1 = Patient(name='Ivan', age=42)                │
│    patient2 = Patient(name='Olena', age=35)               │
│    patient3 = Patient(name='Ivan', age=42)                │
│    patient4 = Patient(name='Petro', age=61)               │
│  ───────────────────────────────────────────────────────  │
│  Порівняння ОДНАКОВИХ (patient1 vs patient3):             │
│    patient1 == patient3: True                             │
│    patient1 is patient3: False                            │
│    id(patient1) = 1799414070112                           │
│    id(patient3) = 1799414422480                           │
│  ───────────────────────────────────────────────────────  │
│  Порівняння РІЗНИХ (patient1 vs patient2):                │
│    patient1 == patient2: False                            │
│    patient1 is patient2: False                            │
└───────────────────────────────────────────────────────────┘
"""

"""
*Пояснення @dataclass — головна відмінність від "ручного" класу (Дні 12):
@dataclass
class Patient:
    name: str
    age: int

*Декоратор @dataclass автоматично генерує за тебе:
__init__(self, name, age) — конструктор
__repr__(self) — читабельне представлення
__eq__(self, other) — порівняння за значеннями полів

Тобто весь той код, що ти писав вручну в дні 12 (__init__ із присвоєнням self.name = name, __repr__ з f"Patient(name={self.name!r}, ...)") — @dataclass пише сам, лише за декларацією типів полів.

*repr — генерується автоматично, у ТОМУ Ж стилі, що й твій ручний __repr__:
repr(patient1)
# → "Patient(name='Ivan', age=42)"

Зверни увагу — це той самий формат, що ти писав вручну в __repr__ дня 12 (Patient(name='Ivan', age=42)) — @dataclass просто автоматизує написання коду, який ти вже розумієш як написати сам.

*Порівняння ОДНАКОВИХ пацієнтів — == перевіряє ЗНАЧЕННЯ, а НЕ ідентичність:
patient1 = Patient("Ivan", 42)
patient3 = Patient("Ivan", 42)    # СТВОРЕНО ОКРЕМО, але з ТИМИ САМИМИ значеннями

patient1 == patient3    # → True!  @dataclass ГЕНЕРУЄ __eq__, який порівнює
                          #         name ТА age ОБОХ об'єктів
patient1 is patient3     # → False  Це ВСЕ ОДНО ДВА РІЗНІХ об'єкти в пам'яті!
id(patient1) != id(patient3)   # РІЗНІ адреси пам'яті

*Це — КЛЮЧОВА відмінність від "звичайного" класу БЕЗ @dataclass:
# Клас БЕЗ @dataclass (як твій ручний Patient з дня 12) — БЕЗ автоматичного __eq__:
class PlainPatient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = PlainPatient("Ivan", 42)
p2 = PlainPatient("Ivan", 42)
p1 == p2   # → False!!! ⚠️ Python порівнює ЗА ЗАМОВЧУВАННЯМ через `is`
             #             (тобто за ІДЕНТИЧНІСТЮ), якщо __eq__ НЕ визначено

# @dataclass Patient (ЦЕ завдання) — З автоматичним __eq__:
patient1 = Patient("Ivan", 42)
patient3 = Patient("Ivan", 42)
patient1 == patient3   # → True!  @dataclass ЗГЕНЕРУВАВ __eq__ за ТЕБЕ

*Порівняння РІЗНИХ пацієнтів — очевидно False для ОБОХ перевірок:
patient1 = Patient("Ivan", 42)
patient2 = Patient("Olena", 35)

patient1 == patient2    # → False  (name та age РІЗНІ)
patient1 is patient2     # → False  (це і РІЗНІ об'єкти, і РІЗНІ значення)

*Головний висновок цього завдання:
	is	== (з @dataclass)
Що перевіряє	ОДИН і той самий об'єкт у пам'яті	ОДНАКОВІ значення полів
patient1 vs patient3 (однакові name/age, різні об'єкти)	False	True
patient1 vs patient2 (різні name/age)	False	False

@dataclass автоматизує саме той "ручний" код, який довелось би писати самостійно, щоб == порівнювало сенс, а не лише адресу пам'яті — це і є головна практична причина, чому @dataclass так широко використовується для класів, що зберігають дані (як Patient), а не мають складної поведінки.
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 2 — default values!

Додай:
diagnosis: str = "unknown"
temperature: float = 36.6

Створи пацієнтів:
Patient("Ivan", 42)
Patient("Olena", 35, "rhinitis", 37.2)
"""

from dataclasses import dataclass


@dataclass
class Patient:
    name: str
    age: int
    diagnosis: str = "unknown"
    temperature: float = 36.6


# --- Створюємо пацієнтів за умовою ---
patient1 = Patient("Ivan", 42)
patient2 = Patient("Olena", 35, "rhinitis", 37.2)

# --- Вивід у рамці ---
lines = [
    f"Patient('Ivan', 42)                       → {patient1}",
    f"Patient('Olena', 35, 'rhinitis', 37.2)    → {patient2}",
    "─" * 60,
    f"patient1.diagnosis   = {patient1.diagnosis!r}",
    f"patient1.temperature = {patient1.temperature}",
    f"patient2.diagnosis    = {patient2.diagnosis!r}",
    f"patient2.temperature  = {patient2.temperature}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  DEFAULT VALUES".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                     DEFAULT VALUES                                                  │
├─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│  Patient('Ivan', 42)                       → Patient(name='Ivan', age=42, diagnosis='unknown', temperature=36.6)    │
│  Patient('Olena', 35, 'rhinitis', 37.2)    → Patient(name='Olena', age=35, diagnosis='rhinitis', temperature=37.2)  │
│  ────────────────────────────────────────────────────────────                                                       │
│  patient1.diagnosis   = 'unknown'                                                                                   │
│  patient1.temperature = 36.6                                                                                        │
│  patient2.diagnosis    = 'rhinitis'                                                                                 │
│  patient2.temperature  = 37.2                                                                                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
*Пояснення значень за замовчуванням у @dataclass:
@dataclass
class Patient:
    name: str                       # ← ОБОВ'ЯЗКОВЕ поле (немає значення за замовчуванням)
    age: int                          # ← теж ОБОВ'ЯЗКОВЕ
    diagnosis: str = "unknown"          # ← НЕОБОВ'ЯЗКОВЕ, якщо не передати — буде "unknown"
    temperature: float = 36.6            # ← теж НЕОБОВ'ЯЗКОВЕ, за замовчуванням 36.6

*Що відбувається для КОЖНОГО виклику:
Patient("Ivan", 42)
# name="Ivan", age=42       ← передано ЯВНО
# diagnosis="unknown"        ← НЕ передано → взято ЗНАЧЕННЯ ЗА ЗАМОВЧУВАННЯМ
# temperature=36.6            ← НЕ передано → взято ЗНАЧЕННЯ ЗА ЗАМОВЧУВАННЯМ

Patient("Olena", 35, "rhinitis", 37.2)
# name="Olena", age=35, diagnosis="rhinitis", temperature=37.2
# ← ВСІ чотири передано ЯВНО, жодних дефолтів не використано

*Важливе синтаксичне правило @dataclass (і Python-функцій узагалі) — порядок полів має значення:
@dataclass
class Patient:
    name: str                      # ← поля БЕЗ дефолту
    age: int                         #    МАЮТЬ йти ПЕРШИМИ
    diagnosis: str = "unknown"          # ← поля З дефолтом —
    temperature: float = 36.6            #    ЛИШЕ ПІСЛЯ обов'язкових

# ❌ ТАК НЕ МОЖНА — SyntaxError:
@dataclass
class Patient:
    diagnosis: str = "unknown"    # ← поле З дефолтом ПЕРШЕ
    name: str                       # ← а ОБОВ'ЯЗКОВЕ поле ПІСЛЯ нього
# 💥 TypeError: non-default argument 'name' follows default argument

Причина: якби Python дозволив такий порядок, при виклику Patient("Ivan") було б неоднозначно — чи "Ivan" іде в diagnosis (перше поле за позицією), чи в name (перше обов'язкове)? Python вимагає чіткого правила: спочатку всі обов'язкові, потім усі з дефолтом.

Зв'язок із Task 2 із дня "функції" (create_measurement з *, keyword-only параметри):

Це схоже обмеження на те, що вже зустрічалось у функціях: def f(a, *, b, c=10) — параметри з дефолтом завжди йдуть після обов'язкових. @dataclass "під капотом" генерує саме такий __init__, тому й успадковує те саме правило порядку.

*Автоматичний __repr__ тепер показує ВСІ чотири поля:
print(patient1)
# → Patient(name='Ivan', age=42, diagnosis='unknown', temperature=36.6)
#                                 ↑                     ↑
#                          НАВІТЬ значення ЗА ЗАМОВЧУВАННЯМ
#                          показані у repr, як і явно передані
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 3 — default_factory!

Додай:
diagnoses: list[str]

але використай:
field(default_factory=list)

Перевір, що два пацієнти мають різні списки:
patient1.diagnoses.append("sinusitis")

та переконайся, що:
patient2.diagnoses
не змінився.
"""

#variant #1
from dataclasses import dataclass, field


# --- Правильний варіант — default_factory ---
@dataclass
class Patient:
    name: str
    age: int
    diagnosis: str = "unknown"
    temperature: float = 36.6
    diagnoses: list[str] = field(default_factory=list)


# --- Спроба НЕПРАВИЛЬНОГО варіанту — Python ВІДМОВЛЯЄ одразу ---
try:
    exec("""
@dataclass
class BadPatient:
    name: str
    diagnoses: list[str] = []
""")
except ValueError as e:
    bad_variant_error = f"❌ ValueError: {e}"

# --- Демонстрація: два пацієнти мають РІЗНІ списки ---
patient1 = Patient("Ivan", 42)
patient2 = Patient("Olena", 35)

patient1.diagnoses.append("sinusitis")

# --- Вивід у рамці ---
lines = [
    f"НЕПРАВИЛЬНИЙ варіант (diagnoses: list[str] = []):",
    f"  {bad_variant_error}",
    "─" * 60,
    f"patient1 = {patient1}",
    f"patient2 = {patient2}",
    "─" * 60,
    f"patient1.diagnoses.append('sinusitis') виконано.",
    f"patient1.diagnoses = {patient1.diagnoses}",
    f"patient2.diagnoses = {patient2.diagnoses}",
    f"patient1.diagnoses is patient2.diagnoses: {patient1.diagnoses is patient2.diagnoses}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  DEFAULT_FACTORY".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                               DEFAULT_FACTORY                                             │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│  НЕПРАВИЛЬНИЙ варіант (diagnoses: list[str] = []):                                                        │
│    ❌ ValueError: mutable default <class 'list'> for field diagnoses is not allowed: use default_factory│
│  ────────────────────────────────────────────────────────────                                             │
│  patient1 = Patient(name='Ivan', age=42, diagnosis='unknown', temperature=36.6, diagnoses=['sinusitis'])  │
│  patient2 = Patient(name='Olena', age=35, diagnosis='unknown', temperature=36.6, diagnoses=[])            │
│  ────────────────────────────────────────────────────────────                                             │
│  patient1.diagnoses.append('sinusitis') виконано.                                                         │
│  patient1.diagnoses = ['sinusitis']                                                                       │
│  patient2.diagnoses = []                                                                                  │
│  patient1.diagnoses is patient2.diagnoses: False                                                          │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
"""

#variant #2
from dataclasses import dataclass, field


# --- Правильний варіант — default_factory ---
@dataclass
class Patient:
    name: str
    age: int
    diagnosis: str = "unknown"
    temperature: float = 36.6
    diagnoses: list[str] = field(default_factory=list)


# --- Безпечний варіант — використовуємо field(default_factory=list) ---
try:
    @dataclass
    class BadPatient:
        name: str
        diagnoses: list[str] = field(default_factory=list)
except ValueError as e:
    bad_variant_error = f"❌ ValueError: {e}"
else:
    bad_variant_error = "✅ field(default_factory=list) дозволяє створювати новий список для кожного екземпляра"

# --- Демонстрація: два пацієнти мають РІЗНІ списки ---
patient1 = Patient("Ivan", 42)
patient2 = Patient("Olena", 35)

patient1.diagnoses.append("sinusitis")

# --- Вивід у рамці ---
lines = [
    "БЕЗПЕЧНИЙ варіант (diagnoses: list[str] = field(default_factory=list)):",
    f"  {bad_variant_error}",
    "─" * 60,
    f"patient1 = {patient1}",
    f"patient2 = {patient2}",
    "─" * 60,
    "patient1.diagnoses.append('sinusitis') виконано.",
    f"patient1.diagnoses = {patient1.diagnoses}",
    f"patient2.diagnoses = {patient2.diagnoses}",
    f"patient1.diagnoses is patient2.diagnoses: {patient1.diagnoses is patient2.diagnoses}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  DEFAULT_FACTORY".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                               DEFAULT_FACTORY                                             │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│  БЕЗПЕЧНИЙ варіант (diagnoses: list[str] = field(default_factory=list)):                                  │
│    ✅ field(default_factory=list) дозволяє створювати новий список для кожного екземпляра│
│  ────────────────────────────────────────────────────────────                                             │
│  patient1 = Patient(name='Ivan', age=42, diagnosis='unknown', temperature=36.6, diagnoses=['sinusitis'])  │
│  patient2 = Patient(name='Olena', age=35, diagnosis='unknown', temperature=36.6, diagnoses=[])            │
│  ────────────────────────────────────────────────────────────                                             │
│  patient1.diagnoses.append('sinusitis') виконано.                                                         │
│  patient1.diagnoses = ['sinusitis']                                                                       │
│  patient2.diagnoses = []                                                                                  │
│  patient1.diagnoses is patient2.diagnoses: False                                                          │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
*Пояснення field(default_factory=list) — навіщо потрібна ЦЯ конструкція:
diagnoses: list[str] = field(default_factory=list)
#                       ↑                    ↑
#                    field() — спеціальна функція   list — САМА ФУНКЦІЯ (без дужок!),
#                    для налаштування поля            яку @dataclass ВИКЛИЧЕ
#                                                       ОКРЕМО для КОЖНОГО нового об'єкта

default_factory=list означає: "щоразу, коли створюється НОВИЙ Patient без явного diagnoses, викликай list() — і отримаєш НОВИЙ, порожній список". Це принципово відрізняється від звичайного дефолту (diagnosis: str = "unknown"), де одне й те саме значення "unknown" просто "копіюється" для кожного об'єкта.

*Чому Python ВІДМОВЛЯЄ, якщо написати diagnoses: list[str] = [] напряму:
❌ ValueError: mutable default <class 'list'> for field diagnoses is not allowed: use default_factory

Це та сама пастка, що вже розбиралась у Дні 11 (Challenge 2 — "mutable default argument" для звичайних функцій, def add_patient(name, patients=[])). Там та сама проблема виникала тихо, і потрібно було самому здогадатись, чому список "накопичується" між викликами. 
@dataclass явно захищає від цієї пастки: не дозволяє навіть написати такий код — Python одразу кидає ValueError під час визначення класу, ще до того, як хтось встиг би створити хоч один об'єкт.

*Чому [] напряму було б небезпечно (та сама логіка, що й для функцій):
# Якби Python ДОЗВОЛИВ diagnoses: list[str] = []:
@dataclass
class Patient:
    diagnoses: list[str] = []   # ЯКБИ це спрацювало...

patient1 = Patient()
patient2 = Patient()

patient1.diagnoses.append("sinusitis")
# patient2.diagnoses теж показав би ["sinusitis"]!!! ⚠️
# Бо ОБИДВА patient1.diagnoses і patient2.diagnoses вказували б
# на ОДИН і той самий список [] — точно як у func(patients=[]) з Дня 11

*Порівняння двох способів дефолту:
diagnosis: str = "unknown"                       # ← ЗВИЧАЙНИЙ дефолт: ОДНЕ значення,
                                                     #   яке БЕЗПЕЧНО "копіюється" (рядки immutable)

diagnoses: list[str] = field(default_factory=list)   # ← ФАБРИКА: ФУНКЦІЯ, яку
                                                         #   ВИКЛИКАЮТЬ ЗАНОВО для КОЖНОГО об'єкта

str безпечний як звичайний дефолт, бо він незмінний (immutable) — навіть якщо два об'єкти "поділяють" одне значення "unknown", жоден з них не може змінити цей рядок "на місці" (можна лише замінити цілком, що не впливає на інші об'єкти). list — змінний (mutable), тому потребує default_factory, щоб гарантувати НОВИЙ, окремий список щоразу.

*Доказ, що patient1.diagnoses і patient2.diagnoses — РІЗНІ об'єкти:
patient1.diagnoses is patient2.diagnoses   # → False!  Це ДВА окремих списки в пам'яті

patient1.diagnoses.append("sinusitis")
# patient1.diagnoses = ["sinusitis"]    ← ЗМІНИВСЯ
# patient2.diagnoses = []                 ← НЕ ЗМІНИВСЯ, залишився порожнім
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 4 — __post_init__!

Реалізуй:
def __post_init__(self) -> None:
    ...

Правила:
name не може бути порожнім
age > 0
temperature > 0

Некоректні значення повинні викликати:
ValueError
"""

from dataclasses import dataclass, field


@dataclass
class Patient:
    name: str
    age: int
    diagnosis: str = "unknown"
    temperature: float = 36.6
    diagnoses: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Перевіряє коректність полів ОДРАЗУ ПІСЛЯ того, як @dataclass
        згенерований __init__ вже присвоїв усі значення.

        Collect-all: перевіряє ВСІ три умови, накопичує ВСІ помилки,
        і піднімає ОДНЕ ValueError з повним переліком.
        """
        errors = []

        if not self.name or not self.name.strip():
            errors.append(f"name не може бути порожнім, отримано: {self.name!r}")

        if self.age <= 0:
            errors.append(f"age має бути більшим за 0, отримано: {self.age}")

        if self.temperature <= 0:
            errors.append(f"temperature має бути більшою за 0, отримано: {self.temperature}")

        if errors:
            raise ValueError("Некоректні дані пацієнта: " + "; ".join(errors))


# --- Демонстрація ---
test_cases = [
    ("Ivan", 42, "unknown", 36.6),        # ✅ валідний
    ("", 42, "unknown", 36.6),              # ❌ порожнє name
    ("Ivan", -5, "unknown", 36.6),            # ❌ невірний age
    ("", -5, "unknown", -1.0),                  # ❌❌❌ ВСІ три помилки одразу
]

lines = []
for name, age, diagnosis, temperature in test_cases:
    try:
        patient = Patient(name, age, diagnosis, temperature)
        lines.append(f"Patient({name!r}, {age}, ...)  →  ✅ {patient}")
    except ValueError as e:
        lines.append(f"Patient({name!r}, {age}, ...)  →  ❌ {e}")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  __POST_INIT__".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                                         __POST_INIT__                                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│  Patient('Ivan', 42, ...)  →  ✅ 
            Patient(name='Ivan', age=42, diagnosis='unknown', temperature=36.6, diagnoses=[])│
│  Patient('', 42, ...)  →  ❌ Некоректні дані пацієнта: 
                            name не може бути порожнім, отримано: ''          │
│  Patient('Ivan', -5, ...)  →  ❌ Некоректні дані пацієнта: 
                                age має бути більшим за 0, отримано:-5        │
│  Patient('', -5, ...)  →  ❌ Некоректні дані пацієнта: 
                            name не може бути порожнім, отримано: ''; 
                            age має бути більшим за 0, отримано: -5; 
                            temperature має бути більшою за 0, отримано: -1.0  │
└──────────────────────────────────────────────────────────────────────────────┘
"""

"""
#*Пояснення __post_init__ — коли саме він викликається:
patient = Patient("Ivan", 42)
# КРОК 1: @dataclass ЗГЕНЕРОВАНИЙ __init__ ВИКОНУЄТЬСЯ ПЕРШИМ:
#          self.name = "Ivan"
#          self.age = 42
#          self.diagnosis = "unknown"
#          self.temperature = 36.6
#          self.diagnoses = []
# КРОК 2: ОДРАЗУ ПІСЛЯ цього, @dataclass САМ викликає __post_init__(self)
#          (якщо цей метод визначено в класі)

Назва "post_init" буквально означає "після ініціалізації" — це гачок (hook), який @dataclass автоматично викликає одразу після того, як звичайний __init__ завершив присвоєння всіх полів.

#*Чому валідація йде саме в __post_init__, а не десь інакше:
@dataclass
class Patient:
    name: str
    age: int
    ...

    def __post_init__(self):
        if self.age <= 0:      # ← ТУТ self.age ВЖЕ ІСНУЄ! __init__ уже присвоїв його
            raise ValueError(...)

@dataclass сам генерує __init__ — ти не пишеш його вручну, тому немає місця, куди можна було б "вставити" перевірку всередині самого __init__ (як робилось у Дні 12 для класу PatientRecord, написаного вручну). 
__post_init__ — це офіційний, передбачений спосіб @dataclass додати власну логіку після автоматичної ініціалізації.

#*Порівняння з "ручним" PatientRecord із Дня 12:
# Ручний клас (День 12) — валідація ВСЕРЕДИНІ __init__, ПЕРЕД self.age = age:
class PatientRecord:
    def __init__(self, name, age):
        if age <= 0:
            raise ValueError(...)   # ← ПЕРЕВІРКА ПЕРЕД присвоєнням
        self.age = age

# @dataclass (це завдання) — валідація ПІСЛЯ автоматичного присвоєння:
@dataclass
class Patient:
    name: str
    age: int

    def __post_init__(self):
        if self.age <= 0:            # ← ПЕРЕВІРКА ПІСЛЯ self.age = age (вже сталось)
            raise ValueError(...)

Різний порядок (до чи після присвоєння), але однаковий кінцевий результат: якщо валідація провалилась, raise все одно зупиняє створення об'єкта — виклик Patient(...) завершиться помилкою, а не поверне "напівготовий" об'єкт, навіть якщо технічно self.age вже був присвоєний за мить до перевірки.

#*Демонстрація "потрійної" помилки для четвертого тестового випадку:
Patient("", -5, "unknown", -1.0)
# __init__ присвоює: self.name="", self.age=-5, self.temperature=-1.0
# __post_init__ перевіряє ВСІ ТРИ:
#   name="" → порожнє → errors.append(...)
#   age=-5 → <=0 → errors.append(...)
#   temperature=-1.0 → <=0 → errors.append(...)
# raise ValueError("Некоректні дані пацієнта: name...; age...; temperature...")
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 5 — classmethod!

Створи:
@classmethod
def from_dict(
    cls,
    data: dict,
) -> "Patient":
    ...

і:
data = {
    "name": "Ivan",
    "age": 42,
    "diagnosis": "sinusitis",
}

Перетвори його в:
Patient(...)
"""

from dataclasses import dataclass, field


@dataclass
class Patient:
    name: str
    age: int
    diagnosis: str = "unknown"
    temperature: float = 36.6
    diagnoses: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        errors = []

        if not self.name or not self.name.strip():
            errors.append(f"name не може бути порожнім, отримано: {self.name!r}")
        if self.age <= 0:
            errors.append(f"age має бути більшим за 0, отримано: {self.age}")
        if self.temperature <= 0:
            errors.append(f"temperature має бути більшою за 0, отримано: {self.temperature}")

        if errors:
            raise ValueError("Некоректні дані пацієнта: " + "; ".join(errors))

    @classmethod
    def from_dict(cls, data: dict) -> "Patient":
        """Створює Patient зі звичайного dict (наприклад, запису з JSON).

        .get() з ТИМИ САМИМИ дефолтами, що й у самому класі — якщо
        поля немає в dict, Patient все одно отримає ЗВИЧНЕ значення
        за замовчуванням, а не помилку.
        """
        return cls(
            name=data["name"],                                # обов'язкове — KeyError, якщо немає
            age=data["age"],                                     # обов'язкове — KeyError, якщо немає
            diagnosis=data.get("diagnosis", "unknown"),             # той самий дефолт, що в @dataclass
            temperature=data.get("temperature", 36.6),                # той самий дефолт, що в @dataclass
        )


# --- Дані за умовою завдання ---
data = {
    "name": "Ivan",
    "age": 42,
    "diagnosis": "sinusitis",
}

patient = Patient.from_dict(data)

# --- Вивід у рамці ---
lines = [
    f"data = {data}",
    "─" * 60,
    f"Patient.from_dict(data)  →  {patient}",
    "─" * 60,
    f"patient.name        = {patient.name!r}",
    f"patient.age          = {patient.age}",
    f"patient.diagnosis     = {patient.diagnosis!r}",
    f"patient.temperature    = {patient.temperature}  (взято ЗА ЗАМОВЧУВАННЯМ, бо не було в data)",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  PATIENT.FROM_DICT()".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌───────────────────────────────────────────────────────────────────────────────────────┐
│                                                 PATIENT.FROM_DICT()                   │
├───────────────────────────────────────────────────────────────────────────────────────┤
│  data = {'name': 'Ivan', 'age': 42, 'diagnosis': 'sinusitis'}                         │
│  ────────────────────────────────────────────────────────────                         │
│  Patient.from_dict(data)  
→  Patient(name='Ivan', age=42, diagnosis='sinusitis', temperature=36.6, diagnoses=[])  │
│  ────────────────────────────────────────────────────────────                         │
│  patient.name        = 'Ivan'                                                         │
│  patient.age          = 42                                                            │
│  patient.diagnosis     = 'sinusitis'                                                  │
│  patient.temperature    = 36.6  (взято ЗА ЗАМОВЧУВАННЯМ, бо не було в data)           │
└───────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
#*Пояснення @classmethod — навіщо потрібен саме такий тип методу:
@classmethod
def from_dict(cls, data: dict) -> "Patient":
    return cls(name=data["name"], ...)

Ключова відмінність від звичайних методів (is_adult(), calculate_bmi() з попередніх днів): звичайний метод отримує self — вже існуючий об'єкт. 
@classmethod отримує cls — сам клас, ще до того, як об'єкт створений. 

#*from_dict() можна викликати без жодного попереднього об'єкта:
Patient.from_dict(data)   # ← викликаємо НА КЛАСІ, а не на екземплярі
#       ↑
#   cls = Patient (сам клас, як "фабрика")

#*Чому саме cls, а не Patient буквально всередині методу:
@classmethod
def from_dict(cls, data):
    return cls(name=data["name"], ...)   # ← cls(...) — те саме, що Patient(...)

cls — це параметризоване посилання на клас, через яке метод був викликаний. Використання cls замість жорстко "зашитого" Patient — це застосування принципу Open/Closed: якщо колись з'явиться підклас Patient (наприклад, VIPPatient), і хтось викличе VIPPatient.from_dict(data), метод автоматично створить VIPPatient, а не завжди Patient — без потреби переписувати from_dict() для кожного підкласу.

#*Пояснення .get() із ТИМИ САМИМИ дефолтами, що й @dataclass:
diagnosis=data.get("diagnosis", "unknown")
#                              ↑
#                   ТОЧНО ТЕ САМЕ значення, що написано в
#                   @dataclass class Patient: diagnosis: str = "unknown"

Це важливий нюанс дизайну: два місця в коді (@dataclass поле і from_dict()) повинні узгоджено "знати" про однакове значення "unknown" — якщо колись дефолт Patient зміниться, доведеться не забути оновити і from_dict(), інакше вони "розсинхронізуються" (порушення DRY, яке варто мати на увазі — детальніше нижче).

#*Чому name/age — через data["name"] (без .get()), а diagnosis/temperature — через .get():
name=data["name"]            # ← ОБОВ'ЯЗКОВЕ: якщо "name" немає в dict —
                                #   КОРЕКТНО кинути KeyError, бо Patient НЕ МАЄ
                                #   дефолту для name (обов'язкове поле)

diagnosis=data.get("diagnosis", "unknown")   # ← НЕОБОВ'ЯЗКОВЕ: у Patient
                                                #   ВЖЕ Є дефолт "unknown" —
                                                #   from_dict() лише ПОВТОРЮЄ цю ж поведінку

Це узгоджується з тим, які поля мають дефолт у @dataclass Patient, а які — ні: from_dict() дзеркалить ту саму структуру обов'язковості.

#*Зауваження про DRY (потенційне вдосконалення на майбутнє):
Дефолти "unknown" і 36.6 зараз "написані двічі" — раз у @dataclass, раз у from_dict(). Строго дотримуючись DRY, можна було б уникнути цього дублювання (наприклад, викликаючи cls(**{k: v for k, v in data.items() if k in ...}) або через dataclasses.fields()), але для навчального прикладу явний .get() з тими самими значеннями — найпростіший (KISS) і найзрозуміліший варіант.
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 6 — staticmethod!

Додай:
@staticmethod
def is_valid_age(age: int) -> bool:
    ...

Перевір:
17 → False
18 → True
42 → True
-5 → False
"""

from dataclasses import dataclass, field


@dataclass
class Patient:
    name: str
    age: int
    diagnosis: str = "unknown"
    temperature: float = 36.6
    diagnoses: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        errors = []

        if not self.name or not self.name.strip():
            errors.append(f"name не може бути порожнім, отримано: {self.name!r}")
        if self.age <= 0:
            errors.append(f"age має бути більшим за 0, отримано: {self.age}")
        if self.temperature <= 0:
            errors.append(f"temperature має бути більшою за 0, отримано: {self.temperature}")

        if errors:
            raise ValueError("Некоректні дані пацієнта: " + "; ".join(errors))

    @classmethod
    def from_dict(cls, data: dict) -> "Patient":
        return cls(
            name=data["name"],
            age=data["age"],
            diagnosis=data.get("diagnosis", "unknown"),
            temperature=data.get("temperature", 36.6),
        )

    @staticmethod
    def is_valid_age(age: int) -> bool:
        """Перевіряє, чи вік відповідає повноліттю (>= 18).

        @staticmethod — бо перевіряє ПЕРЕДАНЕ значення, а НЕ self.age
        конкретного об'єкта. Можна викликати БЕЗ жодного Patient:
        Patient.is_valid_age(20) — так само, як _check_id() у Дні 12.
        """
        return age >= 18


# --- Перевірка за умовою завдання ---
test_ages = [17, 18, 42, -5]

lines = [f"Patient.is_valid_age({age})  →  {Patient.is_valid_age(age)}" for age in test_ages]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  IS_VALID_AGE()".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌──────────────────────────────────────┐
│             IS_VALID_AGE()           │
├──────────────────────────────────────┤
│  Patient.is_valid_age(17)  →  False  │
│  Patient.is_valid_age(18)  →  True   │
│  Patient.is_valid_age(42)  →  True   │
│  Patient.is_valid_age(-5)  →  False  │
└──────────────────────────────────────┘
"""

"""
#*Пояснення @staticmethod у контексті @dataclass — та сама логіка, що й у _check_* методах Дня 12:
@staticmethod
def is_valid_age(age: int) -> bool:
    return age >= 18

is_valid_age() не звертається до self — вона перевіряє передане значення age, а не self.age конкретного об'єкта. Тому її можна викликати напряму на класі, без створення жодного Patient:
Patient.is_valid_age(20)   # → True
#        ↑
#   викликаємо НА КЛАСІ, БЕЗ жодного екземпляра Patient

#*Три способи виклику @staticmethod — усі working однаково:
Patient.is_valid_age(42)         # ✅ на КЛАСІ (найпоширеніший спосіб)

patient1 = Patient("Ivan", 42)
patient1.is_valid_age(42)          # ✅ на ЕКЗЕМПЛЯРІ (теж працює, хоч і незвично)

Patient.is_valid_age(patient1.age)   # ✅ передаємо age КОНКРЕТНОГО пацієнта

#*Порівняння трьох типів методів, які вже зустрічались у Дні 12/13 — узагальнена таблиця:
class Patient:
    def is_adult(self) -> bool:              # ЗВИЧАЙНИЙ метод — потребує self.age
        return self.age >= 18                 #   (ЧИТАЄ стан конкретного об'єкта)

    @classmethod
    def from_dict(cls, data) -> "Patient":     # CLASSMETHOD — потребує cls (сам клас)
        return cls(...)                          #   (СТВОРЮЄ новий об'єкт)

    @staticmethod
    def is_valid_age(age) -> bool:               # STATICMETHOD — НЕ потребує self/cls
        return age >= 18                           #   (лише ОБРОБЛЯЄ передане значення)

	                Перший параметр	        Для чого
Звичайний метод	    self	                працює з конкретним, ВЖЕ ІСНУЮЧИМ об'єктом
@classmethod	    cls	                    створює НОВИЙ об'єкт (як "альтернативний конструктор")
@staticmethod	    — (нічого)	            допоміжна логіка, ТЕМАТИЧНО пов'язана з класом, 
                                            але не залежить ані від конкретного об'єкта, 
                                            ані від класу

#*Практична цінність is_valid_age() — можна перевіряти ЩЕ ДО створення об'єкта:
# Уяви форму реєстрації пацієнта, де треба ПЕРЕВІРИТИ вік
# ще ДО того, як користувач надішле дані на створення Patient:

user_input_age = 15

if not Patient.is_valid_age(user_input_age):
    print("⚠ Цей розділ призначений лише для дорослих пацієнтів")
else:
    patient = Patient("Sofia", user_input_age)   # ← створюємо ЛИШЕ якщо перевірка пройшла

Це той самий принцип Fail Fast, щойно доданий до твоїх принципів написання коду: перевірка раніше, ще до дорогої операції (створення об'єкта, запис у базу тощо), а не постфактум.
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 7 — property!

Створи клас:
class Patient:
    ...

зі внутрішнім:
_age

і property:
age

Setter повинен забороняти:
0
-1
"42"
"""

from dataclasses import InitVar, dataclass, field


@dataclass
class Patient:
    name: str
    age: InitVar[int]                                 # ← приймається як параметр КОНСТРУКТОРА,
                                                          #   але НЕ зберігається як звичайне поле
    diagnosis: str = "unknown"
    temperature: float = 36.6
    diagnoses: list[str] = field(default_factory=list)
    _age: int = field(init=False, default=0)             # ← РЕАЛЬНЕ сховище значення age

    def __post_init__(self, age: int) -> None:
        """age тут — це параметр, переданий у Patient(...), а НЕ self.age."""
        errors = []

        if not self.name or not self.name.strip():
            errors.append(f"name не може бути порожнім, отримано: {self.name!r}")
        if self.temperature <= 0:
            errors.append(f"temperature має бути більшою за 0, отримано: {self.temperature}")

        if errors:
            raise ValueError("Некоректні дані пацієнта: " + "; ".join(errors))

        self.age = age   # ← ЦЕЙ рядок проходить ЧЕРЕЗ property-setter нижче!

    @property
    def age(self) -> int:
        """Getter — повертає значення з ВНУТРІШНЬОГО _age."""
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        """Setter — забороняє 0, від'ємні числа та рядки."""
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"age має бути int, отримано {value!r} ({type(value).__name__})")
        if value <= 0:
            raise ValueError(f"age має бути більшим за 0, отримано {value}")
        self._age = value

    @classmethod
    def from_dict(cls, data: dict) -> "Patient":
        return cls(
            name=data["name"],
            age=data["age"],
            diagnosis=data.get("diagnosis", "unknown"),
            temperature=data.get("temperature", 36.6),
        )

    @staticmethod
    def is_valid_age(age: int) -> bool:
        return age >= 18


# --- Демонстрація за умовою завдання ---
lines = []

patient = Patient("Ivan", 42)
lines.append(f"Patient('Ivan', 42)  →  ✅ age={patient.age}, {patient}")

for bad_value in [0, -1, "42"]:
    try:
        Patient("Test", bad_value)
        lines.append(f"Patient('Test', {bad_value!r})  →  ✅ (НЕ мало пройти!)")
    except (ValueError, TypeError) as e:
        lines.append(f"Patient('Test', {bad_value!r})  →  ❌ {type(e).__name__}: {e}")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  PROPERTY / SETTER".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""

┌───────────────────────────────────────────────────────────┐
│                      DATACLASS PATIENT                    │
├───────────────────────────────────────────────────────────┤
│  repr():                                                  │
│    patient1 = Patient(name='Ivan', age=42)                │
│    patient2 = Patient(name='Olena', age=35)               │
│    patient3 = Patient(name='Ivan', age=42)                │
│    patient4 = Patient(name='Petro', age=61)               │
│  ───────────────────────────────────────────────────────  │
│  Порівняння ОДНАКОВИХ (patient1 vs patient3):             │
│    patient1 == patient3: True                             │
│    patient1 is patient3: False                            │
│    id(patient1) = 2004722303056                           │
│    id(patient3) = 2004721491216                           │
│  ───────────────────────────────────────────────────────  │
│  Порівняння РІЗНИХ (patient1 vs patient2):                │
│    patient1 == patient2: False                            │
│    patient1 is patient2: False                            │
└───────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────┐
│                                                     DEFAULT VALUES             │
├────────────────────────────────────────────────────────────────────────────────┤
│  Patient('Ivan', 42)                       
        → Patient(name='Ivan', age=42, diagnosis='unknown', temperature=36.6)    │
│  Patient('Olena', 35, 'rhinitis', 37.2)    
        → Patient(name='Olena', age=35, diagnosis='rhinitis', temperature=37.2)  │
│  ────────────────────────────────────────────────────────────                  │
│  patient1.diagnosis   = 'unknown'                                              │
│  patient1.temperature = 36.6                                                   │
│  patient2.diagnosis    = 'rhinitis'                                            │
│  patient2.temperature  = 37.2                                                  │
└────────────────────────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                               DEFAULT_FACTORY                                             │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│  НЕПРАВИЛЬНИЙ варіант (diagnoses: list[str] = []):                                                        │
│    ❌ ValueError: mutable default <class 'list'> for field diagnoses is not allowed: use default_factory  │
│  ────────────────────────────────────────────────────────────                                             │
│  patient1 = Patient(name='Ivan', age=42, diagnosis='unknown', temperature=36.6, diagnoses=['sinusitis'])  │
│  patient2 = Patient(name='Olena', age=35, diagnosis='unknown', temperature=36.6, diagnoses=[])            │
│  ────────────────────────────────────────────────────────────                                             │
│  patient1.diagnoses.append('sinusitis') виконано.                                                         │
│  patient1.diagnoses = ['sinusitis']                                                                       │
│  patient2.diagnoses = []                                                                                  │
│  patient1.diagnoses is patient2.diagnoses: False                                                          │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                               DEFAULT_FACTORY                                             │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│  БЕЗПЕЧНИЙ варіант (diagnoses: list[str] = field(default_factory=list)):                                  │
│    ✅ field(default_factory=list) дозволяє створювати новий список для кожного екземпляра                 │
│  ────────────────────────────────────────────────────────────                                             │
│  patient1 = Patient(name='Ivan', age=42, diagnosis='unknown', temperature=36.6, diagnoses=['sinusitis'])  │
│  patient2 = Patient(name='Olena', age=35, diagnosis='unknown', temperature=36.6, diagnoses=[])            │
│  ────────────────────────────────────────────────────────────                                             │
│  patient1.diagnoses.append('sinusitis') виконано.                                                         │
│  patient1.diagnoses = ['sinusitis']                                                                       │
│  patient2.diagnoses = []                                                                                  │
│  patient1.diagnoses is patient2.diagnoses: False                                                          │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              __POST_INIT__                                                     │
├────────────────────────────────────────────────────────────────────────────────────────────────┤
│  Patient('Ivan', 42, ...)  
        →  ✅ Patient(name='Ivan', age=42, diagnosis='unknown', temperature=36.6, diagnoses=[])  │
│  Patient('', 42, ...)  
        →  ❌ Некоректні дані пацієнта: name не може бути порожнім, отримано: ''                 │
│  Patient('Ivan', -5, ...)  
        →  ❌ Некоректні дані пацієнта: age має бути більшим за 0, отримано: -5                  │
│  Patient('', -5, ...)  
        →  ❌ Некоректні дані пацієнта: 
            name не може бути порожнім, отримано: ''; 
            age має бути більшим за 0, отримано: -5; 
            temperature маєбути більшою за 0, отримано: -1.0  │
└────────────────────────────────────────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                 PATIENT.FROM_DICT()                           │
├───────────────────────────────────────────────────────────────────────────────────────────────┤
│  data = {'name': 'Ivan', 'age': 42, 'diagnosis': 'sinusitis'}                                 │
│  ────────────────────────────────────────────────────────────                                 │
│  Patient.from_dict(data)  
        →  Patient(name='Ivan', age=42, diagnosis='sinusitis', temperature=36.6, diagnoses=[])  │
│  ────────────────────────────────────────────────────────────                                 │
│  patient.name        = 'Ivan'                                                                 │
│  patient.age          = 42                                                                    │
│  patient.diagnosis     = 'sinusitis'                                                          │
│  patient.temperature    = 36.6  (взято ЗА ЗАМОВЧУВАННЯМ, бо не було в data)                   │
└───────────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────┐
│             IS_VALID_AGE()           │
├──────────────────────────────────────┤
│  Patient.is_valid_age(17)  →  False  │
│  Patient.is_valid_age(18)  →  True   │
│  Patient.is_valid_age(42)  →  True   │
│  Patient.is_valid_age(-5)  →  False  │
└──────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                    PROPERTY / SETTER                       │
├────────────────────────────────────────────────────────────────────────────────────────────┤
│  Patient('Ivan', 42)  →  ✅ age=42, 
        Patient(name='Ivan', diagnosis='unknown', temperature=36.6, diagnoses=[], _age=42)   │
│  Patient('Test', 0)  →  ❌ ValueError: age має бути більшим за 0, отримано 0              │
│  Patient('Test', -1)  →  ❌ ValueError: age має бути більшим за 0, отримано -1            │
│  Patient('Test', '42')  →  ❌ TypeError: age має бути int, отримано '42' (str)            │
└────────────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
#*Чому НЕ можна просто дописати @property def age(self): ... до звичайного age: int поля — суть проблеми:
@dataclass
class Patient:
    age: int          # ← @dataclass ЗАПАМ'ЯТОВУЄ це як поле "age"

    @property          # ← а ПОТІМ ти ПЕРЕВИЗНАЧАЄШ ім'я "age" як property
    def age(self):        #   Python виконує КЛАС ЗВЕРХУ ВНИЗ, тому ОСТАННЄ
        return self._age    #   присвоєння "age" (ця property) "перекриває" анотацію

Коли @dataclass пізніше дивиться на клас, щоб зрозуміти, "яке значення за замовчуванням у age?" — воно бачить property-об'єкт замість MISSING (тобто "дефолту немає"). 
Це означає, що @dataclass помилково сприйняв би саму property як "значення за замовчуванням" для параметра age — той самий клас проблем, що вже обговорювалась у Task 3 з default_factory (незрозуміла, "заплутана" поведінка, коли клас і property "конфліктують" за одне й те саме ім'я).

#*Як InitVar вирішує проблему — розділяє "параметр конструктора" від "поле, що зберігається":
age: InitVar[int]              # ← "прийми age ПАРАМЕТРОМ у Patient(...),
                                  #    але НЕ створюй з нього автоматичне self.age"

_age: int = field(init=False, default=0)   # ← а ЦЕ — СПРАВЖНЄ поле-сховище

def __post_init__(self, age):    # ← @dataclass передає ТУТ значення age,
    ...                             #   яке прийшло в конструктор
    self.age = age                   # ← а ТУТ ми ЯВНО присвоюємо self.age = age,
                                        #   що ВИКЛИКАЄ property-setter (бо `age` — property!)

InitVar — це "спеціальний сигнал" для @dataclass: "це значення потрібне лише ТИМЧАСОВО, для передачі в __post_init__, не роби з нього звичайний атрибут об'єкта". 
Оскільки InitVar-поле не стає реальним атрибутом об'єкта автоматично, немає конфлікту з @property — вони не борються за те саме "місце" в об'єкті: InitVar — тимчасовий параметр, @property — постійний, обчислюваний доступ до _age.

#*Пояснення самого property/setter механізму — ключова ідея Task 7:
patient.age            # ← ВИКЛИКАЄ getter: return self._age
patient.age = 50         # ← ВИКЛИКАЄ setter: перевіряє 50, потім self._age = 50

Ззовні patient.age виглядає як звичайний атрибут (без дужок виклику), але насправді кожне звернення до нього проходить через функцію. 

#*Це дозволяє захистити _age від прямого, неконтрольованого присвоєння:
patient.age = 0        # 💥 ValueError — не можна ОБІЙТИ перевірку!
patient.age = "42"      # 💥 TypeError  — те саме
patient._age = 0         # ⚠️ ТЕХНІЧНО можна ОБІЙТИ, звернувшись НАПРЯМУ до _age
                            #    (Python не робить атрибути ПРАВДИВО приватними —
                            #    підкреслення "_" це лише КОНВЕНЦІЯ, "не чіпай без потреби")

#*Важливий архітектурний нюанс, вартий уваги — конфлікт із "collect-all" підходом:
def __post_init__(self, age):
    errors = []
    # ... перевірка name, temperature ...
    if errors:
        raise ValueError(...)   # ← якщо name/temperature ОБИДВА невалідні — бачиш ОБИДВІ помилки

    self.age = age    # ← а ЦЕ падає ОКРЕМО, "fail fast", БЕЗ об'єднання з попередніми

На відміну від PatientRecord із Дня 12 (де все збиралось в один ValueError), тут age валідується property-setter'ом окремо — і якщо одночасно невалідні name і age, ти побачиш лише помилку name (з __post_init__), а до перевірки age справа навіть не дійде. Це природний компроміс property-based валідації: вона чудово підходить під принцип Fail Fast (кожне поле перевіряється негайно при кожній зміні, навіть після створення об'єкта — patient.age = -5 теж впаде), але втрачає зручність "побач усі проблеми одразу", яку давав collect-all.
"""

