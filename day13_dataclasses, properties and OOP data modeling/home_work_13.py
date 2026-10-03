"""
## !Challenge 1 — MedicalRecord!

Створи:
@dataclass
class MedicalRecord:
    id: int
    patient_name: str
    diagnosis: str
    temperature: float

Додай:
__post_init__()
summary()
is_fever()
from_dict()
"""

from dataclasses import dataclass

# Константи — щоб не "розкидати" магічні числа по коду (DRY)
FEVER_THRESHOLD = 37.5
MIN_TEMPERATURE = 25.0
MAX_TEMPERATURE = 45.0


@dataclass
class MedicalRecord:
    id: int
    patient_name: str
    diagnosis: str
    temperature: float

    def __post_init__(self) -> None:
        """Collect-all валідація: перевіряє ВСІ поля, піднімає ОДНЕ ValueError."""
        errors = []

        if not isinstance(self.id, int) or isinstance(self.id, bool) or self.id <= 0:
            errors.append(f"id має бути додатним цілим числом, отримано {self.id!r}")

        if not isinstance(self.patient_name, str) or not self.patient_name.strip():
            errors.append(f"patient_name не може бути порожнім, отримано {self.patient_name!r}")

        if not isinstance(self.diagnosis, str) or not self.diagnosis.strip():
            errors.append(f"diagnosis не може бути порожнім, отримано {self.diagnosis!r}")

        if not isinstance(self.temperature, (int, float)) or isinstance(self.temperature, bool):
            errors.append(f"temperature має бути числом, отримано {self.temperature!r}")
        elif not (MIN_TEMPERATURE <= self.temperature <= MAX_TEMPERATURE):
            errors.append(
                f"temperature має бути в діапазоні {MIN_TEMPERATURE}-{MAX_TEMPERATURE}, "
                f"отримано {self.temperature}"
            )

        if errors:
            raise ValueError("Некоректний медичний запис: " + "; ".join(errors))

    def is_fever(self) -> bool:
        """True, якщо температура >= 37.5 °C."""
        return self.temperature >= FEVER_THRESHOLD

    def summary(self) -> str:
        """Короткий опис запису (повертає рядок, не друкує)."""
        status = "лихоманка" if self.is_fever() else "без лихоманки"
        return f"#{self.id} {self.patient_name}: {self.diagnosis}, {self.temperature}°C ({status})"

    @classmethod
    def from_dict(cls, data: dict) -> "MedicalRecord":
        """Створює запис зі словника. Відсутній ключ -> KeyError (Fail Fast)."""
        return cls(
            id=data["id"],
            patient_name=data["patient_name"],
            diagnosis=data["diagnosis"],
            temperature=data["temperature"],
        )


# --- Демонстрація ---
lines = []

record = MedicalRecord(1, "Ivan", "sinusitis", 36.8)
lines.append(f"summary():  {record.summary()}")
lines.append(f"is_fever(): {record.is_fever()}")
lines.append("─" * 62)

fever_record = MedicalRecord(2, "Olena", "rhinitis", 38.4)
lines.append(f"summary():  {fever_record.summary()}")
lines.append(f"is_fever(): {fever_record.is_fever()}")
lines.append("─" * 62)

data = {"id": 3, "patient_name": "Petro", "diagnosis": "otitis", "temperature": 37.5}
border_record = MedicalRecord.from_dict(data)
lines.append(f"from_dict(): {border_record}")
lines.append(f"is_fever() на межі 37.5: {border_record.is_fever()}")
lines.append("─" * 62)

try:
    MedicalRecord(-1, "", "", 100)
except ValueError as e:
    lines.append("❌ ValueError (усі помилки одразу):")
    for part in str(e).split(": ", 1)[1].split("; "):
        lines.append(f"   - {part}")
lines.append("─" * 62)

try:
    MedicalRecord.from_dict({"id": 4, "patient_name": "Hanna"})
except KeyError as e:
    lines.append(f"❌ KeyError: у словнику немає ключа {e}")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  MEDICALRECORD".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                          MEDICALRECORD                                         │
├────────────────────────────────────────────────────────────────────────────────────────────────┤
│  summary():  #1 Ivan: sinusitis, 36.8°C (без лихоманки)                                        │
│  is_fever(): False                                                                             │
│  ──────────────────────────────────────────────────────────────                                │
│  summary():  #2 Olena: rhinitis, 38.4°C (лихоманка)                                            │
│  is_fever(): True                                                                              │
│  ──────────────────────────────────────────────────────────────                                │
│  from_dict(): MedicalRecord(id=3, patient_name='Petro', diagnosis='otitis', temperature=37.5)  │
│  is_fever() на межі 37.5: True                                                                 │
│  ──────────────────────────────────────────────────────────────                                │
│  ❌ ValueError (усі помилки одразу):                                                           │
│     - id має бути додатним цілим числом, отримано -1                                           │
│     - patient_name не може бути порожнім, отримано ''                                          │
│     - diagnosis не може бути порожнім, отримано ''                                             │
│     - temperature має бути в діапазоні 25.0-45.0, отримано 100                                 │
│  ──────────────────────────────────────────────────────────────                                │
│  ❌ KeyError: у словнику немає ключа 'diagnosis'                                               │
└────────────────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
**Пояснення по кожному елементу**

*__post_init__() — перевірка після автоматичного __init__:

@dataclass сам генерує __init__, тому власну перевірку вставляють у __post_init__. 
Його викликають одразу після присвоєння всіх полів. 
Зверни увагу: @dataclass не перевіряє типи з анотацій (id: int — це лише підказка). 
Тому в коді є явні isinstance(), інакше MedicalRecord("abc", 5, None, "hot") створився б без помилок.

*isinstance(self.id, bool) виключає True/False. 
У Python bool є підкласом int, і без цього id=True вважався б коректним id=1.

*Collect-all: 
усі помилки збираються в список errors, і ValueError піднімається один раз наприкінці. 
У демо для MedicalRecord(-1, "", "", 100) видно всі чотири проблеми за один запуск. 
Це той самий підхід, що й у validate_patient() з Дня 11.

*is_fever() і summary() — один метод, одна відповідальність (SRP):
def summary(self) -> str:
    status = "лихоманка" if self.is_fever() else "без лихоманки"   # ← викликає is_fever(), не повторює порівняння

Поріг 37.5 записаний в одному місці (FEVER_THRESHOLD), а summary() бере результат із is_fever(). Якщо поріг зміниться, правити треба один рядок (DRY). 
summary() повертає рядок, а не друкує його. Що робити з цим рядком (print, файл, звіт), вирішує код, який викликає метод. Це розділення відповідальностей, як у greet() з Практики №1 про функції.

*from_dict() — data["key"], а не .get():

У Task 5 Patient.from_dict() використовував .get(..., дефолт), бо в Patient були поля зі значеннями за замовчуванням. У MedicalRecord усі чотири поля обов'язкові: запис без id чи diagnosis не має сенсу. Тому відсутній ключ дає KeyError одразу (Fail Fast), а не тихий None, який зламався б пізніше в іншому місці.

Якщо ключі є, але значення некоректні, from_dict() теж не пропустить їх: він викликає конструктор, а той запускає __post_init__. Окремо перевіряти дані в from_dict() не потрібно (DRY).
"""

# ==============================================================================
# ==============================================================================
"""
## !Challenge 2 — immutable configuration!

Створи:
@dataclass(frozen=True)
class ModelConfig:
    model_name: str
    image_size: int
    threshold: float

Наприклад:
config = ModelConfig(
    model_name="ResNet50",
    image_size=224,
    threshold=0.5,
)

Перевір, що:
config.threshold = 0.7
не дозволяється.
"""

from dataclasses import (
    FrozenInstanceError,
    dataclass,
    replace,
)


@dataclass(frozen=True)
class ModelConfig:
    model_name: str
    image_size: int
    threshold: float

    def __post_init__(self) -> None:
        """Collect-all валідація. У frozen-класі тут можна лише ПЕРЕВІРЯТИ поля."""
        errors = []

        if not isinstance(self.model_name, str) or not self.model_name.strip():
            errors.append(f"model_name не може бути порожнім, отримано {self.model_name!r}")

        if (
            not isinstance(self.image_size, int)
            or isinstance(self.image_size, bool)
            or self.image_size <= 0
        ):
            errors.append(f"image_size має бути додатним цілим числом, отримано {self.image_size!r}")

        if not isinstance(self.threshold, (int, float)) or isinstance(self.threshold, bool):
            errors.append(f"threshold має бути числом, отримано {self.threshold!r}")
        elif not (0.0 <= self.threshold <= 1.0):
            errors.append(f"threshold має бути в діапазоні 0.0-1.0, отримано {self.threshold}")

        if errors:
            raise ValueError("Некоректна конфігурація: " + "; ".join(errors))


# Для контрасту: ЗВИЧАЙНИЙ (не frozen) dataclass
@dataclass
class MutableConfig:
    model_name: str
    threshold: float


# --- Демонстрація ---
lines = []

# 1. Створення
config = ModelConfig(model_name="ResNet50", image_size=224, threshold=0.5)
lines.append(f"config = {config}")
lines.append("─" * 66)

# 2. Спроба змінити поле напряму
try:
    config.threshold = 0.7
    lines.append("config.threshold = 0.7  →  ✅ змінилось (НЕ мало б!)")
except FrozenInstanceError as e:
    lines.append("config.threshold = 0.7  →  ❌ FrozenInstanceError:")
    lines.append(f"   {e}")
lines.append(f"config.threshold далі = {config.threshold}")
lines.append("─" * 66)

# 3. "Змінити" через replace() — створюється НОВИЙ об'єкт
new_config = replace(config, threshold=0.7)
lines.append("new_config = replace(config, threshold=0.7)")
lines.append(f"   new_config.threshold = {new_config.threshold}")
lines.append(f"   config.threshold     = {config.threshold}  (оригінал не змінився)")
lines.append(f"   new_config is config: {new_config is config}")

try:
    replace(config, threshold=5)
except ValueError as e:
    lines.append(f"replace(config, threshold=5) → ❌ {str(e).split(': ', 1)[1]}")
lines.append("─" * 66)

# 4. Hashable: можна використати як ключ dict / елемент set
config_a = ModelConfig("ResNet50", 224, 0.5)
config_b = ModelConfig("ResNet50", 224, 0.5)   # ті самі значення
config_c = ModelConfig("ResNet50", 224, 0.7)

experiments = {config_a: "експеримент №1"}
lines.append(f"experiments[config_b] = {experiments[config_b]!r}  (config_b == config_a)")
lines.append(f"hash(config_a) == hash(config_b): {hash(config_a) == hash(config_b)}")
lines.append(f"len({{config_a, config_b, config_c}}) = {len({config_a, config_b, config_c})}")

try:
    hash(MutableConfig("ResNet50", 0.5))
except TypeError as e:
    lines.append(f"hash(звичайний dataclass) → ❌ TypeError: {e}")
lines.append("─" * 66)

# 5. Некоректна конфігурація
try:
    ModelConfig("", 0, 1.5)
except ValueError as e:
    lines.append("ModelConfig('', 0, 1.5) → ❌ ValueError:")
    for part in str(e).split(": ", 1)[1].split("; "):
        lines.append(f"   - {part}")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  FROZEN DATACLASS: MODELCONFIG".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌───────────────────────────────────────────────────────────────────────────────────────┐
│                              FROZEN DATACLASS: MODELCONFIG                            │
├───────────────────────────────────────────────────────────────────────────────────────┤
│  config = ModelConfig(model_name='ResNet50', image_size=224, threshold=0.5)           │
│  ──────────────────────────────────────────────────────────────────                   │
│  config.threshold = 0.7  →  ❌ FrozenInstanceError:                                   │
│     cannot assign to field 'threshold'                                                │
│  config.threshold далі = 0.5                                                          │
│  ──────────────────────────────────────────────────────────────────                   │
│  new_config = replace(config, threshold=0.7)                                          │
│     new_config.threshold = 0.7                                                        │
│     config.threshold     = 0.5  (оригінал не змінився)                                │
│     new_config is config: False                                                       │
│  replace(config, threshold=5) → ❌ threshold має бути в діапазоні 0.0-1.0, отримано 5 │
│  ──────────────────────────────────────────────────────────────────                   │
│  experiments[config_b] = 'експеримент №1'  (config_b == config_a)                     │
│  hash(config_a) == hash(config_b): True                                               │
│  len({config_a, config_b, config_c}) = 2                                              │
│  hash(звичайний dataclass) → ❌ TypeError: unhashable type: 'MutableConfig'           │
│  ──────────────────────────────────────────────────────────────────                   │
│  ModelConfig('', 0, 1.5) → ❌ ValueError:                                             │
│     - model_name не може бути порожнім, отримано ''                                   │
│     - image_size має бути додатним цілим числом, отримано 0                           │
│     - threshold має бути в діапазоні 0.0-1.0, отримано 1.5                            │
└───────────────────────────────────────────────────────────────────────────────────────┘
"""

"""
**Пояснення**

*frozen=True — заборона змінювати поля після створення:
config.threshold = 0.7   # 💥 FrozenInstanceError: cannot assign to field 'threshold'

@dataclass(frozen=True) генерує __setattr__, який завжди кидає помилку. 
Присвоїти поле не вдасться ні ззовні, ні з методів класу. 
Тому пряме config.threshold = 0.7 не проходить, а config.threshold далі лишається 0.5. 
Для конфігурації моделі це корисно: threshold, image_size та інші параметри не зміняться посеред експерименту, і результати можна буде відтворити.

*__post_init__ у frozen-класі лише перевіряє:
Присвоєння self.щось = ... там теж заборонене, бо об'єкт уже "заморожений". 
Валідація ж тільки читає поля, тож працює як і раніше. 
Це Fail Fast: некоректна конфігурація не створюється взагалі.

*replace() замість зміни на місці:
new_config = replace(config, threshold=0.7)

Змінити незмінний об'єкт неможливо, тому створюють новий з одним іншим полем. 
Оригінал не змінюється (config.threshold лишається 0.5). 
replace() викликає конструктор, тому __post_init__ запускається знову: replace(config, threshold=5) дає ValueError. Некоректну конфігурацію не отримати навіть таким способом.

*Hashable: чому frozen-об'єкт можна класти в dict і set:

Для frozen=True (разом із eq=True, яке за замовчуванням увімкнене) @dataclass генерує __hash__ за значеннями полів.
Тому config_a і config_b з однаковими полями мають однаковий хеш. 
experiments[config_b] знаходить запис, збережений під config_a, а у set три об'єкти зливаються у два.
Звичайний dataclass має __eq__, але його __hash__ вимкнено (unhashable type). 
Причина в тому, що змінюваний об'єкт не можна робити ключем: після зміни поля його хеш став би іншим, і dict більше не знайшов би запис.

*Обмеження, про яке варто знати:
frozen забороняє перепризначати поля. Він не захищає вміст змінюваних об'єктів усередині. 
Якби ModelConfig мав поле-list, то config.classes.append(...) спрацювало б, а hash(config) кидав би TypeError. 
Тому в frozen-конфігурації краще тримати незмінні типи (str, int, float, tuple).
"""

# ==============================================================================
# ==============================================================================
"""
## !Challenge 3 — Factory from JSON!

Створи:
@classmethod
def from_dict(cls, data: dict) -> "MedicalRecord":
    ...

Потім:
JSON
 ↓
dict
 ↓
MedicalRecord.from_dict()
 ↓
object

Створи список:
records: list[MedicalRecord]
з JSON-подібних словників.
"""

"""
data/records.json (6 записів: 3 коректні, 3 навмисно зіпсовані):

json
[
  {"id": 1, "patient_name": "Ivan", "diagnosis": "sinusitis", "temperature": 37.2},
  {"id": 2, "patient_name": "Olena", "diagnosis": "rhinitis", "temperature": 38.4},
  {"id": 3, "patient_name": "Petro", "temperature": 36.6},
  {"id": -4, "patient_name": "", "diagnosis": "otitis", "temperature": "hot"},
  "not a record",
  {"id": 6, "patient_name": "Sofia", "diagnosis": "pharyngitis", "temperature": 39.2}
]
"""

import json
from dataclasses import dataclass

FEVER_THRESHOLD = 37.5
MIN_TEMPERATURE = 25.0
MAX_TEMPERATURE = 45.0


@dataclass
class MedicalRecord:
    id: int
    patient_name: str
    diagnosis: str
    temperature: float

    def __post_init__(self) -> None:
        """Collect-all валідація: усі помилки збираються в одне ValueError."""
        errors = []

        if not isinstance(self.id, int) or isinstance(self.id, bool) or self.id <= 0:
            errors.append(f"id має бути додатним цілим числом, отримано {self.id!r}")

        if not isinstance(self.patient_name, str) or not self.patient_name.strip():
            errors.append(f"patient_name не може бути порожнім, отримано {self.patient_name!r}")

        if not isinstance(self.diagnosis, str) or not self.diagnosis.strip():
            errors.append(f"diagnosis не може бути порожнім, отримано {self.diagnosis!r}")

        if not isinstance(self.temperature, (int, float)) or isinstance(self.temperature, bool):
            errors.append(f"temperature має бути числом, отримано {self.temperature!r}")
        elif not (MIN_TEMPERATURE <= self.temperature <= MAX_TEMPERATURE):
            errors.append(
                f"temperature має бути в діапазоні {MIN_TEMPERATURE}-{MAX_TEMPERATURE}, "
                f"отримано {self.temperature}"
            )

        if errors:
            raise ValueError("; ".join(errors))

    def is_fever(self) -> bool:
        return self.temperature >= FEVER_THRESHOLD

    def summary(self) -> str:
        status = "лихоманка" if self.is_fever() else "без лихоманки"
        return f"#{self.id} {self.patient_name}: {self.diagnosis}, {self.temperature}°C ({status})"

    @classmethod
    def from_dict(cls, data: dict) -> "MedicalRecord":
        """Фабрика: словник -> MedicalRecord. Валідація відбувається в __post_init__."""
        if not isinstance(data, dict):
            raise ValueError(f"запис має бути dict, отримано {type(data).__name__}")

        return cls(
            id=data["id"],                        # відсутній ключ -> KeyError
            patient_name=data["patient_name"],
            diagnosis=data["diagnosis"],
            temperature=data["temperature"],
        )


def read_json(path: str) -> list[dict]:
    """JSON-файл -> Python-структура. Лише читання файлу (SRP)."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def build_records(
    raw_records: list[dict],
) -> tuple[list[MedicalRecord], list[tuple[int, str]]]:
    """list[dict] -> (валідні MedicalRecord, пропущені записи з причинами).

    Некоректний запис не зупиняє обробку решти.
    """
    records = []
    skipped = []

    for index, data in enumerate(raw_records):
        try:
            records.append(MedicalRecord.from_dict(data))
        except KeyError as e:
            skipped.append((index, f"відсутній ключ {e}"))
        except ValueError as e:
            skipped.append((index, str(e)))

    return records, skipped


def main() -> None:
    # JSON-файл -> list[dict] -> MedicalRecord.from_dict() -> list[MedicalRecord]
    try:
        raw_records = read_json("data/records.json")
    except FileNotFoundError:
        print("✗ Файл data/records.json не знайдено")
        return
    except json.JSONDecodeError as e:
        print(f"✗ data/records.json містить некоректний JSON: {e}")
        return

    records: list[MedicalRecord]
    skipped: list[tuple[int, str]]
    records, skipped = build_records(raw_records)

    lines = [
        f"Записів у файлі:       {len(raw_records)}",
        f"Створено MedicalRecord: {len(records)}",
        f"Пропущено:              {len(skipped)}",
        "─" * 64,
        "records:",
    ]
    lines += [f"  {record.summary()}" for record in records]
    lines.append("─" * 64)
    lines.append("Пропущені записи:")
    for index, reason in skipped:
        lines.append(f"  запис #{index}:")
        for part in reason.split("; "):
            lines.append(f"     - {part}")

    width = max(len(line) for line in lines) + 4

    print("\n┌" + "─" * width + "┐")
    print("│" + "  FACTORY FROM JSON".center(width) + "│")
    print("├" + "─" * width + "┤")
    for line in lines:
        print("│  " + line.ljust(width - 2) + "│")
    print("└" + "─" * width + "┘")


if __name__ == "__main__":
    main()

"""
┌────────────────────────────────────────────────────────────────────┐
│                          FACTORY FROM JSON                         │
├────────────────────────────────────────────────────────────────────┤
│  Записів у файлі:       6                                          │
│  Створено MedicalRecord: 3                                         │
│  Пропущено:              3                                         │
│  ────────────────────────────────────────────────────────────────  │
│  records:                                                          │
│    #1 Ivan: sinusitis, 37.2°C (без лихоманки)                      │
│    #2 Olena: rhinitis, 38.4°C (лихоманка)                          │
│    #6 Sofia: pharyngitis, 39.2°C (лихоманка)                       │
│  ────────────────────────────────────────────────────────────────  │
│  Пропущені записи:                                                 │
│    запис #2:                                                       │
│       - відсутній ключ 'diagnosis'                                 │
│    запис #3:                                                       │
│       - id має бути додатним цілим числом, отримано -4             │
│       - patient_name не може бути порожнім, отримано ''            │
│       - temperature має бути числом, отримано 'hot'                │
│    запис #4:                                                       │
│       - запис має бути dict, отримано str                          │
└────────────────────────────────────────────────────────────────────┘
"""

"""
#*Помилки самого файлу теж не валять програму*:
✗ Файл data/records.json не знайдено
✗ data/records.json містить некоректний JSON: Expecting property name enclosed in double quotes: line 2 column 1 (char 11)

Запускай скрипт із папки, де лежить data/: шлях "data/records.json" відраховується від поточної робочої директорії.

#*Пояснення
Pipeline і хто за що відповідає (SRP):

JSON-файл ──read_json()──▶ list[dict] ──from_dict()──▶ MedicalRecord ──build_records()──▶ list[MedicalRecord]
Крок	            Хто робить	                Що знає
файл → list[dict]	read_json()	                лише про читання файлу
dict → об'єкт	    MedicalRecord.from_dict()	як ключі словника відповідають полям класу
весь список 	    build_records()	            що робити з поганим записом
→ об'єкти + пропущені
порядок кроків 	    main()	                    нічого про внутрішню логіку
і вивід

Кожну частину можна змінити окремо. 
Наприклад, якщо дані підуть з API замість файлу, зміниться лише read_json().

#*Чому from_dict() не перевіряє значення сам (DRY):
Він лише читає ключі й передає їх у конструктор (cls(...)). 
Усі перевірки живуть в одному місці, __post_init__. 
Тому створити некоректний запис не вдасться жодним способом: ні через MedicalRecord(...), ні через from_dict(). 
Єдина перевірка в самому from_dict() стосується межі: чи прийшов взагалі dict, а не рядок "not a record".

#*Fail Fast для одного запису, але не для всього списку:
Кожен окремий MedicalRecord або створюється коректним, або не створюється (ValueError).
build_records() ловить цю помилку для кожного запису окремо, записує причину в skipped і йде до наступного.
Це та сама ідея skip-invalid з Дня 11, тільки тепер перевірку робить сам клас, а не окрема функція над dict.

#*Ловимо конкретні винятки, а не except Exception:
except KeyError і except ValueError описують саме ті проблеми, які очікуємо від поганих даних. 
Якби тут стояв except Exception, то справжня помилка в коді (наприклад, друкарська помилка в імені атрибута) теж потрапила б у "пропущені записи", і знайти її було б набагато важче.

#*Що змінилось порівняно з Challenge 1:
З повідомлення ValueError прибрано префікс "Некоректний медичний запис: ". 
Тепер str(e) містить лише причини, і їх легко розбити на рядки через split("; ").
У from_dict() додано перевірку isinstance(data, dict).

#*Обмеження, яке видно у виводі:
Для запису #2 показано лише один відсутній ключ, бо from_dict() читає ключі по черзі, і перший KeyError зупиняє читання. 
Якби бракувало одразу diagnosis і temperature, ти побачив би тільки diagnosis. 
Якщо захочеш побачити всі відсутні ключі одразу, from_dict() можна доповнити перевіркою всіх ключів наперед. Для цієї вправи це зайве (YAGNI).
"""

# ==============================================================================
# ==============================================================================
"""
## !Challenge 4 — properties for BMI!

Створи:
@dataclass
class Patient:
    name: str
    weight: float
    height: float

та:

@property
def bmi(self) -> float:
    ...

Тоді:
patient.bmi
повинен автоматично повертати BMI.

Тут вже побачиш різницю:
patient.calculate_bmi()

проти:
patient.bmi
"""

from dataclasses import dataclass


@dataclass
class Patient:
    name: str
    weight: float   # кг
    height: float   # метри

    def __post_init__(self) -> None:
        """Fail Fast: некоректні weight/height не дають створити об'єкт."""
        errors = []

        if not isinstance(self.weight, (int, float)) or isinstance(self.weight, bool) or self.weight <= 0:
            errors.append(f"weight має бути додатним числом, отримано {self.weight!r}")

        if not isinstance(self.height, (int, float)) or isinstance(self.height, bool) or self.height <= 0:
            errors.append(f"height має бути додатним числом, отримано {self.height!r}")

        if errors:
            raise ValueError("; ".join(errors))

    @property
    def bmi(self) -> float:
        """BMI = weight / height². Рахується щоразу з ПОТОЧНИХ weight/height."""
        return self.weight / (self.height ** 2)

    def calculate_bmi(self) -> float:
        """Старий стиль (метод). Тонка обгортка: формула живе лише в bmi (DRY)."""
        return self.bmi


def main() -> None:
    lines = []

    patient = Patient("Ivan", 82, 1.80)

    # 1. Метод проти property
    lines.append("1. Метод проти property:")
    lines.append(f"   patient.calculate_bmi()  = {patient.calculate_bmi():.1f}   (дужки обов'язкові)")
    lines.append(f"   patient.bmi              = {patient.bmi:.1f}   (без дужок, як атрибут)")
    lines.append(f"   callable(patient.calculate_bmi) = {callable(patient.calculate_bmi)}   (це метод, його ще треба викликати)")
    lines.append(f"   type(patient.bmi).__name__      = {type(patient.bmi).__name__}   (одразу готове число)")
    lines.append("─" * 70)

    # 2. Автоматичне оновлення
    lines.append("2. bmi автоматично оновлюється:")
    lines.append(f"   weight = {patient.weight}  ->  bmi = {patient.bmi:.1f}")
    patient.weight = 95
    lines.append(f"   weight = {patient.weight}  ->  bmi = {patient.bmi:.1f}   (ми НЕ викликали ніякого оновлення)")
    lines.append("─" * 70)

    # 3. Property без setter
    lines.append("3. Property без setter:")
    try:
        patient.bmi = 30
        lines.append("   patient.bmi = 30  ->  змінилось (НЕ мало б!)")
    except AttributeError as e:
        lines.append("   patient.bmi = 30  ->  AttributeError:")
        lines.append(f"      {e}")
    lines.append("─" * 70)

    # 4. Property не є полем dataclass
    lines.append("4. bmi не входить у repr/==, бо це не поле:")
    lines.append(f"   repr(patient) = {patient!r}")
    lines.append("─" * 70)

    # 5. Валідація при створенні
    lines.append("5. Валідація при створенні:")
    try:
        Patient("Test", -5, 0)
    except ValueError as e:
        lines.append("   Patient('Test', -5, 0)  ->  ValueError:")
        for part in str(e).split("; "):
            lines.append(f"      - {part}")
    lines.append("─" * 70)

    # 6. Обмеження: після створення перевірки немає
    lines.append("6. Обмеження: __post_init__ працює лише при створенні:")
    patient.height = 0
    try:
        patient.bmi
    except ZeroDivisionError as e:
        lines.append("   patient.height = 0  (дозволено!), далі patient.bmi  ->  ZeroDivisionError:")
        lines.append(f"      {e}")

    width = max(len(line) for line in lines) + 4

    print("\n┌" + "─" * width + "┐")
    print("│" + "  PROPERTY BMI".center(width) + "│")
    print("├" + "─" * width + "┤")
    for line in lines:
        print("│  " + line.ljust(width - 2) + "│")
    print("└" + "─" * width + "┘")


if __name__ == "__main__":
    main()

"""
┌───────────────────────────────────────────────────────────────────────────────────┐
│                                     PROPERTY BMI                                  │
├───────────────────────────────────────────────────────────────────────────────────┤
│  1. Метод проти property:                                                         │
│     patient.calculate_bmi()  = 25.3   (дужки обов'язкові)                         │
│     patient.bmi              = 25.3   (без дужок, як атрибут)                     │
│     callable(patient.calculate_bmi) = True   (це метод, його ще треба викликати)  │
│     type(patient.bmi).__name__      = float   (одразу готове число)               │
│  ──────────────────────────────────────────────────────────────────────           │
│  2. bmi автоматично оновлюється:                                                  │
│     weight = 82  ->  bmi = 25.3                                                   │
│     weight = 95  ->  bmi = 29.3   (ми НЕ викликали ніякого оновлення)             │
│  ──────────────────────────────────────────────────────────────────────           │
│  3. Property без setter:                                                          │
│     patient.bmi = 30  ->  AttributeError:                                         │
│        property 'bmi' of 'Patient' object has no setter                           │
│  ──────────────────────────────────────────────────────────────────────           │
│  4. bmi не входить у repr/==, бо це не поле:                                      │
│     repr(patient) = Patient(name='Ivan', weight=95, height=1.8)                   │
│  ──────────────────────────────────────────────────────────────────────           │
│  5. Валідація при створенні:                                                      │
│     Patient('Test', -5, 0)  ->  ValueError:                                       │
│        - weight має бути додатним числом, отримано -5                             │
│        - height має бути додатним числом, отримано 0                              │
│  ──────────────────────────────────────────────────────────────────────           │
│  6. Обмеження: __post_init__ працює лише при створенні:                           │
│     patient.height = 0  (дозволено!), далі patient.bmi  ->  ZeroDivisionError:    │
│        division by zero                                                           │
└───────────────────────────────────────────────────────────────────────────────────┘
"""

"""
*Текст помилки в блоці 3 залежить від версії Python. 
У нових версіях (я запускав на 3.12) це property 'bmi' of 'Patient' object has no setter, у старіших (до 3.11) було can't set attribute. Тест перевіряє лише тип помилки, тому від версії не залежить.

*Пояснення
patient.bmi проти patient.calculate_bmi():

Метод треба викликати з дужками, це дія: «порахуй».
Property читається як атрибут, це властивість: «який у пацієнта BMI».
Блок 1 це показує: callable(...) для методу дає True (його ще потрібно викликати), а patient.bmi одразу число.
BMI тут обчислюється з даних, а не вводиться окремо, тому логічно, що це властивість.

*BMI не зберігається, а рахується щоразу заново:
У блоці 2 ми змінили weight з 82 на 95, і bmi одразу став 29.3. Ніякого «оновлення» не було, тому розсинхронізація неможлива. Якби BMI був звичайним полем, після зміни ваги він показував би старе значення.

*Property без setter захищає від присвоєння:
patient.bmi = 30 дає AttributeError. Значення, яке виводиться з інших полів, не можна встановити вручну, бо воно б суперечило weight і height.

*Чому calculate_bmi() лишився як обгортка:
Формула живе в одному місці (bmi), старий метод просто повертає self.bmi. 
Код, який вже викликає calculate_bmi(), не зламається (Open/Closed), а формулу не продубльовано (DRY).

*Property не є полем dataclass:
Блок 4 показує, що bmi немає в repr. З тієї ж причини його не буде в asdict() і в порівнянні ==. Якщо BMI потрібен, наприклад, у JSON, його треба додати вручну.

*Обмеження, яке є в блоці 6:
__post_init__ перевіряє дані лише при створенні. 
Далі patient.height = 0 проходить без помилки, а patient.bmi падає з ZeroDivisionError. 
Це не помилка в коді, а межа підходу, тому один із тестів її документує. Є два шляхи:

frozen=True з replace(), як у ModelConfig (Challenge 2);
@property-сеттери для weight і height, як age у Task 7.

Для цього завдання це зайве (YAGNI), але в MedAssistant, де пацієнтів будуть оновлювати, питання виникне.
"""

# ==============================================================================
# ==============================================================================
"""
## !🔥 Challenge 5 — MedAssistant OOP v2!
Перероби твій День 12 PatientRecord у @dataclass.
Має бути:
JSON
 ↓
PatientRecord.from_dict()
 ↓
validation
 ↓
list[PatientRecord]
 ↓
statistics
 ↓
report

Клас:
@dataclassclass PatientRecord:    
id: int    
name: str    
age: int    
diagnosis: str    
temperature: float

Обов'язково реалізуй:
__post_init__()
from_dict()
is_adult()
is_fever()
summary()
"""

##Variant#1
"""
data/patients.json
[
  {"id": 1, "name": "Ivan", "age": 42, "diagnosis": "sinusitis", "temperature": 37.2},
  {"id": 2, "name": "Olena", "age": 35, "diagnosis": "rhinitis", "temperature": 38.4},
  {"id": 3, "name": "Petro", "age": 61, "diagnosis": "sinusitis", "temperature": 38.9},
  {"id": 4, "name": "Sofia", "age": 15, "diagnosis": "otitis", "temperature": 36.6},
  {"id": 5, "name": "Hanna", "age": 29, "temperature": 36.9},
  {"id": -6, "name": "", "age": "61", "diagnosis": "otitis", "temperature": 99},
  "not a record"
]
"""

#patient_record.py
"""patient_record.py

Модель PatientRecord (dataclass) та побудова списку записів із сирих даних JSON.
"""

import json
from dataclasses import dataclass, fields

# Пороги в одному місці (DRY): змінюємо тут, і всі методи отримують нове значення
ADULT_AGE = 18
FEVER_THRESHOLD = 37.5
MIN_TEMPERATURE = 25.0
MAX_TEMPERATURE = 45.0


def _is_positive_int(value: object) -> bool:
    """int > 0. bool виключаємо: у Python True == 1."""
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _is_non_empty_str(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _is_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


@dataclass
class PatientRecord:
    id: int
    name: str
    age: int
    diagnosis: str
    temperature: float

    def __post_init__(self) -> None:
        """Перевіряє ВСІ поля й піднімає ОДНЕ ValueError з усіма проблемами.

        @dataclass не перевіряє типи з анотацій, тому перевірки пишемо самі.
        Невалідний запис створити неможливо: Fail Fast.
        """
        errors = []

        if not _is_positive_int(self.id):
            errors.append(f"id має бути додатним цілим числом, отримано {self.id!r}")
        if not _is_non_empty_str(self.name):
            errors.append(f"name не може бути порожнім, отримано {self.name!r}")
        if not _is_positive_int(self.age):
            errors.append(f"age має бути додатним цілим числом, отримано {self.age!r}")
        if not _is_non_empty_str(self.diagnosis):
            errors.append(f"diagnosis не може бути порожнім, отримано {self.diagnosis!r}")

        if not _is_number(self.temperature):
            errors.append(f"temperature має бути числом, отримано {self.temperature!r}")
        elif not (MIN_TEMPERATURE <= self.temperature <= MAX_TEMPERATURE):
            errors.append(
                f"temperature має бути в діапазоні {MIN_TEMPERATURE}-{MAX_TEMPERATURE}, "
                f"отримано {self.temperature}"
            )

        if errors:
            raise ValueError("; ".join(errors))

    def is_adult(self) -> bool:
        return self.age >= ADULT_AGE

    def is_fever(self) -> bool:
        return self.temperature >= FEVER_THRESHOLD

    def summary(self) -> str:
        """Короткий опис запису. Повертає рядок, друкує той, хто викликає."""
        age_status = "дорослий" if self.is_adult() else "неповнолітній"
        fever_status = "лихоманка" if self.is_fever() else "без лихоманки"
        return (
            f"#{self.id} {self.name} ({self.age}, {age_status}) — "
            f"{self.diagnosis}, {self.temperature}°C ({fever_status})"
        )

    @classmethod
    def from_dict(cls, data: dict) -> "PatientRecord":
        """dict -> PatientRecord. На будь-які погані дані піднімає ЛИШЕ ValueError.

        Імена полів беремо з самого dataclass (fields), а не пишемо вдруге:
        додали поле в клас, і воно автоматично стало обов'язковим тут (DRY).
        """
        if not isinstance(data, dict):
            raise ValueError(f"запис має бути словником (dict), отримано {type(data).__name__}")

        names = [f.name for f in fields(cls)]
        missing = [name for name in names if name not in data]
        if missing:
            raise ValueError("відсутні поля: " + ", ".join(missing))

        return cls(**{name: data[name] for name in names})   # значення перевірить __post_init__


@dataclass(frozen=True)
class SkippedRecord:
    """Запис, який не вдалося перетворити на PatientRecord, і причина."""
    number: int     # позиція в JSON-списку, рахуючи з 1
    reason: str


def build_records(raw_records: list) -> tuple[list[PatientRecord], list[SkippedRecord]]:
    """Сирі записи -> (валідні PatientRecord, пропущені з причинами).

    Один поганий запис не зупиняє решту.
    """
    records = []
    skipped = []

    for number, raw in enumerate(raw_records, start=1):
        try:
            records.append(PatientRecord.from_dict(raw))
        except ValueError as e:
            skipped.append(SkippedRecord(number, str(e)))

    return records, skipped


def read_json(path: str) -> object:
    """Лише читає JSON-файл. Помилки файлу не ловимо, їх обробляє main()."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_records(path: str) -> tuple[list[PatientRecord], list[SkippedRecord]]:
    """JSON-файл -> (валідні записи, пропущені записи)."""
    raw = read_json(path)
    if not isinstance(raw, list):
        raise ValueError(f"очікувався JSON-список записів, отримано {type(raw).__name__}")
    return build_records(raw)

#statistics_utils.py
"""statistics_utils.py

Чиста статистика над list[PatientRecord]: без файлів і без print().
"""

from dataclasses import dataclass

from patient_record import PatientRecord


@dataclass(frozen=True)
class Statistics:
    """Готовий набір результатів: його приймає report_utils."""
    total: int
    adults: int
    average_age: float
    average_temperature: float
    oldest: PatientRecord
    fever: tuple[PatientRecord, ...]


def _require_records(records: list[PatientRecord]) -> None:
    """Спільна перевірка (DRY): статистика порожнього списку не має сенсу."""
    if not records:
        raise ValueError("немає записів для статистики")


def average_age(records: list[PatientRecord]) -> float:
    _require_records(records)
    return sum(r.age for r in records) / len(records)


def average_temperature(records: list[PatientRecord]) -> float:
    _require_records(records)
    return sum(r.temperature for r in records) / len(records)


def oldest_patient(records: list[PatientRecord]) -> PatientRecord:
    _require_records(records)
    return max(records, key=lambda r: r.age)


def count_adults(records: list[PatientRecord]) -> int:
    return sum(1 for r in records if r.is_adult())


def fever_records(records: list[PatientRecord]) -> list[PatientRecord]:
    return [r for r in records if r.is_fever()]


def calculate_statistics(records: list[PatientRecord]) -> Statistics:
    """Складає окремі функції в один результат (Composition)."""
    return Statistics(
        total=len(records),
        adults=count_adults(records),
        average_age=average_age(records),
        average_temperature=average_temperature(records),
        oldest=oldest_patient(records),
        fever=tuple(fever_records(records)),
    )

#report_utils.py
"""report_utils.py

Формування й збереження звіту. Приймає готові дані, нічого не рахує сам.
"""

from patient_record import SkippedRecord
from statistics_utils import Statistics


def build_report(stats: Statistics, skipped: list[SkippedRecord]) -> str:
    """Повертає текст звіту (без файлів і print())."""
    title = "ЗВІТ MEDASSISTANT"

    lines = [
        title,
        "=" * len(title),
        "",
        f"Записів у файлі:  {stats.total + len(skipped)}",
        f"Валідних:         {stats.total}",
        f"Пропущено:        {len(skipped)}",
        "",
        "Статистика (лише валідні записи):",
        f"  Середній вік:         {stats.average_age:.1f}",
        f"  Середня температура:  {stats.average_temperature:.1f}",
        f"  Найстарший пацієнт:   {stats.oldest.name} ({stats.oldest.age})",
        f"  Дорослих:             {stats.adults} з {stats.total}",
        "",
        "Пацієнти з лихоманкою:",
    ]
    lines += [f"  - {r.summary()}" for r in stats.fever] or ["  (немає)"]

    lines += ["", "Пропущені записи:"]
    lines += [f"  - запис №{s.number}: {s.reason}" for s in skipped] or ["  (немає)"]

    return "\n".join(lines) + "\n"


def save_report(path: str, text: str) -> None:
    """Зберігає звіт. Помилки запису (OSError) обробляє main()."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)

#main.py
"""main.py

Лише послідовність кроків:
JSON -> PatientRecord.from_dict() -> валідація -> list[PatientRecord] -> статистика -> звіт
"""

import json
import sys

from patient_record import load_records
from report_utils import build_report, save_report
from statistics_utils import calculate_statistics


def main(data_path: str = "data/patients.json", report_path: str = "data/report.txt") -> int:
    """Повертає 0 при успіху і 1 при помилці. Програма не падає з traceback."""
    print("MEDASSISTANT")
    print("============\n")

    # --- Завантаження: кожен запис перевіряє сам PatientRecord ---
    print("Завантаження записів...")
    try:
        records, skipped = load_records(data_path)
    except FileNotFoundError:                       # має стояти ПЕРЕД OSError (його підклас)
        print(f"✗ Файл не знайдено:\n  {data_path}")
        return 1
    except OSError as e:
        print(f"✗ Не вдалося прочитати файл:\n  {e}")
        return 1
    except json.JSONDecodeError as e:               # має стояти ПЕРЕД ValueError (його підклас)
        print(f"✗ Некоректний JSON:\n  {e}")
        return 1
    except ValueError as e:
        print(f"✗ Некоректна структура файлу:\n  {e}")
        return 1

    print(f"✓ Валідних записів: {len(records)}, пропущено: {len(skipped)}")
    for item in skipped:
        print(f"  ⚠ запис №{item.number}: {item.reason}")
    if not records:
        print("✗ Немає жодного валідного запису, звіт не сформовано")
        return 1
    print()

    # --- Статистика ---
    print("Розрахунок статистики...")
    stats = calculate_statistics(records)
    print("✓ Статистика розрахована\n")

    # --- Звіт ---
    print("Формування звіту...")
    report = build_report(stats, skipped)
    try:
        save_report(report_path, report)
    except OSError as e:
        print(f"✗ Не вдалося зберегти звіт:\n  {e}")
        return 1
    print(f"✓ Звіт збережено: {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""
MEDASSISTANT
============

Завантаження записів...
✓ Валідних записів: 4, пропущено: 3
  ⚠ запис №5: відсутні поля: diagnosis
  ⚠ запис №6: id має бути додатним цілим числом, отримано -6; name не може бути порожнім, отримано ''; age має бути додатним цілим числом, отримано '61'; temperature має бути в діапазоні 25.0-45.0, отримано 99
  ⚠ запис №7: запис має бути словником (dict), отримано str

Розрахунок статистики...
✓ Статистика розрахована

Формування звіту...
✓ Звіт збережено: data/report.txt
"""

##Variant#2
"""
data/patients.json
[
  {"id": 1, "name": "Ivan", "age": 42, "diagnosis": "sinusitis", "temperature": 37.2},
  {"id": 2, "name": "Olena", "age": 35, "diagnosis": "rhinitis", "temperature": 38.4},
  {"id": 3, "name": "Petro", "age": 61, "diagnosis": "sinusitis", "temperature": 38.5},
  {"id": 4, "name": "Sofia", "age": 15, "diagnosis": "otitis", "temperature": 36.9},
  {"id": 5, "name": "Mykola", "age": 8, "diagnosis": "pharyngitis"},
  {"id": -6, "name": "", "age": "61", "diagnosis": "", "temperature": 99},
  "not a record",
  {"id": 8, "name": "Hanna", "age": 29, "diagnosis": "pharyngitis", "temperature": 39.1}
]

"""


#patient_record.py
"""patient_record.py

The PatientRecord data model for MedAssistant: state, validation, and
the behavior that belongs to a single patient record.
"""

from dataclasses import dataclass, fields

ADULT_AGE = 18
FEVER_THRESHOLD = 37.5
MIN_TEMPERATURE = 25.0
MAX_TEMPERATURE = 45.0


class RecordValidationError(ValueError):
    """Raised when a record is invalid.

    Carries EVERY problem found (not just the first), as a list, so callers
    never have to split a message string to get the individual problems.
    It subclasses ValueError, so `except ValueError` still catches it.
    """

    def __init__(self, errors: list[str]) -> None:
        self.errors = list(errors)
        super().__init__("; ".join(self.errors))


def _is_int(value: object) -> bool:
    """True for real integers. bool is excluded: True would pass as 1."""
    return isinstance(value, int) and not isinstance(value, bool)


def _is_number(value: object) -> bool:
    """True for int/float. bool is excluded for the same reason."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


@dataclass
class PatientRecord:
    id: int
    name: str
    age: int
    diagnosis: str
    temperature: float

    def __post_init__(self) -> None:
        """Validate every field right after the generated __init__ ran.

        Collect-all: all fields are checked and all problems are reported
        together, so one run shows everything that is wrong.

        Raises:
            RecordValidationError: If at least one field is invalid.
        """
        errors = []

        if not _is_int(self.id) or self.id <= 0:
            errors.append(f"id must be a positive integer, got {self.id!r}")

        if not isinstance(self.name, str) or not self.name.strip():
            errors.append(f"name must be a non-empty string, got {self.name!r}")

        if not _is_int(self.age) or self.age <= 0:
            errors.append(f"age must be a positive integer, got {self.age!r}")

        if not isinstance(self.diagnosis, str) or not self.diagnosis.strip():
            errors.append(f"diagnosis must be a non-empty string, got {self.diagnosis!r}")

        if not _is_number(self.temperature):
            errors.append(f"temperature must be a number, got {self.temperature!r}")
        elif not MIN_TEMPERATURE <= self.temperature <= MAX_TEMPERATURE:
            errors.append(
                f"temperature must be between {MIN_TEMPERATURE} and "
                f"{MAX_TEMPERATURE}, got {self.temperature}"
            )

        if errors:
            raise RecordValidationError(errors)

    @classmethod
    def from_dict(cls, data: dict) -> "PatientRecord":
        """Build a PatientRecord from a plain dict (e.g. one JSON object).

        Expected keys are taken from the dataclass fields themselves, so
        adding a field later needs no change here. Unknown extra keys are
        ignored. Value checks are NOT repeated here: the constructor runs
        __post_init__, which is the single place that knows the rules.

        Args:
            data: The raw record.

        Returns:
            PatientRecord: A valid record.

        Raises:
            RecordValidationError: If data is not a dict, keys are missing,
                or any value is invalid.
        """
        if not isinstance(data, dict):
            raise RecordValidationError(
                [f"record must be a JSON object, got {type(data).__name__}"]
            )

        names = [field.name for field in fields(cls)]
        missing = [name for name in names if name not in data]
        if missing:
            raise RecordValidationError([f"missing key {name!r}" for name in missing])

        return cls(**{name: data[name] for name in names})

    def is_adult(self) -> bool:
        """Check whether the patient is an adult (18 or older)."""
        return self.age >= ADULT_AGE

    def is_fever(self) -> bool:
        """Check whether the temperature indicates a fever (>= 37.5 C)."""
        return self.temperature >= FEVER_THRESHOLD

    def summary(self) -> str:
        """Return a one-line, human-readable description of the record."""
        age_group = "adult" if self.is_adult() else "minor"
        fever_status = "fever" if self.is_fever() else "no fever"
        return (
            f"#{self.id} {self.name} ({self.age}, {age_group}) — "
            f"{self.diagnosis}, {self.temperature}°C ({fever_status})"
        )


@dataclass(frozen=True)
class SkippedRecord:
    """A raw record that could not become a PatientRecord, and why."""

    index: int
    label: str
    reasons: tuple[str, ...]


def _label(data: object) -> str:
    """Best-effort human label for a raw record (its name, if it has one)."""
    name = data.get("name") if isinstance(data, dict) else None
    return name if isinstance(name, str) and name.strip() else "unnamed"


def build_records(
    raw_records: list,
) -> tuple[list[PatientRecord], list[SkippedRecord]]:
    """Turn raw JSON records into valid PatientRecords; skip the bad ones.

    One bad record never stops the rest. Only RecordValidationError is
    caught: any other exception is a real bug and must not be hidden.

    Args:
        raw_records: The decoded JSON (expected to be a list).

    Returns:
        tuple: (valid records, skipped records with reasons).

    Raises:
        ValueError: If raw_records is not a list at all.
    """
    if not isinstance(raw_records, list):
        raise ValueError(f"expected a JSON array of records, got {type(raw_records).__name__}")

    records = []
    skipped = []

    for index, data in enumerate(raw_records):
        try:
            records.append(PatientRecord.from_dict(data))
        except RecordValidationError as error:
            skipped.append(SkippedRecord(index, _label(data), tuple(error.errors)))

    return records, skipped


#statistics_utils.py
"""statistics_utils.py

Aggregate statistics over a list of PatientRecord objects.
Pure computation: no file access, no printing.
"""

from dataclasses import dataclass

from patient_record import PatientRecord


@dataclass(frozen=True)
class Statistics:
    """All aggregate results in one object, passed to the report builder."""

    total: int
    adults: int
    average_age: float
    average_temperature: float
    oldest: PatientRecord
    fever_records: tuple[PatientRecord, ...]


def _require_records(records: list[PatientRecord]) -> None:
    """Fail Fast with a clear message instead of ZeroDivisionError later."""
    if not records:
        raise ValueError("cannot calculate statistics: no valid records")


def average_age(records: list[PatientRecord]) -> float:
    """Average age of the given records."""
    _require_records(records)
    return sum(record.age for record in records) / len(records)


def average_temperature(records: list[PatientRecord]) -> float:
    """Average temperature of the given records."""
    _require_records(records)
    return sum(record.temperature for record in records) / len(records)


def oldest_record(records: list[PatientRecord]) -> PatientRecord:
    """The record with the highest age (the first one if there is a tie)."""
    _require_records(records)
    return max(records, key=lambda record: record.age)


def fever_records(records: list[PatientRecord]) -> list[PatientRecord]:
    """Records for which is_fever() is True."""
    return [record for record in records if record.is_fever()]


def count_adults(records: list[PatientRecord]) -> int:
    """How many records satisfy is_adult()."""
    return sum(1 for record in records if record.is_adult())


def calculate_statistics(records: list[PatientRecord]) -> Statistics:
    """Combine all statistics into one Statistics object.

    Raises:
        ValueError: If records is empty.
    """
    _require_records(records)
    return Statistics(
        total=len(records),
        adults=count_adults(records),
        average_age=average_age(records),
        average_temperature=average_temperature(records),
        oldest=oldest_record(records),
        fever_records=tuple(fever_records(records)),
    )


#report_utils.py
"""report_utils.py

Turning statistics into a text report, and saving it.
"""

from pathlib import Path

from patient_record import FEVER_THRESHOLD, SkippedRecord
from statistics_utils import Statistics


def build_report(stats: Statistics, skipped: list[SkippedRecord]) -> str:
    """Build the text report. Pure formatting: no file access.

    Args:
        stats: Statistics of the valid records.
        skipped: Records that were skipped, with reasons.

    Returns:
        str: The full report text.
    """
    title = "MEDASSISTANT PATIENT REPORT"
    lines = [
        title,
        "=" * len(title),
        "",
        f"Records in file: {stats.total + len(skipped)}",
        f"Valid records: {stats.total}",
        f"Skipped records: {len(skipped)}",
        "",
        f"Average age: {stats.average_age:.1f}",
        f"Average temperature: {stats.average_temperature:.1f}",
        f"Adults: {stats.adults} of {stats.total}",
        f"Oldest patient: {stats.oldest.name} ({stats.oldest.age})",
        "",
        f"Patients with fever (>= {FEVER_THRESHOLD}°C): {len(stats.fever_records)}",
    ]
    lines += [f"  - {record.summary()}" for record in stats.fever_records]

    if skipped:
        lines += ["", f"Skipped records ({len(skipped)}):"]
        for item in skipped:
            lines.append(f"  - index {item.index} ({item.label}):")
            lines += [f"      * {reason}" for reason in item.reasons]

    return "\n".join(lines) + "\n"


def save_report(path: Path, report: str) -> None:
    """Write the report to disk (the only function here that touches files)."""
    path.write_text(report, encoding="utf-8")


#main.py
"""main.py

MedAssistant v2 entry point. Orchestration only:

    JSON -> PatientRecord.from_dict() (validation) -> list[PatientRecord]
         -> statistics -> report -> save

Helper modules only RAISE exceptions; this file is the one place that
decides how a problem is shown to the user.
"""

import json
import sys
from pathlib import Path

from patient_record import build_records
from report_utils import build_report, save_report
from statistics_utils import calculate_statistics

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "patients.json"
REPORT_PATH = BASE_DIR / "data" / "report.txt"


def read_json(path: Path) -> object:
    """Read and decode a JSON file."""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main(data_path: Path = DATA_PATH, report_path: Path = REPORT_PATH) -> int:
    """Run the whole pipeline.

    Returns:
        int: 0 on success, 1 on any handled failure (usable as exit code).
    """
    print("MEDASSISTANT")
    print("============\n")

    try:
        print("Loading JSON...")
        raw_records = read_json(data_path)
        print("✓ JSON loaded\n")

        print("Validating records...")
        records, skipped = build_records(raw_records)
        if skipped:
            print(f"⚠ {len(skipped)} record(s) skipped:")
            for item in skipped:
                print(f"  index {item.index} ({item.label}):")
                for reason in item.reasons:
                    print(f"    - {reason}")
        print(f"✓ {len(records)} valid record(s)\n")

        print("Calculating statistics...")
        stats = calculate_statistics(records)
        print("✓ Statistics calculated\n")

        print("Generating report...")
        save_report(report_path, build_report(stats, skipped))
        print(f"✓ Report saved: {report_path.name}")

    except FileNotFoundError as error:
        print(f"✗ File not found:\n  {error.filename}")
        return 1
    except json.JSONDecodeError as error:  # must come BEFORE ValueError (its parent)
        print(f"✗ Invalid JSON:\n  {error}")
        return 1
    except ValueError as error:
        print(f"✗ {error}")
        return 1
    except OSError as error:
        print(f"✗ File error: {error}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

"""
MEDASSISTANT
============

Loading JSON...
✓ JSON loaded

Validating records...
⚠ 3 record(s) skipped:
  index 4 (Mykola):
    - missing key 'temperature'
  index 5 (unnamed):
    - id must be a positive integer, got -6
    - name must be a non-empty string, got ''
    - age must be a positive integer, got '61'
    - diagnosis must be a non-empty string, got ''
    - temperature must be between 25.0 and 45.0, got 99
  index 6 (unnamed):
    - record must be a JSON object, got str
✓ 5 valid record(s)

Calculating statistics...
✓ Statistics calculated

Generating report...
✓ Report saved: report.txt
"""

"""
#data/medassistant.txt
MEDASSISTANT PATIENT REPORT
===========================

Records in file: 8
Valid records: 5
Skipped records: 3

Average age: 36.4
Average temperature: 38.0
Adults: 4 of 5
Oldest patient: Petro (61)

Patients with fever (>= 37.5°C): 3
  - #2 Olena (35, adult) — rhinitis, 38.4°C (fever)
  - #3 Petro (61, adult) — sinusitis, 38.5°C (fever)
  - #8 Hanna (29, adult) — pharyngitis, 39.1°C (fever)

Skipped records (3):
  - index 4 (Mykola):
      * missing key 'temperature'
  - index 5 (unnamed):
      * id must be a positive integer, got -6
      * name must be a non-empty string, got ''
      * age must be a positive integer, got '61'
      * diagnosis must be a non-empty string, got ''
      * temperature must be between 25.0 and 45.0, got 99
  - index 6 (unnamed):
      * record must be a JSON object, got str
"""



#test_medassistant.py
"""Tests for MedAssistant v2. Run with: python -m unittest -v"""

import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from abc import ABC, abstractmethod
from contextlib import redirect_stdout
from dataclasses import FrozenInstanceError
from pathlib import Path
from unittest.mock import patch

import main as app
from patient_record import (
    PatientRecord,
    RecordValidationError,
    SkippedRecord,
    build_records,
)
from report_utils import build_report, save_report
from statistics_utils import (
    average_age,
    average_temperature,
    calculate_statistics,
    count_adults,
    fever_records,
    oldest_record,
)

PROJECT_DIR = Path(__file__).resolve().parent

BASE = {
    "id": 1,
    "name": "Ivan",
    "age": 42,
    "diagnosis": "sinusitis",
    "temperature": 36.8,
}


def make(**overrides) -> PatientRecord:
    return PatientRecord(**{**BASE, **overrides})


class TestPatientRecordValidation(unittest.TestCase):
    def test_valid_record_keeps_its_fields(self):
        record = make()
        self.assertEqual(
            (record.id, record.name, record.age, record.diagnosis, record.temperature),
            (1, "Ivan", 42, "sinusitis", 36.8),
        )

    def test_boundary_values_are_accepted(self):
        for overrides in (
            {"temperature": 25.0},
            {"temperature": 45.0},
            {"temperature": 38},
            {"age": 1},
            {"id": 1},
        ):
            with self.subTest(overrides=overrides):
                make(**overrides)

    def test_each_bad_value_gives_exactly_one_error_naming_the_field(self):
        bad_values = {
            "id": [0, -1, "1", None, True, 1.5],
            "name": ["", "   ", None, 5],
            "age": [0, -5, "42", None, True, 42.0],
            "diagnosis": ["", "  ", None],
            "temperature": [24.9, 45.1, "37", None, True, float("nan"), float("inf")],
        }
        for field, values in bad_values.items():
            for value in values:
                with self.subTest(field=field, value=value):
                    with self.assertRaises(RecordValidationError) as ctx:
                        make(**{field: value})
                    errors = ctx.exception.errors
                    self.assertEqual(len(errors), 1)
                    self.assertTrue(errors[0].startswith(field))

    def test_all_errors_are_collected_in_field_order(self):
        with self.assertRaises(RecordValidationError) as ctx:
            PatientRecord(-1, "", -5, "", 100)
        errors = ctx.exception.errors
        self.assertEqual(len(errors), 5)
        fields = ("id", "name", "age", "diagnosis", "temperature")
        for error, field in zip(errors, fields, strict=True):
            self.assertTrue(error.startswith(field), error)

    def test_error_is_a_value_error_with_joined_message(self):
        with self.assertRaises(ValueError) as ctx:
            make(id=0, name="")
        error = ctx.exception
        self.assertIsInstance(error, RecordValidationError)
        self.assertEqual(str(error), "; ".join(error.errors))


class TestPatientRecordBehavior(unittest.TestCase):
    def test_is_adult_boundary(self):
        for age, expected in ((1, False), (17, False), (18, True), (19, True)):
            with self.subTest(age=age):
                self.assertEqual(make(age=age).is_adult(), expected)

    def test_is_fever_boundary(self):
        for temperature, expected in (
            (36.6, False),
            (37.4, False),
            (37.5, True),
            (37.6, True),
            (38, True),
        ):
            with self.subTest(temperature=temperature):
                self.assertEqual(make(temperature=temperature).is_fever(), expected)

    def test_summary_text(self):
        self.assertEqual(
            make().summary(),
            "#1 Ivan (42, adult) — sinusitis, 36.8°C (no fever)",
        )
        self.assertEqual(
            make(id=2, name="Sofia", age=15, diagnosis="otitis", temperature=38.0).summary(),
            "#2 Sofia (15, minor) — otitis, 38.0°C (fever)",
        )

    def test_summary_returns_text_and_prints_nothing(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            result = make().summary()
        self.assertIsInstance(result, str)
        self.assertEqual(buffer.getvalue(), "")

    def test_equality_by_value(self):
        self.assertEqual(make(), make())
        self.assertNotEqual(make(), make(id=2))


class TestFromDict(unittest.TestCase):
    def test_builds_the_same_record_as_the_constructor(self):
        self.assertEqual(PatientRecord.from_dict(BASE), make())

    def test_extra_keys_are_ignored(self):
        self.assertEqual(PatientRecord.from_dict({**BASE, "ward": "ENT"}), make())

    def test_all_missing_keys_are_reported_together(self):
        with self.assertRaises(RecordValidationError) as ctx:
            PatientRecord.from_dict({"id": 1})
        self.assertEqual(
            ctx.exception.errors,
            [
                "missing key 'name'",
                "missing key 'age'",
                "missing key 'diagnosis'",
                "missing key 'temperature'",
            ],
        )

    def test_non_dict_input_is_rejected(self):
        for value in ("text", None, 5, [1, 2]):
            with self.subTest(value=value):
                with self.assertRaises(RecordValidationError) as ctx:
                    PatientRecord.from_dict(value)
                self.assertIn("JSON object", ctx.exception.errors[0])

    def test_invalid_values_are_caught_by_post_init(self):
        with self.assertRaises(RecordValidationError) as ctx:
            PatientRecord.from_dict({**BASE, "age": "61"})
        self.assertTrue(ctx.exception.errors[0].startswith("age"))

    def test_input_dict_is_not_modified(self):
        data = dict(BASE)
        PatientRecord.from_dict(data)
        self.assertEqual(data, BASE)


class TestBuildRecords(unittest.TestCase):
    def test_valid_and_invalid_are_separated(self):
        raw = [
            BASE,
            {**BASE, "id": 2, "temperature": 1000},
            "x",
            {**BASE, "id": 3, "name": "Olena"},
        ]
        records, skipped = build_records(raw)
        self.assertEqual([r.id for r in records], [1, 3])
        self.assertEqual([s.index for s in skipped], [1, 2])
        self.assertEqual([s.label for s in skipped], ["Ivan", "unnamed"])
        self.assertTrue(all(isinstance(s, SkippedRecord) for s in skipped))
        self.assertTrue(all(isinstance(s.reasons, tuple) for s in skipped))

    def test_reasons_are_kept_as_separate_items(self):
        bad = {"id": -1, "name": "", "age": 1, "diagnosis": "d", "temperature": 36.6}
        _, skipped = build_records([bad])
        self.assertEqual(len(skipped[0].reasons), 2)

    def test_empty_list_gives_empty_results(self):
        self.assertEqual(build_records([]), ([], []))

    def test_non_list_raises_value_error(self):
        for value in ({"a": 1}, "text", None, 5):
            with self.subTest(value=value), self.assertRaises(ValueError):
                build_records(value)

    def test_real_bugs_are_not_swallowed(self):
        with patch.object(PatientRecord, "from_dict", side_effect=RuntimeError("bug")), self.assertRaises(RuntimeError):
            build_records([BASE])


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.records = [
            make(id=1, age=20, temperature=36.0),
            make(id=2, age=40, temperature=38.0),
            make(id=3, age=40, temperature=37.5),
            make(id=4, age=10, temperature=39.0),
        ]

    def test_individual_functions(self):
        self.assertAlmostEqual(average_age(self.records), 27.5)
        self.assertAlmostEqual(average_temperature(self.records), 37.625)
        self.assertEqual(count_adults(self.records), 3)
        self.assertEqual([r.id for r in fever_records(self.records)], [2, 3, 4])

    def test_oldest_takes_the_first_on_a_tie(self):
        self.assertEqual(oldest_record(self.records).id, 2)

    def test_calculate_statistics_combines_everything(self):
        stats = calculate_statistics(self.records)
        self.assertEqual(stats.total, 4)
        self.assertEqual(stats.adults, 3)
        self.assertAlmostEqual(stats.average_age, 27.5)
        self.assertAlmostEqual(stats.average_temperature, 37.625)
        self.assertEqual(stats.oldest.id, 2)
        self.assertEqual([r.id for r in stats.fever_records], [2, 3, 4])

    def test_statistics_object_is_frozen(self):
        stats = calculate_statistics(self.records)
        with self.assertRaises(FrozenInstanceError):
            stats.total = 99

    def test_empty_input_fails_fast_with_a_clear_message(self):
        for function in (average_age, average_temperature, oldest_record, calculate_statistics):
            with self.subTest(function=function.__name__), self.assertRaisesRegex(ValueError, "no valid records"):
                function([])
        self.assertEqual(fever_records([]), [])
        self.assertEqual(count_adults([]), 0)


class TestReport(unittest.TestCase):
    def setUp(self):
        self.records = [
            make(id=1, name="Ivan", age=42, temperature=36.8),
            make(id=2, name="Olena", age=35, temperature=38.4),
            make(id=3, name="Sofia", age=15, diagnosis="otitis", temperature=38.0),
        ]
        self.stats = calculate_statistics(self.records)

    def test_report_without_skipped_records(self):
        report = build_report(self.stats, [])
        for expected in (
            "MEDASSISTANT PATIENT REPORT",
            "Records in file: 3",
            "Valid records: 3",
            "Skipped records: 0",
            "Average age: 30.7",
            "Average temperature: 37.7",
            "Adults: 2 of 3",
            "Oldest patient: Ivan (42)",
            "Patients with fever (>= 37.5°C): 2",
            "  - #2 Olena (35, adult) — sinusitis, 38.4°C (fever)",
            "  - #3 Sofia (15, minor) — otitis, 38.0°C (fever)",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, report)
        self.assertNotIn("Skipped records (", report)
        self.assertTrue(report.endswith("\n"))

    def test_report_counts_valid_plus_skipped_as_records_in_file(self):
        skipped = [SkippedRecord(4, "Mykola", ("missing key 'temperature'",))]
        report = build_report(self.stats, skipped)
        self.assertIn("Records in file: 4", report)
        self.assertIn("Valid records: 3", report)
        self.assertIn("Skipped records: 1", report)

    def test_skipped_section_shows_index_label_and_every_reason(self):
        skipped = [
            SkippedRecord(4, "Mykola", ("missing key 'temperature'",)),
            SkippedRecord(
                5,
                "unnamed",
                (
                    "id must be a positive integer, got -6",
                    "name must be a non-empty string, got ''",
                ),
            ),
        ]
        report = build_report(self.stats, skipped)
        for expected in (
            "Skipped records (2):",
            "  - index 4 (Mykola):",
            "      * missing key 'temperature'",
            "  - index 5 (unnamed):",
            "      * id must be a positive integer, got -6",
            "      * name must be a non-empty string, got ''",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, report)

    def test_report_with_no_fever_lists_nobody(self):
        stats = calculate_statistics([make()])
        report = build_report(stats, [])
        self.assertIn("Patients with fever (>= 37.5°C): 0", report)
        self.assertNotIn("  - #", report)

    def test_save_report_keeps_non_ascii_characters(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "report.txt"
            report = build_report(self.stats, [])
            save_report(path, report)
            self.assertEqual(path.read_text(encoding="utf-8"), report)


class TestPipeline(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.dir = Path(temp.name)
        self.data_path = self.dir / "patients.json"
        self.report_path = self.dir / "report.txt"

    def run_pipeline(self, content=None, report_path=None):
        if content is not None:
            self.data_path.write_text(content, encoding="utf-8")
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = app.main(self.data_path, report_path or self.report_path)
        return code, buffer.getvalue()

    def test_valid_and_invalid_records_still_produce_a_report(self):
        content = json.dumps([BASE, {"id": 2}, {**BASE, "id": 3, "name": "Olena"}])
        code, output = self.run_pipeline(content)
        self.assertEqual(code, 0)
        self.assertIn("⚠ 1 record(s) skipped:", output)
        self.assertIn("  index 1 (unnamed):", output)
        self.assertIn("✓ 2 valid record(s)", output)
        report = self.report_path.read_text(encoding="utf-8")
        self.assertIn("Valid records: 2", report)
        self.assertIn("Skipped records (1):", report)

    def test_all_valid_records_print_no_warning(self):
        code, output = self.run_pipeline(json.dumps([BASE]))
        self.assertEqual(code, 0)
        self.assertNotIn("skipped", output)
        self.assertTrue(self.report_path.exists())

    def test_missing_file(self):
        code, output = self.run_pipeline()
        self.assertEqual(code, 1)
        self.assertIn("✗ File not found", output)
        self.assertIn(str(self.data_path), output)
        self.assertFalse(self.report_path.exists())

    def test_broken_json_is_reported_as_invalid_json_not_as_value_error(self):
        code, output = self.run_pipeline('[{"id": 1,')
        self.assertEqual(code, 1)
        self.assertIn("✗ Invalid JSON", output)
        self.assertFalse(self.report_path.exists())

    def test_json_that_is_not_an_array(self):
        code, output = self.run_pipeline('{"id": 1}')
        self.assertEqual(code, 1)
        self.assertIn("expected a JSON array", output)
        self.assertFalse(self.report_path.exists())

    def test_empty_array_and_all_invalid_records_stop_with_a_clear_message(self):
        for content in ("[]", json.dumps([{"id": 1}, "x"])):
            with self.subTest(content=content):
                code, output = self.run_pipeline(content)
                self.assertEqual(code, 1)
                self.assertIn("no valid records", output)
                self.assertFalse(self.report_path.exists())

    def test_unwritable_report_path_names_the_report_not_the_input(self):
        bad_report = self.dir / "no_such_folder" / "report.txt"
        code, output = self.run_pipeline(json.dumps([BASE]), report_path=bad_report)
        self.assertEqual(code, 1)
        self.assertIn(str(bad_report), output)

    def test_shipped_sample_data(self):
        code, _ = self.run_pipeline_with_shipped_data()
        self.assertEqual(code, 0)
        report = self.report_path.read_text(encoding="utf-8")
        for expected in (
            "Records in file: 8",
            "Valid records: 5",
            "Skipped records: 3",
            "Average age: 36.4",
            "Average temperature: 38.0",
            "Adults: 4 of 5",
            "Oldest patient: Petro (61)",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, report)

    def run_pipeline_with_shipped_data(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = app.main(app.DATA_PATH, self.report_path)
        return code, buffer.getvalue()

    def test_script_runs_from_any_working_directory(self):
        copy = self.dir / "project_copy"
        shutil.copytree(PROJECT_DIR, copy, ignore=shutil.ignore_patterns("__pycache__", "report.*"))
        env = {**os.environ, "PYTHONUTF8": "1"}
        result = subprocess.run(
            [sys.executable, "-X", "utf8", str(copy / "main.py")],
            cwd=tempfile.gettempdir(),
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
            env=env,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("✓ Report saved: report.txt", result.stdout)
        self.assertTrue((copy / "data" / "report.txt").exists())


class self(ABC):
    """A tiny, self-contained interface with useful default implementations."""

    @property
    @abstractmethod
    def name(self):
        return getattr(self, "_name", "self")

    @abstractmethod
    def run(self):
        return {"name": self.name}

    def describe(self):
        return f"{self.name}: {self.run()}"


if __name__ == "__main__":
    unittest.main()

"""
........................................
----------------------------------------------------------------------
Ran 40 tests in 0.117s

OK
"""

"""
*Тести

Команда: python -m unittest -v у папці проєкту, нічого встановлювати не треба. 
Результат: 40 тестів, OK.

Група тестів	                Кількість	Що перевіряє
TestPatientRecordValidation	    5	        Кожне некоректне значення 
                                            (0, -1, "42", None, True, nan, inf) 
                                            дає рівно одну помилку з назвою поля; 
                                            усі помилки збираються разом
TestPatientRecordBehavior	    5	        Межі: 17/18 років, 37.4/37.5 °C; 
                                            точний текст summary()
TestFromDict	                6	        Усі відсутні ключі в одній помилці, 
                                            не-словники, зайві ключі, 
                                            вхідний словник не змінюється
TestBuildRecords	            5	        Розділення на валідні та пропущені; 
                                            справжня помилка в коді 
                                            (RuntimeError) не ховається
TestStatistics	                5	        Значення, рівність за віком 
                                            (береться перший), порожній список
TestReport	                    5	        Секція пропущених, підписи index, 
                                            збереження ° і — у UTF-8
TestPipeline	                9	        Немає файлу, зламаний JSON, JSON не масив, 
                                            порожній масив, усі записи погані, 
                                            недоступний шлях звіту, запуск з іншої папки

Тест test_shipped_sample_data перевіряє точні цифри з patients.json. 
Якщо змінюєш тестові дані, цей тест впаде, і так задумано.

Лінтер я запускав так: ruff check --select E,F,W,I,B,UP --line-length 100. 
Якщо у твоєму редакторі інша довжина рядка (стандартна в ruff 88), він може запропонувати переформатування.

*Виправлення мого попереднього пояснення
Раніше я пояснив твоє попередження VS Code Import block is un-sorted так: імпорти мають іти за алфавітом модулів, тобто import json останнім. Це було неправильно. Я перевірив у ruff:

*Варіант	Результат
import json / from dataclasses import dataclass, asdict / from enum import Enum (твій початковий)	попередження
from dataclasses … / from enum … / import json (моя «порада»)	теж попередження
import json / from dataclasses import asdict, dataclass / from enum import Enum	чисто

*Справжня причина: 
імена всередині from dataclasses import dataclass, asdict мають бути за алфавітом, asdict, dataclass. 
Порядок самих рядків у твоєму файлі був правильним (import x перед from x import y), тож поправ лише цей рядок.

*Пояснення коду
*Архітектура. Модулі відповідають кроках pipeline з завдання:

Крок	                                            Хто робить
JSON → PatientRecord.from_dict() → validation	    patient_record.py
list[PatientRecord] → statistics	                statistics_utils.py
report → save	                                    report_utils.py
порядок кроків, повідомлення користувачу	        main.py

Допоміжні модулі лише піднімають винятки і нічого не друкують. Як показати помилку, вирішує main.py.

*PatientRecord як @dataclass. 
У Дні 12 ти писав __init__, __repr__ і порівняння вручну, тепер їх генерує декоратор. 
Вручну лишається те, що залежить від наших правил: 
__post_init__, from_dict(), is_adult(), is_fever(), summary().

*__post_init__ збирає всі помилки одразу. 
Це як validate_patient() з Дня 11, але правила тепер живуть у самому класі. 
Записи bool для id і age виключено, бо в Python True проходить як 1.

*RecordValidationError носить список проблем. 
У попередніх задачах помилки склеювались у рядок через "; ", а потім розрізались назад. 
Це ламалось би, якби в самому значенні був такий роздільник. Тепер список лежить в error.errors. 
Клас наслідує ValueError, тому старий except ValueError теж його ловить.

*from_dict() бере ключі з fields(cls). 
Якщо додаси нове поле в клас, функцію правити не треба. 
Значення вона не перевіряє, це робить __post_init__, тож правила в одному місці (DRY).

*build_records() ловить лише RecordValidationError. 
Погані дані пропускаються, а справжня помилка в коді (наприклад, друкарська помилка в імені атрибута) не ховається. Один із тестів перевіряє саме це. 
Якби тут стояв except Exception, такий баг потрапив би в «пропущені записи» і загубився б.

*Statistics об'єднує результати в один об'єкт. 
Без нього build_report() мав би шість параметрів. 
Клас frozen=True, тож результати не змінюються після обчислення. 
Порожній список дає зрозуміле ValueError, а не ZeroDivisionError (Fail Fast).

*Позначення в звіті. 
# означає id (#2 Olena), а позицію у файлі підписано словом index. 
# На першій спробі я використав # для обох, і Mykola з id 5 виглядав як #4.

*Порядок except у main() має значення.
    FileNotFoundError стоїть перед OSError, бо є його підкласом.
    json.JSONDecodeError стоїть перед ValueError, бо теж його підклас. 
Інакше зламаний JSON показувався б як загальна помилка валідації.
    error.filename вказує на реальний файл: 
якщо не вдалось записати звіт, помилка називає звіт, а не вхідний JSON.

*Шляхи й тестованість. 
Path(__file__) прив'язує шляхи до папки проєкту, тож програма працює з будь-якої робочої директорії (я запускав її з /). 
main() приймає шляхи параметрами, тому тести підставляють тимчасові файли замість справжніх. 
Код виходу 0 або 1 корисний, коли програму запускає інший скрипт.

*Обмеження
Перевірка лише при створенні. 
@dataclass без frozen=True дозволяє пізніше написати record.age = -5, і ніхто цього не перевірить. 
Виправлення: frozen=True із replace() (як у ModelConfig) або property-сеттер (як у Task 7).
Зайві ключі ігноруються. Запис із додатковим полем "ward" пройде.
Вік як 42.0 відхиляється. Це дробове число, а не ціле.
Дублікати id не виявляються. Це зайве для цього завдання (YAGNI), але в реальних даних може знадобитись.
Діапазон 25-45 °C для температури — моє припущення, як і раніше. 
За потреби змінюється двома константами.
"""

# ==============================================================================
# ==============================================================================
