# 🐍 День 13 — OOP II: `dataclass`, `classmethod`, `staticmethod` та encapsulation

Після Дня 12 ти вже освоїв базову модель:

```text
class
 ↓
object
 ↓
attributes
 ↓
methods
 ↓
state
```

На Дні 13 підемо на наступний рівень: навчимося **писати OOP-класи чистіше, компактніше та ближче до реального Python-коду**.

Це особливо важливо для твого майбутнього `Medical Imaging AI`, де з'являться об'єкти на кшталт:

```text
Patient
Image
Study
Dataset
Prediction
ModelConfig
```

---

# 🎯 Цілі Дня 13

Сьогодні освоїмо:

* `@dataclass`;
* `field()`;
* default values;
* `__post_init__()`;
* `@classmethod`;
* `@staticmethod`;
* property;
* контроль доступу до атрибутів;
* `_private` convention;
* immutable objects через `frozen=True`;
* порівняння звичайного класу та `dataclass`.

Головна ідея:

```text
Day 12
ручний OOP
   ↓
Day 13
Pythonic OOP
```

---

# 1. Проблема звичайного класу

На Дні 12 ми писали:

```python
class Patient:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Patient(name={self.name!r}, age={self.age})"
```

Це нормально.

Але якщо клас має:

```text
10 полів
__init__
__repr__
__eq__
```

коду стає багато.

Для класів, які переважно зберігають дані, Python має спеціальний інструмент:

```python
@dataclass
```

---

# 2. `@dataclass`

```python
from dataclasses import dataclass


@dataclass
class Patient:
    name: str
    age: int
```

Тепер можна:

```python
patient = Patient("Ivan", 42)

print(patient)
```

і Python автоматично створить зрозумілий `repr`:

```text
Patient(name='Ivan', age=42)
```

Також автоматично генерується порівняння:

```python
patient1 = Patient("Ivan", 42)
patient2 = Patient("Ivan", 42)

print(patient1 == patient2)
```

Результат:

```text
True
```

---

# 3. Default values

```python
from dataclasses import dataclass


@dataclass
class Patient:
    name: str
    age: int
    diagnosis: str = "unknown"
```

Тепер:

```python
Patient("Ivan", 42)
```

отримаємо:

```text
Patient(name='Ivan', age=42, diagnosis='unknown')
```

---

# 4. `field()`

Для складніших полів використовуємо:

```python
from dataclasses import dataclass, field


@dataclass
class Patient:
    name: str
    diagnoses: list[str] = field(default_factory=list)
```

Це важливо.

Не треба:

```python
diagnoses: list[str] = []
```

для mutable default.

Правильний варіант:

```python
field(default_factory=list)
```

---

# 5. `__post_init__()`

Дуже важлива концепція для твого MedAssistant.

`dataclass` створює `__init__` автоматично, але ми можемо додати власну перевірку після створення:

```python
from dataclasses import dataclass


@dataclass
class Patient:
    name: str
    age: int

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Name cannot be empty.")

        if self.age <= 0:
            raise ValueError("Age must be greater than 0.")
```

Тепер:

```python
Patient("Ivan", 42)
```

працює.

А:

```python
Patient("", -5)
```

дасть:

```text
ValueError
```

Це прямо продовжує validation із Дня 11 та OOP із Дня 12.

---

# 6. `classmethod`

Тепер дуже важливий тип методу.

```python
@dataclass
class Patient:
    name: str
    age: int

    @classmethod
    def from_dict(cls, data: dict) -> "Patient":
        return cls(
            name=data["name"],
            age=data["age"],
        )
```

Тепер:

```python
data = {
    "name": "Ivan",
    "age": 42,
}

patient = Patient.from_dict(data)
```

Це чудово підходить для твого JSON pipeline:

```text
JSON dict
   ↓
Patient.from_dict()
   ↓
Patient object
```

---

# 7. `self` vs `cls`

### Instance method

```python
def summary(self):
```

Працює з **конкретним об'єктом**.

### Class method

```python
@classmethod
def from_dict(cls, data):
```

Працює через **клас**.

Спрощено:

```text
self → конкретний object
cls  → class
```

Наприклад:

```python
patient.from_something(...)
```

не означає те саме, що:

```python
Patient.from_dict(...)
```

---

# 8. `staticmethod`

Статичний метод не потребує ні `self`, ні `cls`.

```python
@dataclass
class Patient:
    name: str
    age: int

    @staticmethod
    def is_valid_age(age: int) -> bool:
        return age > 0
```

Виклик:

```python
Patient.is_valid_age(42)
```

Результат:

```text
True
```

Це корисно, коли функція логічно пов'язана з класом, але не використовує стан об'єкта.

---

# 9. `classmethod` vs `staticmethod`

Запам'ятай:

| Тип             | Перший аргумент | Доступ до instance | Доступ до class |
| --------------- | --------------- | ------------------ | --------------- |
| instance method | `self`          | ✅                  | ✅               |
| classmethod     | `cls`           | ❌                  | ✅               |
| staticmethod    | немає           | ❌                  | ❌               |

---

# 10. Properties

Іноді не хочемо дозволяти пряме неконтрольоване редагування атрибута.

Наприклад:

```python
class Patient:
    def __init__(self, age: int):
        self._age = age

    @property
    def age(self) -> int:
        return self._age
```

Тепер:

```python
patient.age
```

працює як звичайний атрибут.

Але всередині його контролює:

```python
@property
def age(...)
```

---

# 11. Setter

Можемо контролювати зміну:

```python
class Patient:
    def __init__(self, age: int):
        self.age = age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Age must be greater than 0.")

        self._age = value
```

Тепер:

```python
patient.age = 43
```

працює.

А:

```python
patient.age = -5
```

викличе `ValueError`.

---

# 12. `_attribute`

У Python:

```python
_age
```

не є справді private.

Це **convention**:

> "не використовуй напряму ззовні без необхідності".

Тому:

```python
self._age
```

означає:

```text
internal implementation detail
```

На відміну від деяких інших мов Python більше покладається на convention.

---

# 13. `frozen=True`

Для об'єктів, які після створення не повинні змінюватися:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class PatientID:
    value: int
```

Тепер:

```python
patient_id = PatientID(101)

patient_id.value = 102
```

дасть помилку.

Це називається **immutable object**.

---

# 🏫 CLASS WORK

## Task 1 — перший `dataclass`

Створи:

```python
@dataclass
class Patient:
    name: str
    age: int
```

Створи 4 пацієнти та покажи:

* `repr`;
* порівняння двох однакових пацієнтів;
* порівняння двох різних пацієнтів.

---

# Task 2 — default values

Додай:

```python
diagnosis: str = "unknown"
temperature: float = 36.6
```

Створи пацієнтів:

```python
Patient("Ivan", 42)
Patient("Olena", 35, "rhinitis", 37.2)
```

---

# Task 3 — `default_factory`

Додай:

```python
diagnoses: list[str]
```

але використай:

```python
field(default_factory=list)
```

Перевір, що два пацієнти мають **різні списки**:

```python
patient1.diagnoses.append("sinusitis")
```

та переконайся, що:

```python
patient2.diagnoses
```

не змінився.

---

# Task 4 — `__post_init__`

Реалізуй:

```python
def __post_init__(self) -> None:
    ...
```

Правила:

```text
name не може бути порожнім
age > 0
temperature > 0
```

Некоректні значення повинні викликати:

```python
ValueError
```

---

# Task 5 — `classmethod`

Створи:

```python
@classmethod
def from_dict(
    cls,
    data: dict,
) -> "Patient":
    ...
```

і:

```python
data = {
    "name": "Ivan",
    "age": 42,
    "diagnosis": "sinusitis",
}
```

Перетвори його в:

```python
Patient(...)
```

---

# Task 6 — `staticmethod`

Додай:

```python
@staticmethod
def is_valid_age(age: int) -> bool:
    ...
```

Перевір:

```text
17 → False
18 → True
42 → True
-5 → False
```

---

# Task 7 — property

Створи клас:

```python
class Patient:
    ...
```

зі внутрішнім:

```python
_age
```

і property:

```python
age
```

Setter повинен забороняти:

```text
0
-1
"42"
```

---

# ⚔️ CHALLENGES

## Challenge 1 — `MedicalRecord`

Створи:

```python
@dataclass
class MedicalRecord:
    id: int
    patient_name: str
    diagnosis: str
    temperature: float
```

Додай:

```text
__post_init__()
summary()
is_fever()
from_dict()
```

---

# Challenge 2 — immutable configuration

Створи:

```python
@dataclass(frozen=True)
class ModelConfig:
    model_name: str
    image_size: int
    threshold: float
```

Наприклад:

```python
config = ModelConfig(
    model_name="ResNet50",
    image_size=224,
    threshold=0.5,
)
```

Перевір, що:

```python
config.threshold = 0.7
```

не дозволяється.

Це вже пряме наближення до майбутніх ML-проєктів.

---

# Challenge 3 — Factory from JSON

Створи:

```python
@classmethod
def from_dict(cls, data: dict) -> "MedicalRecord":
    ...
```

Потім:

```text
JSON
 ↓
dict
 ↓
MedicalRecord.from_dict()
 ↓
object
```

Створи список:

```python
records: list[MedicalRecord]
```

з JSON-подібних словників.

---

# Challenge 4 — properties for BMI

Створи:

```python
@dataclass
class Patient:
    name: str
    weight: float
    height: float
```

та:

```python
@property
def bmi(self) -> float:
    ...
```

Тоді:

```python
patient.bmi
```

повинен автоматично повертати BMI.

Тут вже побачиш різницю:

```python
patient.calculate_bmi()
```

проти:

```python
patient.bmi
```

---

# 🔥 Challenge 5 — MedAssistant OOP v2

Перероби твій День 12 `PatientRecord` у `@dataclass`.

Має бути:

```text
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
```

Клас:

```python
@dataclass
class PatientRecord:
    id: int
    name: str
    age: int
    diagnosis: str
    temperature: float
```

Обов'язково реалізуй:

```text
__post_init__()
from_dict()
is_adult()
is_fever()
summary()
```

Це буде дуже корисна вправа, тому що ти побачиш, **наскільки `dataclass` прибирає boilerplate**, який ти написав на Дні 12 вручну.

---

# 🏠 HOMEWORK

Створи:

```text
day13/
├── class_work_13.py
├── home_work_13.py
├── patient.py
├── model_config.py
└── data/
```

## `patient.py`

```python
@dataclass
class Patient:
    ...
```

із:

```text
validation
properties
classmethod
staticmethod
methods
```

## `model_config.py`

```python
@dataclass(frozen=True)
class ModelConfig:
    ...
```

## `home_work_13.py`

Побудуй:

```text
load JSON
    ↓
Patient.from_dict()
    ↓
validation
    ↓
statistics
    ↓
report
```

---

# 🧠 80/20 Дня 13

Сьогодні найважливіші речі:

```python
@dataclass
```

```python
field(default_factory=list)
```

```python
__post_init__()
```

```python
@classmethod
```

```python
@staticmethod
```

```python
@property
```

і:

```python
@dataclass(frozen=True)
```

Головний conceptual shift:

```text
Day 12
"Я можу створити клас"

        ↓

Day 13
"Я можу спроєктувати Pythonic data object"
```

---

# 🔗 Зв'язок з твоїм AI/ML напрямом

Цей день особливо корисний перед переходом до Data Science.

У майбутньому в тебе будуть об'єкти приблизно такого типу:

```text
ImageMetadata
Study
Patient
DatasetConfig
ModelConfig
Prediction
TrainingConfig
InferenceResult
```

Наприклад:

```python
config = ModelConfig(
    image_size=512,
    threshold=0.7,
)
```

або:

```python
record = MedicalRecord.from_dict(json_data)
```

Тобто ти вже тренуєш той самий стиль роботи, який пізніше зустрінеш у складних AI/ML системах.

---

# 🎯 Результат Дня 13

Після виконання ти маєш уміти пояснити:

```text
@dataclass
        ↓
automatic __init__
automatic __repr__
automatic equality
        ↓
__post_init__
        ↓
validation
```

а також чітко розрізняти:

```text
self
cls
staticmethod
property
```

і розуміти, **коли об'єкт повинен бути mutable, а коли immutable**.

Після здачі `class_work_13.py`, `home_work_13.py` та додаткових модулів перевірю їх у нашому звичному форматі: **кожне завдання → оцінка → технічні зауваження → загальна оцінка `/10` → рівень → GitHub commit `learn(day13): ...`**.
