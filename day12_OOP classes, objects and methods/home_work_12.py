"""
## *Challenge 1 — PatientRecord

Створи повноцінний клас:
class PatientRecord:
    ...

Поля:
id
name
age
diagnosis
temperature

Методи:
is_adult()
is_fever()
summary()
"""

class PatientRecord:
    def __init__(
        self,
        id: int,
        name: str,
        age: int,
        diagnosis: str,
        temperature: float,
    ):
        """Створює повний медичний запис пацієнта з валідацією ВСІХ полів.

        Collect-all підхід (Дні 11): перевіряє КОЖНЕ поле, накопичує
        ВСІ помилки, і піднімає ОДНЕ ValueError з повним переліком.
        """
        errors = []

        if not isinstance(id, int) or isinstance(id, bool) or id <= 0:
            errors.append(f"id має бути додатним цілим числом, отримано {id!r}")

        if not isinstance(name, str) or not name.strip():
            errors.append(f"name не може бути порожнім, отримано {name!r}")

        if not isinstance(age, int) or isinstance(age, bool) or age <= 0:
            errors.append(f"age має бути додатним цілим числом, отримано {age!r}")

        if not isinstance(diagnosis, str) or not diagnosis.strip():
            errors.append(f"diagnosis не може бути порожнім, отримано {diagnosis!r}")

        if not isinstance(temperature, (int, float)) or isinstance(temperature, bool):
            errors.append(f"temperature має бути числом, отримано {temperature!r}")
        elif not (25.0 <= temperature <= 45.0):
            errors.append(f"temperature має бути в діапазоні 25.0-45.0, отримано {temperature}")

        if errors:
            raise ValueError("Некоректні дані запису пацієнта: " + "; ".join(errors))

        self.id = id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.temperature = temperature

    def is_adult(self) -> bool:
        """Перевіряє, чи пацієнту 18 років чи більше."""
        return self.age >= 18

    def is_fever(self) -> bool:
        """Перевіряє, чи температура вказує на лихоманку (>= 37.5 °C)."""
        return self.temperature >= 37.5

    def summary(self) -> str:
        """Формує короткий, читабельний опис запису пацієнта."""
        adult_status = "adult" if self.is_adult() else "minor"
        fever_status = "has fever" if self.is_fever() else "no fever"
        return (
            f"#{self.id} {self.name} ({self.age}, {adult_status}) — "
            f"{self.diagnosis}, {self.temperature}°C ({fever_status})"
        )

    def __repr__(self) -> str:
        return (
            f"PatientRecord(id={self.id}, name={self.name!r}, age={self.age}, "
            f"diagnosis={self.diagnosis!r}, temperature={self.temperature})"
        )


# --- Демонстрація ---
records = [
    PatientRecord(1, "Ivan", 42, "sinusitis", 37.2),
    PatientRecord(2, "Olena", 35, "rhinitis", 38.5),
    PatientRecord(3, "Sofia", 15, "otitis", 36.6),
]

lines = []
for record in records:
    lines.append(repr(record))
    lines.append(f"  is_adult(): {record.is_adult()}")
    lines.append(f"  is_fever(): {record.is_fever()}")
    lines.append(f"  summary(): {record.summary()}")
    lines.append("─" * 60)
lines.pop()   # прибираємо зайвий розділювач наприкінці

# --- Демонстрація валідації ---
try:
    PatientRecord(-1, "", -5, "", 99.0)
except ValueError as e:
    lines.append(f"❌ {e}")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  PATIENTRECORD".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────────────────────────────────────────────────────────┐
│                            PATIENTRECORD                                     │
├────────────────────────────────────────────────────────────────────────┤
│  PatientRecord(id=1, name='Ivan', age=42, diagnosis='sinusitis', temperature=37.2) │
│    is_adult(): True                                                              │
│    is_fever(): False                                                              │
│    summary(): #1 Ivan (42, adult) — sinusitis, 37.2°C (no fever)                    │
│  ────────────────────────────────────────────────────                              │
│  PatientRecord(id=2, name='Olena', age=35, diagnosis='rhinitis', temperature=38.5)     │
│    is_adult(): True                                                                     │
│    is_fever(): True                                                                       │
│    summary(): #2 Olena (35, adult) — rhinitis, 38.5°C (has fever)                            │
│  ────────────────────────────────────────────────────                                        │
│  PatientRecord(id=3, name='Sofia', age=15, diagnosis='otitis', temperature=36.6)                 │
│    is_adult(): False                                                                                │
│    is_fever(): False                                                                                  │
│    summary(): #3 Sofia (15, minor) — otitis, 36.6°C (no fever)                                          │
│  ────────────────────────────────────────────────────                                                    │
│  ❌ Некоректні дані запису пацієнта: id має бути додатним цілим числом, отримано -1; name не може бути порожнім, отримано ''; age має бути додатним цілим числом, отримано -5; diagnosis не може бути порожнім, отримано ''; temperature має бути в діапазоні 25.0-45.0, отримано 99.0 │
└────────────────────────────────────────────────────────────────────────┘
"""

"""
#*Пояснення трьох методів — кожен виконує РІВНО одну роль:
def is_adult(self) -> bool:           # ЛОГІЧНА перевірка ОДНОГО поля (age)
def is_fever(self) -> bool:            # ЛОГІЧНА перевірка ОДНОГО поля (temperature)
def summary(self) -> str:               # КОМБІНУЄ дані з ДЕКІЛЬКОХ полів у текст

Це той самий принцип single responsibility, що вже неодноразово застосовувався (calculate_bmi() vs bmi_category() у дні "функції"): is_adult() і is_fever() — прості, незалежні перевірки, а summary() використовує результати цих методів, а не дублює їхню логіку:

def summary(self) -> str:
    adult_status = "adult" if self.is_adult() else "minor"    # ← ВИКЛИК методу,
    fever_status = "has fever" if self.is_fever() else "no fever"   #   а НЕ повторення `self.age >= 18`
    return f"..."

#*Чому summary() викликає self.is_adult() замість self.age >= 18 напряму:
# ❌ ПОГАНО — дублювання логіки:
def summary(self):
    status = "adult" if self.age >= 18 else "minor"   # ← та сама логіка, що й у is_adult()!

# ✅ ДОБРЕ — перевикористання:
def summary(self):
    status = "adult" if self.is_adult() else "minor"    # ← ОДНЕ джерело істини

Якщо завтра поріг повноліття зміниться (наприклад, на 21 для якоїсь конкретної медичної процедури) — правиш лише is_adult(), і summary() автоматично підхопить зміну, без потреби шукати всі місця, де ця умова могла бути продубльована.

#*Валідація в PatientRecord.__init__ — розширена версія Task 5, тепер для ВСІХ 5 полів:
errors = []
# перевіряємо id, name, age, diagnosis, temperature — КОЖНЕ окремо
if errors:
    raise ValueError(...)   # ОДНЕ повідомлення з УСІМ, що не так

Це прямий розвиток validate_patient() з Дня 11 (Challenge 3), лише тепер логіка валідації живе всередині самого класу — об'єкт сам відповідає за власну коректність, а не покладається на зовнішню функцію-валідатор.

is_fever() — те саме порогове значення (37.5), що вже застосовувалось у classify_temperature():
def is_fever(self) -> bool:
    return self.temperature >= 37.5

Тут навмисно не повний classify_temperature() (з категоріями normal/fever/high_fever) — а проста булева перевірка, точно як просить сигнатура завдання (is_fever() -> bool, а не -> str).
"""

# ==============================================================================
# ==============================================================================
"""
## !Challenge 2 — validation inside class!

Перенеси валідацію з Дня 11 у клас.

Наприклад:
PatientRecord(
    id=1,
    name="Ivan",
    age=42,
    diagnosis="sinusitis",
    temperature=36.8,
)

повинен створювати об'єкт.

А:
PatientRecord(
    id=-1,
    name="",
    age=-5,
    diagnosis="",
    temperature=100,
)
повинен кинути ValueError.

Тут важливо не просто копіювати код Дня 11, а правильно розмістити перевірки всередині object model.
"""

class PatientRecord:
    def __init__(
        self,
        id: int,
        name: str,
        age: int,
        diagnosis: str,
        temperature: float,
    ):
        """Створює запис пацієнта з валідацією ВСІХ полів одразу тут.

        Валідація живе В КЛАСІ (в __init__), а не в окремій функції
        ЗОВНІ, як validate_patient() у Дні 11. Це і є "правильне
        розміщення в object model" — детальніше пояснення нижче коду.
        """
        errors = []

        if not isinstance(id, int) or isinstance(id, bool) or id <= 0:
            errors.append(f"id має бути додатним цілим числом, отримано {id!r}")

        if not isinstance(name, str) or not name.strip():
            errors.append(f"name не може бути порожнім, отримано {name!r}")

        if not isinstance(age, int) or isinstance(age, bool) or age <= 0:
            errors.append(f"age має бути додатним цілим числом, отримано {age!r}")

        if not isinstance(diagnosis, str) or not diagnosis.strip():
            errors.append(f"diagnosis не може бути порожнім, отримано {diagnosis!r}")

        if not isinstance(temperature, (int, float)) or isinstance(temperature, bool):
            errors.append(f"temperature має бути числом, отримано {temperature!r}")
        elif not (25.0 <= temperature <= 45.0):
            errors.append(f"temperature має бути в діапазоні 25.0-45.0, отримано {temperature}")

        if errors:
            raise ValueError("Некоректні дані запису пацієнта: " + "; ".join(errors))

        self.id = id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.temperature = temperature

    def is_adult(self) -> bool:
        return self.age >= 18

    def is_fever(self) -> bool:
        return self.temperature >= 37.5

    def summary(self) -> str:
        adult_status = "adult" if self.is_adult() else "minor"
        fever_status = "has fever" if self.is_fever() else "no fever"
        return (
            f"#{self.id} {self.name} ({self.age}, {adult_status}) — "
            f"{self.diagnosis}, {self.temperature}°C ({fever_status})"
        )

    def __repr__(self) -> str:
        return (
            f"PatientRecord(id={self.id}, name={self.name!r}, age={self.age}, "
            f"diagnosis={self.diagnosis!r}, temperature={self.temperature})"
        )


# --- Демонстрація за умовою завдання ---
lines = []

try:
    valid_record = PatientRecord(
        id=1, name="Ivan", age=42, diagnosis="sinusitis", temperature=36.8,
    )
    lines.append(f"✅ Створено: {valid_record}")
except ValueError as e:
    lines.append(f"❌ {e}")

try:
    invalid_record = PatientRecord(
        id=-1, name="", age=-5, diagnosis="", temperature=100,
    )
    lines.append(f"✅ Створено: {invalid_record}")
except ValueError as e:
    lines.append(f"❌ {e}")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  VALIDATION INSIDE CLASS".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────────────────────────────────────────────────────┐
│                     VALIDATION INSIDE CLASS                              │
├────────────────────────────────────────────────────────────────────┤
│  ✅ Створено: #1 Ivan (42, adult) — sinusitis, 36.8°C (no fever)             │
│  ❌ Некоректні дані запису пацієнта: id має бути додатним цілим числом, отримано -1; name не може бути порожнім, отримано ''; age має бути додатним цілим числом, отримано -5; diagnosis не може бути порожнім, отримано ''; temperature має бути в діапазоні 25.0-45.0, отримано 100 │
└────────────────────────────────────────────────────────────────────┘
"""

"""
#*Чому "правильне розміщення" 
це НЕ просто "скопіювати validate_patient() в __init__", а зміна самої архітектурної ролі валідації:
# ═══ День 11: валідація — ЗОВНІШНЯ функція над dict ═══
def validate_patient(patient: dict) -> None:
    if "id" not in patient:
        raise ValueError(...)
    ...

patient = {"id": 1, "name": "Ivan", ...}   # ← dict МОЖНА створити БЕЗ валідації
validate_patient(patient)                    # ← валідація — ОКРЕМИЙ, ДОБРОВІЛЬНИЙ крок
                                                #   ХТОСЬ МУСИТЬ ЗГАДАТИ її викликати!

# ═══ Challenge 2: валідація — ЧАСТИНА конструктора об'єкта ═══
class PatientRecord:
    def __init__(self, id, name, age, diagnosis, temperature):
        # валідація ТУТ — і ЖОДЕН PatientRecord НЕ МОЖЕ існувати без неї

record = PatientRecord(id=1, name="Ivan", ...)   # ← валідація ВІДБУВАЄТЬСЯ АВТОМАТИЧНО,
                                                    #   не можна "забути" її викликати

#*Ключова відмінність — "необов'язкова перевірка" проти "гарантія цілісності об'єкта":

	День 11 (validate_patient() окремо)	Challenge 2 (валідація в __init__)
Хто відповідає за валідацію	той, ХТО ВИКОРИСТОВУЄ dict (може забути!)	сам ОБ'ЄКТ (неможливо оминути)
Чи можна створити "невалідний" запис	✅ так — dict — це просто dict, ніхто не заважає	❌ ні — PatientRecord або створюється валідним, або НЕ ІСНУЄ взагалі
Де "живе" правило валідності	у ЗОВНІШНЬОМУ коді, ЯКИЙ ПОТРІБНО пам'ятати викликати	ВСЕРЕДИНІ самого типу даних — невід'ємна частина того, ЩО ОЗНАЧАЄ бути PatientRecord

#*Це і є суть "object model" у ООП — інкапсуляція інваріантів:
# ❌ БЕЗ інкапсуляції (Day 11 стиль) — dict НЕ ГАРАНТУЄ нічого:
patient_dict = {"id": -1, "name": "", "age": -5}   # ← ЦІЛКОМ можливо створити!
# Валідність — це "домовленість", яку легко порушити, ЗАБУВШИ виклик validate_patient()

# ✅ З інкапсуляцією (Challenge 2 стиль) — PatientRecord ГАРАНТУЄ:
record = PatientRecord(id=-1, name="", age=-5, ...)   # 💥 ValueError ОДРАЗУ
# "Якщо PatientRecord ІСНУЄ — він ЗАВЖДИ валідний" — це ІНВАРІАНТ,
# гарантований самим ТИПОМ, а не дисципліною програміста

#*Практична цінність цієї гарантії — довіра до типу без повторної перевірки:
# Будь-яка функція, що ОТРИМУЄ PatientRecord, МОЖЕ довіряти йому "наосліп":
def print_summary(record: PatientRecord) -> None:
    print(record.summary())   # НЕ ТРЕБА перевіряти record.age > 0 —
                                 # якщо record ІСНУЄ, він ВЖЕ гарантовано валідний!

# Порівняй з dict-версією Дня 11 — там ЩОРАЗУ доводилось би
# запитувати "а чи вже викликали validate_patient() для цього dict?"
"""

# ==============================================================================
# ==============================================================================
"""
## !Challenge 3 — methods that use state!

Додай:
def update_temperature(self, temperature: float) -> None:
    ...

та:
def change_diagnosis(self, diagnosis: str) -> None:
    ...

Після цього:
patient.update_temperature(38.4)
patient.change_diagnosis("acute sinusitis")

об'єкт повинен змінити власний стан.
"""

class PatientRecord:
    def __init__(
        self,
        id: int,
        name: str,
        age: int,
        diagnosis: str,
        temperature: float,
    ):
        errors = []
        errors += self._check_id(id)
        errors += self._check_name(name)
        errors += self._check_age(age)
        errors += self._check_diagnosis(diagnosis)
        errors += self._check_temperature(temperature)

        if errors:
            raise ValueError("Некоректні дані запису пацієнта: " + "; ".join(errors))

        self.id = id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.temperature = temperature

    # --- Приватні перевірки ОДНОГО поля кожна — ВИКОРИСТОВУЮТЬСЯ і в __init__,
    #     і в update_*()/change_*() методах, щоб НЕ дублювати правила ---

    @staticmethod
    def _check_id(id) -> list[str]:
        if not isinstance(id, int) or isinstance(id, bool) or id <= 0:
            return [f"id має бути додатним цілим числом, отримано {id!r}"]
        return []

    @staticmethod
    def _check_name(name) -> list[str]:
        if not isinstance(name, str) or not name.strip():
            return [f"name не може бути порожнім, отримано {name!r}"]
        return []

    @staticmethod
    def _check_age(age) -> list[str]:
        if not isinstance(age, int) or isinstance(age, bool) or age <= 0:
            return [f"age має бути додатним цілим числом, отримано {age!r}"]
        return []

    @staticmethod
    def _check_diagnosis(diagnosis) -> list[str]:
        if not isinstance(diagnosis, str) or not diagnosis.strip():
            return [f"diagnosis не може бути порожнім, отримано {diagnosis!r}"]
        return []

    @staticmethod
    def _check_temperature(temperature) -> list[str]:
        if not isinstance(temperature, (int, float)) or isinstance(temperature, bool):
            return [f"temperature має бути числом, отримано {temperature!r}"]
        if not (25.0 <= temperature <= 45.0):
            return [f"temperature має бути в діапазоні 25.0-45.0, отримано {temperature}"]
        return []

    # --- Методи, що ЗМІНЮЮТЬ стан об'єкта (state mutation) ---

    def update_temperature(self, temperature: float) -> None:
        """Оновлює температуру, використовуючи ТУ САМУ перевірку, що й __init__."""
        errors = self._check_temperature(temperature)
        if errors:
            raise ValueError("Не вдалося оновити temperature: " + "; ".join(errors))
        self.temperature = temperature

    def change_diagnosis(self, diagnosis: str) -> None:
        """Оновлює діагноз, використовуючи ТУ САМУ перевірку, що й __init__."""
        errors = self._check_diagnosis(diagnosis)
        if errors:
            raise ValueError("Не вдалося змінити diagnosis: " + "; ".join(errors))
        self.diagnosis = diagnosis

    # --- Методи, що ЛИШЕ ЧИТАЮТЬ стан ---

    def is_adult(self) -> bool:
        return self.age >= 18

    def is_fever(self) -> bool:
        return self.temperature >= 37.5

    def summary(self) -> str:
        adult_status = "adult" if self.is_adult() else "minor"
        fever_status = "has fever" if self.is_fever() else "no fever"
        return (
            f"#{self.id} {self.name} ({self.age}, {adult_status}) — "
            f"{self.diagnosis}, {self.temperature}°C ({fever_status})"
        )

    def __repr__(self) -> str:
        return (
            f"PatientRecord(id={self.id}, name={self.name!r}, age={self.age}, "
            f"diagnosis={self.diagnosis!r}, temperature={self.temperature})"
        )


# --- Демонстрація ---
patient = PatientRecord(id=1, name="Ivan", age=42, diagnosis="sinusitis", temperature=36.8)

lines = [f"До зміни:  {patient.summary()}"]

patient.update_temperature(38.4)
patient.change_diagnosis("acute sinusitis")

lines.append(f"Після зміни: {patient.summary()}")
lines.append("─" * 60)

try:
    patient.update_temperature(100)
except ValueError as e:
    lines.append(f"❌ {e}")

try:
    patient.change_diagnosis("")
except ValueError as e:
    lines.append(f"❌ {e}")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  METHODS THAT USE STATE".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")
"""
До змін:
#1 Ivan (42, adult) — sinusitis, 36.8°C (no fever)

Після змін:
#1 Ivan (42, adult) — acute sinusitis, 38.4°C (has fever)

Спроба некоректного оновлення:
❌ ValueError: temperature має бути в діапазоні 25.0-45.0, отримано 99.0
❌ ValueError: diagnosis не може бути порожнім, отримано ''
"""

"""
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                                     METHODS THAT USE STATE                                   │
├──────────────────────────────────────────────────────────────────────────────────────────────┤
│  До зміни:  #1 Ivan (42, adult) — sinusitis, 36.8°C (no fever)                               │
│  Після зміни: #1 Ivan (42, adult) — acute sinusitis, 38.4°C (has fever)                      │
│  ────────────────────────────────────────────────────────────                                │
│  ❌ Не вдалося оновити temperature: temperature має бути в діапазоні 25.0-45.0, отримано 100 │
│  ❌ Не вдалося змінити diagnosis: diagnosis не може бути порожнім, отримано ''               │
└──────────────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
Оскільки треба уникнути дублювання правил валідації між __init__ і новими методами, тут природно виникає потреба винести перевірку кожного поля в окремі приватні методи — це саме той рефакторинг, від якого ти відмовився в Challenge 2, але тепер він стає необхідним, а не просто "стилістичним вибором".

#*Чому це "методи, що використовують стан" — ключова ідея завдання:
def update_temperature(self, temperature: float) -> None:
    ...
    self.temperature = temperature   # ← ЗМІНЮЄ self, а не ПОВЕРТАЄ нове значення

Це принципово інша категорія методів порівняно з is_adult(), summary() (лише читають self). Тут метод мутує об'єкт: той самий patient, викликаний до і після update_temperature(), матиме різний patient.temperature. Це різниться від того, що вже застосовувалось раніше, де об'єкти або створювались одразу з готовими значеннями (__init__), або лише читались — тепер об'єкт живе довше і змінюється протягом свого "життя".

#*Чому _check_temperature() як окремий метод, а не повторення коду:
# ❌ Дублювання (без окремого _check_temperature):
def __init__(self, ..., temperature, ...):
    if not (25.0 <= temperature <= 45.0):
        errors.append(f"temperature має бути...")   # ← правило ТУТ

def update_temperature(self, temperature):
    if not (25.0 <= temperature <= 45.0):             # ← ТЕ САМЕ правило СКОПІЙОВАНО
        raise ValueError(f"temperature має бути...")    #    сюди — DRY порушено!

# ✅ Без дублювання (з _check_temperature):
@staticmethod
def _check_temperature(temperature):
    if not (25.0 <= temperature <= 45.0):
        return [f"temperature має бути..."]

def __init__(self, ..., temperature, ...):
    errors += self._check_temperature(temperature)   # ← ВИКЛИК

def update_temperature(self, temperature):
    errors = self._check_temperature(temperature)      # ← ТОЙ САМИЙ виклик

Якщо завтра діапазон "нормальної" температури зміниться (наприклад, з 25.0-45.0 на щось інше) — правиш лише _check_temperature(), і автоматично й __init__, і update_temperature() використовують нове правило.

#*Чому @staticmethod для _check_* методів:
@staticmethod
def _check_temperature(temperature) -> list[str]:
    ...

Ці методи не потребують self — вони перевіряють передане значення, а не стан конкретного об'єкта (не звертаються до self.щось). @staticmethod явно каже: "ця функція логічно належить класу, але не залежить від конкретного екземпляра" — можна викликати навіть PatientRecord._check_temperature(38.4) без створення жодного об'єкта.

#*Різниця з update_temperature() (звичайний метод, self потрібен):
def update_temperature(self, temperature):   # ← self ТУТ ПОТРІБЕН
    ...
    self.temperature = temperature             #   бо він ЗМІНЮЄ КОНКРЕТНИЙ об'єкт

update_temperature() не може бути @staticmethod, бо вона обов'язково повинна знати, у якому саме об'єкті змінювати temperature.
"""

# ==============================================================================
# ==============================================================================
"""
## !Challenge 4 — statistics without dictionaries!

На Дні 9–11 у тебе були:
list[dict]

Тепер використовуй:
list[PatientRecord]

Створи функції:
def average_age(patients: list[PatientRecord]) -> float:
    ...


def oldest_patient(
    patients: list[PatientRecord],
) -> PatientRecord:
    ...

Порівняй концептуально:
list[dict]
і:
list[PatientRecord]
"""

class PatientRecord:
    def __init__(self, id: int, name: str, age: int, diagnosis: str, temperature: float):
        errors = []
        errors += self._check_id(id)
        errors += self._check_name(name)
        errors += self._check_age(age)
        errors += self._check_diagnosis(diagnosis)
        errors += self._check_temperature(temperature)

        if errors:
            raise ValueError("Некоректні дані запису пацієнта: " + "; ".join(errors))

        self.id = id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.temperature = temperature

    @staticmethod
    def _check_id(id) -> list[str]:
        if not isinstance(id, int) or isinstance(id, bool) or id <= 0:
            return [f"id має бути додатним цілим числом, отримано {id!r}"]
        return []

    @staticmethod
    def _check_name(name) -> list[str]:
        if not isinstance(name, str) or not name.strip():
            return [f"name не може бути порожнім, отримано {name!r}"]
        return []

    @staticmethod
    def _check_age(age) -> list[str]:
        if not isinstance(age, int) or isinstance(age, bool) or age <= 0:
            return [f"age має бути додатним цілим числом, отримано {age!r}"]
        return []

    @staticmethod
    def _check_diagnosis(diagnosis) -> list[str]:
        if not isinstance(diagnosis, str) or not diagnosis.strip():
            return [f"diagnosis не може бути порожнім, отримано {diagnosis!r}"]
        return []

    @staticmethod
    def _check_temperature(temperature) -> list[str]:
        if not isinstance(temperature, (int, float)) or isinstance(temperature, bool):
            return [f"temperature має бути числом, отримано {temperature!r}"]
        if not (25.0 <= temperature <= 45.0):
            return [f"temperature має бути в діапазоні 25.0-45.0, отримано {temperature}"]
        return []

    def is_adult(self) -> bool:
        return self.age >= 18

    def is_fever(self) -> bool:
        return self.temperature >= 37.5

    def summary(self) -> str:
        adult_status = "adult" if self.is_adult() else "minor"
        fever_status = "has fever" if self.is_fever() else "no fever"
        return (
            f"#{self.id} {self.name} ({self.age}, {adult_status}) — "
            f"{self.diagnosis}, {self.temperature}°C ({fever_status})"
        )

    def __repr__(self) -> str:
        return (
            f"PatientRecord(id={self.id}, name={self.name!r}, age={self.age}, "
            f"diagnosis={self.diagnosis!r}, temperature={self.temperature})"
        )


class PatientStatistics:
    """Утиліта для статистики над list[PatientRecord].

    @staticmethod тут доречний з ТІЄЇ САМОЇ причини, що й у _check_*
    методах PatientRecord: жодна з цих функцій не звертається до
    "власного" стану (немає СВОГО self.щось) — вони лише ОБРОБЛЯЮТЬ
    переданий список пацієнтів. Група в клас — суто ОРГАНІЗАЦІЙНА
    (тематичне групування), а не потреба у стані екземпляра.
    """

    @staticmethod
    def average_age(patients: list[PatientRecord]) -> float:
        """Обчислює середній вік серед списку PatientRecord."""
        return sum(p.age for p in patients) / len(patients)

    @staticmethod
    def oldest_patient(patients: list[PatientRecord]) -> PatientRecord:
        """Знаходить найстаршого пацієнта серед списку PatientRecord."""
        return max(patients, key=lambda p: p.age)


# --- Демонстрація з 5 пацієнтами ---
patients = [
    PatientRecord(1, "Ivan", 42, "sinusitis", 37.2),
    PatientRecord(2, "Olena", 35, "rhinitis", 36.7),
    PatientRecord(3, "Petro", 61, "sinusitis", 38.5),
    PatientRecord(4, "Sofia", 15, "otitis", 36.9),
    PatientRecord(5, "Mykola", 8, "pharyngitis", 37.0),
]

avg_age = PatientStatistics.average_age(patients)
oldest = PatientStatistics.oldest_patient(patients)

# --- Вивід у рамці ---
lines = ["Пацієнти:"]
lines += [f"  {p!r}" for p in patients]
lines.append("─" * 60)
lines.append(f"PatientStatistics.average_age(patients)   = {avg_age:.1f}")
lines.append(f"PatientStatistics.oldest_patient(patients) = {oldest.name} ({oldest.age})")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  STATISTICS OVER list[PatientRecord]".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                            STATISTICS OVER list[PatientRecord]                           │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│  Пацієнти:                                                                               │
│    PatientRecord(id=1, name='Ivan', age=42, diagnosis='sinusitis', temperature=37.2)     │
│    PatientRecord(id=2, name='Olena', age=35, diagnosis='rhinitis', temperature=36.7)     │
│    PatientRecord(id=3, name='Petro', age=61, diagnosis='sinusitis', temperature=38.5)    │
│    PatientRecord(id=4, name='Sofia', age=15, diagnosis='otitis', temperature=36.9)       │
│    PatientRecord(id=5, name='Mykola', age=8, diagnosis='pharyngitis', temperature=37.0)  │
│  ────────────────────────────────────────────────────────────                            │
│  PatientStatistics.average_age(patients)   = 32.2                                        │
│  PatientStatistics.oldest_patient(patients) = Petro (61)                                 │
└──────────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
#*Це той самий принцип, що й _check_id(), _check_name() у PatientRecord (Challenge 3): 
функція не залежить від якогось "власного" стану конкретного об'єкта PatientStatistics — вона просто обробляє те, що їй передали. 
@staticmethod тут — це організаційний прийом (згрупувати пов'язані функції під одним "дахом" — іменем класу), а НЕ технічна необхідність (на відміну від update_temperature() із Challenge 3, де self обов'язковий, бо метод змінює конкретний об'єкт).

#*Концептуальне порівняння: list[dict] vs list[PatientRecord]
Доступ до даних — [] проти .:
# list[dict] (Дні 9-11):
patient["age"]           # ← доступ через РЯДКОВИЙ ключ — Python НЕ ПЕРЕВІРЯЄ,
                            #    чи "age" взагалі МАЄ ІСНУВАТИ

# list[PatientRecord] (тепер):
patient.age                # ← доступ через АТРИБУТ — існує ТІЛЬКИ якщо
                              #    __init__ ГАРАНТУВАВ його наявність

#*Захист від помилок — коли Python "ловить" проблему:
# list[dict] — помилка з'являється ТІЛЬКИ ПІД ЧАС ВИКОНАННЯ, у НЕПЕРЕДБАЧЕНОМУ місці:
patient["ge"]   # ← ДРУКАРСЬКА ПОМИЛКА в ключі ("ge" замість "age")
# 💥 KeyError, і ТІЛЬКИ ТОДІ, коли цей рядок РЕАЛЬНО виконається

# list[PatientRecord] — помилка ловиться РАНІШЕ, часто ще ДО запуску:
patient.ge      # ← та сама ДРУКАРСЬКА ПОМИЛКА
# Сучасна IDE (PyCharm, VS Code + Pylance) ПІДКРЕСЛИТЬ ЦЕ ЧЕРВОНИМ ще ПІД ЧАС НАБОРУ коду,
# бо ЗНАЄ, що клас PatientRecord НЕ МАЄ атрибута "ge"

#*Гарантія валідності — "порожня коробка" проти "завжди повний контейнер":
# list[dict]:
{"id": -1, "name": "", "age": -5}   # ← можна СТВОРИТИ такий dict — dict "не заперечує"

# list[PatientRecord]:
PatientRecord(id=-1, name="", age=-5, diagnosis="", temperature=100)
# 💥 ValueError ОДРАЗУ при СТВОРЕННІ — НЕМОЖЛИВО отримати "поганий" PatientRecord

#*Поведінка "прикріплена" до даних — методи проти окремих функцій:
# list[dict] — логіка ЗАВЖДИ ОКРЕМО від даних:
def is_adult(patient: dict) -> bool:
    return patient["age"] >= 18

is_adult(patient)             # ← треба ПАМ'ЯТАТИ, ЯКУ функцію застосувати ДО ЯКОГО dict

# list[PatientRecord] — логіка "живе" РАЗОМ із даними:
patient.is_adult()              # ← об'єкт "знає, ЯК" відповісти на запитання ПРО СЕБЕ,
                                    #   не треба ШУКАТИ окрему функцію

#*Підсумкова таблиця:
	                    list[dict]	                    list[PatientRecord]
Доступ до поля	        patient["age"]	                patient.age

Помилка в назві поля	KeyError 	                    помилка типізації, 
                        під час виконання               часто ще в IDE

Гарантія валідності	    ❌ ніяка — 	                  ✅ гарантована 
                        будь-який dict "проходить"      через __init__

Логіка 	                окремі функції, 	            методи, "прикріплені"
(перевірки, обчислення) ЗАВЖДИ передавати               до об'єкта
                        dict як аргумент

Легко 	                ✅ так — можна 	              ❌ ні — атрибути 
"зіпсувати" структуру   ДОДАТИ/ВИДАЛИТИ                 class фіксовані 
                        ключ будь-де                    в __init__

Швидкість написання 	швидше для 	                    трохи більше "церемоній" 
прототипу               одноразового скрипту            на старті

#*Головний висновок: 
list[dict] — гнучкий, швидкий для прототипування, але не гарантує нічого про свій вміст. 
list[PatientRecord] — потребує трохи більше коду наперед (клас, __init__, валідація), але натомість гарантує: якщо об'єкт PatientRecord існує, він завжди валідний, і його поведінка (методи) завжди доступна поруч із даними — саме тому реальні, довготривалі проєкти (як MedAssistant) з часом природно еволюціонують від dict до повноцінних класів.
"""

# ==============================================================================
# ==============================================================================
"""
## !🔥 Challenge 5 — MedAssistant OOP!

Це головне завдання дня.

Перероби частину твого MedAssistant із:
list[dict]
на:
list[Patient]

Архітектура:
JSON
 ↓
load
 ↓
Patient objects
 ↓
validation
 ↓
methods
 ↓
statistics
 ↓
report

Наприклад:
patients = [
    Patient(
        name="Ivan",
        age=42,
        diagnosis="sinusitis",
        temperature=37.2,
    ),
    ...
]

Потім:
for patient in patients:
    if patient.is_fever():
        ...

Тобто логіка починає читатися природною мовою:

patient.is_adult()
patient.is_fever()
patient.calculate_bmi()
patient.summary()
"""

#data/patients.json
"""
[
  {
    "id": 1,
    "name": "Ivan",
    "age": 42,
    "diagnosis": "sinusitis",
    "temperature": 37.2,
    "weight": 82,
    "height": 1.80
  },
  {
    "id": 2,
    "name": "Olena",
    "age": 35,
    "diagnosis": "rhinitis",
    "temperature": 36.7,
    "weight": 58,
    "height": 1.65
  },
  {
    "id": 3,
    "name": "Petro",
    "age": 61,
    "diagnosis": "sinusitis",
    "temperature": 38.5,
    "weight": 95,
    "height": 1.72
  }
]
"""

#patient.py — клас «Patient», у якому вага та зріст тепер є частиною його стану:
"""patient.py

The Patient object model for MedAssistant: state, validation, and
self-contained behavior (is_adult, is_fever, calculate_bmi, summary).
"""


class Patient:
    def __init__(
        self,
        id: int,
        name: str,
        age: int,
        diagnosis: str,
        temperature: float,
        weight: float,
        height: float,
    ):
        """Create a validated patient. Raises ValueError if anything is wrong.

        Collect-all validation: every field is checked, and ALL
        problems are reported together in a single ValueError.
        """
        errors = []
        errors += self._check_id(id)
        errors += self._check_name(name)
        errors += self._check_age(age)
        errors += self._check_diagnosis(diagnosis)
        errors += self._check_temperature(temperature)
        errors += self._check_weight(weight)
        errors += self._check_height(height)

        if errors:
            raise ValueError("Invalid patient data: " + "; ".join(errors))

        self.id = id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.temperature = temperature
        self.weight = weight
        self.height = height

    @staticmethod
    def _check_id(id) -> list[str]:
        if not isinstance(id, int) or isinstance(id, bool) or id <= 0:
            return [f"'id' must be a positive integer, got {id!r}"]
        return []

    @staticmethod
    def _check_name(name) -> list[str]:
        if not isinstance(name, str) or not name.strip():
            return [f"'name' cannot be empty, got {name!r}"]
        return []

    @staticmethod
    def _check_age(age) -> list[str]:
        if not isinstance(age, int) or isinstance(age, bool) or age <= 0:
            return [f"'age' must be a positive integer, got {age!r}"]
        return []

    @staticmethod
    def _check_diagnosis(diagnosis) -> list[str]:
        if not isinstance(diagnosis, str) or not diagnosis.strip():
            return [f"'diagnosis' cannot be empty, got {diagnosis!r}"]
        return []

    @staticmethod
    def _check_temperature(temperature) -> list[str]:
        if not isinstance(temperature, (int, float)) or isinstance(temperature, bool):
            return [f"'temperature' must be a number, got {temperature!r}"]
        if not (25.0 <= temperature <= 45.0):
            return [f"'temperature' must be in range 25.0-45.0, got {temperature}"]
        return []

    @staticmethod
    def _check_weight(weight) -> list[str]:
        if not isinstance(weight, (int, float)) or isinstance(weight, bool) or weight <= 0:
            return [f"'weight' must be a positive number, got {weight!r}"]
        return []

    @staticmethod
    def _check_height(height) -> list[str]:
        if not isinstance(height, (int, float)) or isinstance(height, bool) or height <= 0:
            return [f"'height' must be a positive number, got {height!r}"]
        return []

    def is_adult(self) -> bool:
        """Check whether this patient is 18 or older."""
        return self.age >= 18

    def is_fever(self) -> bool:
        """Check whether this patient's temperature indicates a fever."""
        return self.temperature >= 37.5

    def calculate_bmi(self) -> float:
        """Calculate this patient's BMI from its own weight/height.

        No arguments needed anymore — weight and height are now
        part of the patient's own state.
        """
        return self.weight / (self.height ** 2)

    def summary(self) -> str:
        """Build a short, human-readable summary of this patient."""
        adult_status = "adult" if self.is_adult() else "minor"
        fever_status = "has fever" if self.is_fever() else "no fever"
        bmi = self.calculate_bmi()
        return (
            f"#{self.id} {self.name} ({self.age}, {adult_status}) — "
            f"{self.diagnosis}, {self.temperature}°C ({fever_status}), BMI {bmi:.1f}"
        )

    @classmethod
    def from_dict(cls, data: dict) -> "Patient":
        """Build a Patient from a plain dict (e.g. one JSON record).

        This is the ONLY place that knows how to translate raw JSON
        keys into Patient's constructor — keeps that translation out
        of the loading code entirely.
        """
        return cls(
            id=data["id"],
            name=data["name"],
            age=data["age"],
            diagnosis=data["diagnosis"],
            temperature=data["temperature"],
            weight=data["weight"],
            height=data["height"],
        )

    def __repr__(self) -> str:
        return (
            f"Patient(id={self.id}, name={self.name!r}, age={self.age}, "
            f"diagnosis={self.diagnosis!r}, temperature={self.temperature}, "
            f"weight={self.weight}, height={self.height})"
        )

#statistics_utils.py — тепер працює з об’єктами типу «Пацієнт», а не зі словниками:
"""statistics_utils.py

Aggregate statistics over a list of Patient objects, for MedAssistant.
"""

from patient import Patient


def average_age(patients: list[Patient]) -> float:
    """Compute the average age across all patients."""
    return sum(p.age for p in patients) / len(patients)


def average_temperature(patients: list[Patient]) -> float:
    """Compute the average temperature across all patients."""
    return sum(p.temperature for p in patients) / len(patients)


def oldest_patient(patients: list[Patient]) -> Patient:
    """Find the oldest patient in the list."""
    return max(patients, key=lambda p: p.age)


def fever_patients(patients: list[Patient]) -> list[Patient]:
    """Return patients whose is_fever() is True.

    Reads like natural language, as the challenge asked:
        [p for p in patients if p.is_fever()]
    """
    return [p for p in patients if p.is_fever()]

#report_utils.py — формує та зберігає звіт на основі об’єктів класу «Пацієнт»:
"""report_utils.py

Report generation and saving for MedAssistant.
"""

from patient import Patient


def generate_report(
    patients: list[Patient],
    avg_age: float,
    avg_temp: float,
    oldest: Patient,
    fevers: list[Patient],
) -> str:
    """Build a human-readable text report from Patient objects."""
    title = "MEDASSISTANT PATIENT REPORT"

    lines = [
        f"{title}",
        "=" * len(title),
        "",
        f"Total patients: {len(patients)}",
        f"Average age: {avg_age:.1f}",
        f"Average temperature: {avg_temp:.1f}",
        f"Oldest patient: {oldest.name} ({oldest.age})",
        "",
        "Patients with fever:",
    ]
    lines += [f"  - {p.summary()}" for p in fevers] if fevers else ["  (none)"]

    return "\n".join(lines) + "\n"


def save_report(path: str, report: str) -> None:
    """Save a text report to disk."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(report)

#main.py — координація: JSON → об’єкти «Пацієнт» → методи → статистика → звіт:
"""main.py

MedAssistant pipeline, now built on Patient objects instead of
list[dict]:

    JSON -> load -> Patient objects -> validation -> methods ->
    statistics -> report
"""

import json

from patient import Patient
from statistics_utils import average_age, average_temperature, oldest_patient, fever_patients
from report_utils import generate_report, save_report


def load_patients(path: str) -> list[Patient]:
    """Load raw JSON and turn each record into a validated Patient.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
        ValueError: If any record fails Patient's own validation.
    """
    with open(path, "r", encoding="utf-8") as file:
        raw_records = json.load(file)

    return [Patient.from_dict(record) for record in raw_records]


def main() -> None:
    print("MEDASSISTANT")
    print("============\n")

    try:
        print("Loading patients...")
        patients = load_patients("data/patients.json")
        print(f"✓ {len(patients)} Patient object(s) loaded\n")

        # --- logic now reads like natural language ---
        print("Checking patients...")
        for patient in patients:
            if patient.is_fever():
                print(f"  ⚠ {patient.name} has a fever ({patient.temperature}°C)")
            if not patient.is_adult():
                print(f"  ℹ {patient.name} is a minor ({patient.age})")
        print()

        print("Calculating statistics...")
        avg_age = average_age(patients)
        avg_temp = average_temperature(patients)
        oldest = oldest_patient(patients)
        fevers = fever_patients(patients)
        print("✓ Statistics calculated\n")

        print("Generating report...")
        report = generate_report(patients, avg_age, avg_temp, oldest, fevers)
        save_report("data/report.txt", report)
        print("✓ Report generated")

    except FileNotFoundError as e:
        print(f"✗ File not found:\n  {e}")
    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON:\n  {e}")
    except ValueError as e:
        print(f"✗ Validation failed:\n  {e}")


if __name__ == "__main__":
    main()

"""
MEDASSISTANT
============

Loading patients...
✓ 3 Patient object(s) loaded

Checking patients...
  ⚠ Petro has a fever (38.5°C)

Calculating statistics...
✓ Statistics calculated

Generating report...
✓ Report generated
"""
"""
#data/report.txt
MEDASSISTANT PATIENT REPORT
===========================

Total patients: 3
Average age: 46.0
Average temperature: 37.5
Oldest patient: Petro (61)

Patients with fever:
  - #3 Petro (61, adult) — sinusitis, 38.5°C (has fever), BMI 32.1
"""
"""
#*Чому на схемі конвеєра тепер з’явився етап, якого не було при використанні list[dict]:
JSON → load → Patient objects → validation → methods → statistics → report
                    ↑                ↑            ↑
              from_dict()      built into    is_fever(),
              per record       __init__      is_adult(), etc.

У випадку з list[dict] «перевірка» була окремою функцією, про виклик якої потрібно було пам’ятати (validate_patients(patients)). 
У випадку з list[Patient] перевірка невіддільна від створення — щойно завершується виконання load_patients(), кожен об’єкт у повернутому списку вже гарантовано є дійсним. Більше немає послідовності «завантажити, а потім, можливо, перевірити» — тепер це «завантажити, і перевірка відбувається як побічний ефект створення».

#*Чому цикл у main() тепер виглядає так, як описано в завданні:
for patient in patients:
    if patient.is_fever():
        print(f"  ⚠ {patient.name} has a fever ({patient.temperature}°C)")

#*Порівняйте це з аналогом для 9/11, для якого знадобилися вільна функція та пошук у словнику:
# list[dict] version:
for patient in patients:
    if classify_temperature(patient["temperature"]) != "normal":
        ...

function patient.is_fever() сприймається як запитання, яке ви ставите пацієнту, а не як обчислення, яке ви виконуєте над словником. Саме на цю зміну вказує це завдання: тепер об’єкт сам володіє логікою, що стосується його.

#*Чому функція from_dict() розміщена безпосередньо в класі Patient, а не в файлі main.py чи в функції завантаження:
@classmethod
def from_dict(cls, data: dict) -> "Patient":
    return cls(id=data["id"], name=data["name"], ...)

Таким чином інформація про те, «як перетворити необроблений запис JSON на об’єкт Patient», зберігається виключно в одному місці — у класі, який знає сигнатуру власного конструктора. Якщо в методі Patient.__init__ з’явиться нове обов’язкове поле, оновлювати потрібно буде лише функцію from_dict(), а функцію load_patients() у файлі main.py змінювати не доведеться.
"""

# ==============================================================================
# ==============================================================================

# ==============================================================================
# ==============================================================================


# ==============================================================================
# ==============================================================================
