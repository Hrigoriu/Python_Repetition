# 🐍 День 12 — Object-Oriented Programming (OOP): класи та об’єкти

Після Дня 11 ти вже вмієш будувати **модулі, валідацію та контроль помилок**. Наступний логічний крок — навчитися об’єднувати **дані + поведінку** в окремі об’єкти.

Сьогодні починаємо OOP. Це один із ключових переходів у Python, тому тут важливіше **зрозуміти модель**, ніж написати якомога більше коду.

---

# 🎯 Що маєш освоїти сьогодні

До кінця Дня 12 ти повинен розуміти:

```text
class
object
instance
__init__
self
attributes
methods
class attributes
instance attributes
```

і вміти:

* створювати власні класи;
* створювати екземпляри;
* зберігати стан об’єкта;
* описувати поведінку через методи;
* використовувати `self`;
* використовувати type hints у класах;
* відокремлювати відповідальність між класами.

---

# 1. Що таке клас

Клас — це шаблон.

```python
class Patient:
    pass
```

А об'єкт:

```python
patient = Patient()
```

Тобто:

```text
class Patient
      ↓
     blueprint
      ↓
patient = Patient()
      ↓
   object
```

---

# 2. `__init__`

Найважливіший метод початку.

```python
class Patient:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
```

Створення:

```python
patient = Patient("Ivan", 42)
```

Тепер:

```python
print(patient.name)
print(patient.age)
```

отримаємо:

```text
Ivan
42
```

---

# 3. Що таке `self`

Це одна з головних концепцій сьогодні.

```python
patient.name
```

означає:

> отримати `name` конкретного об'єкта `patient`.

Усередині класу:

```python
self.name
```

означає:

> `name` цього конкретного екземпляра.

Наприклад:

```python
patient1 = Patient("Ivan", 42)
patient2 = Patient("Olena", 35)
```

У них різні:

```text
patient1.name → Ivan
patient2.name → Olena
```

але клас той самий.

---

# 4. Методи

Метод — функція всередині класу.

```python
class Patient:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"Patient: {self.name}, age: {self.age}"
```

Виклик:

```python
patient = Patient("Ivan", 42)

print(patient.introduce())
```

---

# 5. Дані + поведінка

До OOP ми писали:

```python
patient = {
    "name": "Ivan",
    "age": 42,
}

def is_adult(patient):
    return patient["age"] >= 18
```

З класом:

```python
class Patient:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        return self.age >= 18
```

Тепер:

```python
patient = Patient("Ivan", 42)

patient.is_adult()
```

Тобто:

```text
dict + functions
        ↓
      class
        ↓
data + behavior
```

---

# 6. Class attribute vs instance attribute

### Instance attribute

```python
class Patient:
    def __init__(self, name: str):
        self.name = name
```

Кожен об'єкт має власний `name`.

### Class attribute

```python
class Patient:
    species = "Human"
```

Воно спільне для класу.

```python
patient1 = Patient()
patient2 = Patient()

print(patient1.species)
print(patient2.species)
```

---

# 7. `__repr__`

Для зручного представлення об'єкта:

```python
class Patient:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Patient(name={self.name!r}, age={self.age})"
```

Тепер:

```python
print(patient)
```

дасть:

```text
Patient(name='Ivan', age=42)
```

Це дуже корисна практика для debugging.

---

# 🏫 CLASS WORK

## Task 1 — перший клас

Створи:

```python
class Patient:
    pass
```

та створіть три екземпляри:

```text
Ivan
Olena
Petro
```

Покажи, що це різні об'єкти.

---

## Task 2 — `__init__`

Розшир:

```python
class Patient:
    def __init__(self, name: str, age: int):
        ...
```

Збережи:

```text
name
age
```

Створи щонайменше 4 пацієнти.

---

## Task 3 — метод `is_adult`

Додай:

```python
def is_adult(self) -> bool:
    ...
```

Перевір:

```text
15 → False
18 → True
42 → True
```

---

## Task 4 — BMI method

Додай:

```python
def calculate_bmi(
    self,
    weight: float,
    height: float,
) -> float:
    ...
```

Формула:

```text
BMI = weight / height²
```

`height` — у метрах.

---

## Task 5 — validation

Твій клас повинен не дозволяти створити очевидно некоректного пацієнта:

```python
Patient("", 42)
Patient("Ivan", -5)
```

При невалідних значеннях:

```python
raise ValueError(...)
```

Тут використай знання **Дня 11**.

---

## Task 6 — `__repr__`

Додай:

```python
def __repr__(self) -> str:
    ...
```

Очікуваний стиль:

```text
Patient(name='Ivan', age=42)
```

---

## Task 7 — клас і список

Створи:

```python
patients: list[Patient]
```

з п'яти пацієнтів.

За допомогою methods класу:

* порахуй кількість дорослих;
* знайди середній вік;
* виведи BMI кількох пацієнтів.

---

# ⚔️ CHALLENGES

## Challenge 1 — `PatientRecord`

Створи повноцінний клас:

```python
class PatientRecord:
    ...
```

Поля:

```text
id
name
age
diagnosis
temperature
```

Методи:

```python
is_adult()
is_fever()
summary()
```

---

## Challenge 2 — validation inside class

Перенеси валідацію з Дня 11 у клас.

Наприклад:

```python
PatientRecord(
    id=1,
    name="Ivan",
    age=42,
    diagnosis="sinusitis",
    temperature=36.8,
)
```

повинен створювати об'єкт.

А:

```python
PatientRecord(
    id=-1,
    name="",
    age=-5,
    diagnosis="",
    temperature=100,
)
```

повинен кинути `ValueError`.

Тут важливо **не просто копіювати** код Дня 11, а правильно розмістити перевірки всередині object model.

---

# Challenge 3 — methods that use state

Додай:

```python
def update_temperature(self, temperature: float) -> None:
    ...
```

та:

```python
def change_diagnosis(self, diagnosis: str) -> None:
    ...
```

Після цього:

```python
patient.update_temperature(38.4)
patient.change_diagnosis("acute sinusitis")
```

об'єкт повинен змінити власний стан.

---

# Challenge 4 — statistics without dictionaries

На Дні 9–11 у тебе були:

```python
list[dict]
```

Тепер використовуй:

```python
list[PatientRecord]
```

Створи функції:

```python
def average_age(patients: list[PatientRecord]) -> float:
    ...


def oldest_patient(
    patients: list[PatientRecord],
) -> PatientRecord:
    ...
```

Порівняй концептуально:

```text
list[dict]
```

і:

```text
list[PatientRecord]
```

---

# 🔥 Challenge 5 — MedAssistant OOP

Це головне завдання дня.

Перероби частину твого MedAssistant із:

```text
list[dict]
```

на:

```text
list[Patient]
```

Архітектура:

```text
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
```

Наприклад:

```python
patients = [
    Patient(
        name="Ivan",
        age=42,
        diagnosis="sinusitis",
        temperature=37.2,
    ),
    ...
]
```

Потім:

```python
for patient in patients:
    if patient.is_fever():
        ...
```

Тобто логіка починає читатися природною мовою:

```text
patient.is_adult()
patient.is_fever()
patient.calculate_bmi()
patient.summary()
```

Саме тут ти почнеш бачити реальну перевагу OOP.

---

# 🏠 HOMEWORK

Створи:

```text
day12/
├── class_work_12.py
├── home_work_12.py
├── patient.py
└── data/
```

У `patient.py`:

```python
class Patient:
    ...
```

У `home_work_12.py`:

```text
load data
   ↓
create Patient objects
   ↓
validate
   ↓
process
   ↓
statistics
   ↓
report
```

Обов'язково використай:

```text
__init__
self
methods
type hints
raise ValueError
__repr__
```

---

# 🧠 80/20 Дня 12

Сьогодні тобі не потрібно запам'ятовувати десятки OOP-патернів.

Зосередься на:

```python
class Patient:
```

```python
def __init__(self, ...):
```

```python
self.name
```

```python
def method(self):
```

```python
patient = Patient(...)
```

і головній моделі:

```text
CLASS
  ↓
OBJECT
  ↓
STATE + BEHAVIOR
```

---

# 🔗 Зв'язок із твоєю майбутньою професією

У майбутніх ML-проєктах ти зустрінеш об'єкти на кожному рівні:

```text
Patient
Image
Dataset
Model
Prediction
Trainer
Config
Pipeline
```

Наприклад:

```python
model.predict(image)
dataset[0]
patient.is_fever()
pipeline.run()
```

Тобто OOP — це не окрема «теоретична тема». Воно стане частиною способу, яким ти будеш працювати з ML-фреймворками та великими Python-проєктами.

---

# 🎯 Результат Дня 12

Після завершення я очікую, що ти зможеш пояснити без підказок:

> **Що таке class, object, instance, `self`, `__init__`, attribute та method — і навіщо вони потрібні?**

А головне — ти повинен уміти перетворити:

```python
{"name": "Ivan", "age": 42}
```

у:

```python
Patient("Ivan", 42)
```

і перенести пов'язану з пацієнтом поведінку всередину самого об'єкта.

**День 12 — перший фундаментальний крок у OOP.**
