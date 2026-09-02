# День 8 — Колекції Python: `list`, `tuple`, `dict`, `set`

Сьогодні переходимо до **структур даних**. Після comprehension це логічний наступний крок: важливо не просто вміти створювати колекції, а розуміти **як вони зберігають дані, як змінюються, як копіюються та коли яку структуру обирати**.

Для твоєї подальшої роботи з **NumPy → Pandas → ML** це одна з базових тем.

## 🎯 Мета Дня 8

Після уроку ти маєш впевнено розуміти:

* `list`
* `tuple`
* `dict`
* `set`
* mutable vs immutable;
* indexing / slicing колекцій;
* `append()`, `extend()`, `insert()`, `remove()`, `pop()`;
* `keys()`, `values()`, `items()`;
* `in`;
* unpacking;
* shallow copy;
* deep copy;
* вкладені структури;
* коли використовувати `list`, `tuple`, `dict`, `set`.

---

# 1. `list`

`list` — впорядкована **mutable** колекція.

```python
patients = ["Ivan", "Olena", "Petro"]
```

Можна змінювати:

```python
patients.append("Hanna")
```

Отримаємо:

```python
["Ivan", "Olena", "Petro", "Hanna"]
```

---

# 2. Indexing у `list`

```python
patients = ["Ivan", "Olena", "Petro"]
```

```python
print(patients[0])
print(patients[-1])
```

Результат:

```text
Ivan
Petro
```

---

# 3. Slicing у `list`

Працює так само, як із `str`:

```python
numbers = [0, 1, 2, 3, 4, 5]
```

```python
numbers[1:4]
```

→

```python
[1, 2, 3]
```

---

# 4. Основні методи `list`

## `append()`

Додає **один** елемент.

```python
patients.append("Dmytro")
```

---

## `extend()`

Додає всі елементи іншої колекції.

```python
patients.extend(["Anna", "Oleh"])
```

---

## `insert()`

Вставляє елемент у конкретну позицію.

```python
patients.insert(1, "Maria")
```

---

## `remove()`

Видаляє перше співпадіння:

```python
patients.remove("Ivan")
```

---

## `pop()`

Видаляє та повертає елемент.

```python
removed = patients.pop()
```

Або:

```python
removed = patients.pop(1)
```

---

# 5. `sort()` vs `sorted()`

Ми вже бачили:

```python
sorted(patients)
```

Вона створює **новий список**.

А:

```python
patients.sort()
```

змінює існуючий список.

```python
numbers = [3, 1, 2]

result = numbers.sort()

print(numbers)
print(result)
```

Результат:

```text
[1, 2, 3]
None
```

Це важлива особливість.

---

# 6. `tuple`

`tuple` — впорядкована **immutable** колекція.

```python
patient = ("Ivan", 42, 180)
```

Не можна:

```python
patient[0] = "Petro"
```

буде:

```text
TypeError
```

---

## Коли використовувати `tuple`

Коли набір значень логічно не повинен змінюватися.

Наприклад:

```python
coordinates = (50.45, 30.52)
```

або:

```python
patient = ("Ivan", 42)
```

---

# 7. Tuple unpacking

Ти вже це використовував.

```python
patient = ("Ivan", 42)

name, age = patient
```

Тепер:

```python
print(name)
print(age)
```

---

# 8. Extended unpacking

```python
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers
```

Отримаємо:

```text
first  → 1
middle → [2, 3, 4]
last   → 5
```

Це дуже корисний Pythonic-патерн.

---

# 9. `dict`

`dict` зберігає пари:

```text
key → value
```

Наприклад:

```python
patient = {
    "name": "Ivan",
    "age": 42,
    "temperature": 38.2,
}
```

Доступ:

```python
print(patient["name"])
```

→

```text
Ivan
```

---

# 10. `dict.get()`

Небезпечніше:

```python
patient["weight"]
```

якщо ключа немає:

```text
KeyError
```

Безпечніше:

```python
patient.get("weight")
```

→ `None`

Або:

```python
patient.get("weight", 0)
```

→ `0`

---

# 11. `keys()`, `values()`, `items()`

```python
patient = {
    "name": "Ivan",
    "age": 42,
}
```

### Keys

```python
patient.keys()
```

### Values

```python
patient.values()
```

### Items

```python
patient.items()
```

Найважливіший варіант:

```python
for key, value in patient.items():
    print(key, value)
```

---

# 12. Додавання та зміна значень

```python
patient["weight"] = 82
```

Якщо ключ уже існує — значення зміниться.

```python
patient["age"] = 43
```

---

# 13. Видалення

```python
del patient["age"]
```

Або:

```python
age = patient.pop("age")
```

`pop()` повертає видалене значення.

---

# 14. `set`

`set` — колекція **унікальних** значень.

```python
symptoms = {
    "fever",
    "cough",
    "fever",
}
```

Результат:

```python
{"fever", "cough"}
```

Дублікат зникає.

---

# 15. Навіщо потрібен `set`

Наприклад:

```python
diagnoses = [
    "sinusitis",
    "rhinitis",
    "sinusitis",
    "otitis",
]
```

Отримати унікальні:

```python
unique_diagnoses = set(diagnoses)
```

---

# 16. Set operations

## Об'єднання

```python
a = {"fever", "cough"}
b = {"cough", "pain"}

a | b
```

→

```python
{"fever", "cough", "pain"}
```

---

## Перетин

```python
a & b
```

→

```python
{"cough"}
```

---

## Різниця

```python
a - b
```

→

```python
{"fever"}
```

---

# 17. `in`

Для `set` перевірка membership дуже природна:

```python
symptoms = {"fever", "cough", "pain"}

if "fever" in symptoms:
    print("Fever detected")
```

---

# 18. Порівняння структур

| Структура | Ordered | Mutable | Унікальність    |
| --------- | ------- | ------- | --------------- |
| `list`    | ✅       | ✅       | ❌               |
| `tuple`   | ✅       | ❌       | ❌               |
| `dict`    | ✅*      | ✅       | ключі унікальні |
| `set`     | ❌       | ✅       | ✅               |

* `dict` зберігає порядок вставки елементів.

---

# 19. Найважливіше: mutable vs immutable

### Mutable

```python
list
dict
set
```

### Immutable

```python
int
float
bool
str
tuple
frozenset
```

---

# 20. Небезпечна ситуація

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
```

Результат:

```python
[1, 2, 3, 4]
```

Чому?

Тому що:

```text
a ─────┐
       ▼
    [1,2,3]
       ▲
b ─────┘
```

`a` і `b` посилаються на **один об'єкт**.

---

# 21. Копія

```python
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
print(b)
```

Отримаємо:

```text
[1, 2, 3]
[1, 2, 3, 4]
```

---

# 22. Shallow copy

Тут починається важливий момент.

```python
a = [[1, 2], [3, 4]]
b = a.copy()
```

Зовнішній список скопійований, але внутрішні списки — ні.

Тобто:

```python
b[0].append(99)
```

може змінити й `a`.

---

# 23. `deepcopy`

```python
from copy import deepcopy

a = [[1, 2], [3, 4]]
b = deepcopy(a)

b[0].append(99)

print(a)
print(b)
```

Тепер вони незалежні.

---

# 24. Вкладений `dict`

Реальні дані часто виглядають так:

```python
patient = {
    "name": "Ivan",
    "age": 42,
    "measurements": {
        "temperature": 38.2,
        "weight": 82,
        "height": 180,
    },
}
```

Доступ:

```python
patient["measurements"]["temperature"]
```

---

# 25. `dict` + `list`

Наприклад:

```python
patient = {
    "name": "Ivan",
    "symptoms": [
        "fever",
        "cough",
        "pain",
    ],
}
```

Доступ:

```python
patient["symptoms"][0]
```

→

```text
fever
```

Саме такі вкладені структури дуже часто зустрічаються в JSON/API.

---

# 26. Копіювання вкладених даних

Для:

```python
patient_copy = patient.copy()
```

вкладені:

```python
patient["measurements"]
```

ще можуть залишатися спільними.

Для повністю незалежної копії:

```python
patient_copy = deepcopy(patient)
```

---

# Практика №1 — List

Створи:

```python
patients = ["Ivan", "Olena", "Petro"]
```

Виконай:

1. `append("Hanna")`
2. `insert(1, "Maria")`
3. `remove("Petro")`
4. `pop()`

Після кожної операції виведи список.

---

# Практика №2 — Tuple

Створи:

```python
patient = ("Ivan", 42, 180, 82)
```

Зроби unpacking:

```text
name
age
height
weight
```

Після цього виведи всі чотири значення.

---

# Практика №3 — Dict

Створи:

```python
patient = {
    "name": "Ivan",
    "age": 42,
    "diagnosis": "Sinusitis",
}
```

Додай:

```text
temperature
weight
height
```

Потім виведи всі `key → value` через `.items()`.

---

# Практика №4 — `get()`

Спробуй отримати:

```python
patient["allergy"]
```

Побачиш проблему.

Потім:

```python
patient.get("allergy")
```

і:

```python
patient.get("allergy", "Unknown")
```

Поясни різницю.

---

# Практика №5 — Set

Є:

```python
diagnoses = [
    "sinusitis",
    "rhinitis",
    "sinusitis",
    "otitis",
    "rhinitis",
]
```

Отримай список унікальних діагнозів через `set`.

---

# Практика №6 — Set operations

Є:

```python
patient_a = {"fever", "cough", "pain"}
patient_b = {"cough", "pain", "fatigue"}
```

Знайди:

* всі симптоми;
* спільні симптоми;
* симптоми тільки `patient_a`;
* симптоми тільки `patient_b`.

Використай:

```text
|
&
-
```

---

# Практика №7 — nested dictionary

Створи:

```python
patient = {
    "name": "Ivan",
    "measurements": {
        "temperature": 38.2,
        "weight": 82,
        "height": 180,
    },
}
```

Отримай:

```text
Name
Temperature
Weight
Height
```

---

# Практика №8 — копіювання

Продемонструй різницю між:

```python
b = a
```

```python
b = a.copy()
```

і:

```python
b = deepcopy(a)
```

Використай вкладений список:

```python
a = [[1, 2], [3, 4]]
```

і покажи, коли зміна `b` впливає на `a`.

---

# 🧠 Challenge №1

Не запускаючи код:

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)
print(a is b)
```

Що буде?

---

# 🧠 Challenge №2

Що відбудеться?

```python
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
print(b)
print(a is b)
```

---

# 🧠 Challenge №3

Що буде?

```python
data = {
    "patient": {
        "name": "Ivan",
        "age": 42,
    }
}

print(data["patient"]["name"])
```

Поясни, як Python знаходить `"Ivan"`.

---

# 🧠 Challenge №4

Що буде?

```python
symptoms = {"fever", "cough", "fever"}

print(len(symptoms))
```

Чому?

---

# 🚀 Challenge №5 — MedAssistant

Створи:

```python
patients = [
    {
        "name": "Ivan",
        "temperature": 36.6,
    },
    {
        "name": "Olena",
        "temperature": 38.2,
    },
    {
        "name": "Petro",
        "temperature": 39.1,
    },
]
```

За допомогою comprehension створи:

```python
{
    "Ivan": "normal",
    "Olena": "fever",
    "Petro": "high_fever",
}
```

Використай твою функцію:

```python
classify_temperature()
```

із попередніх днів.

Тут об'єднаються:

```text
list
+
dict
+
dict comprehension
+
function
```

---

# 🚀 Challenge №6 — Junior+

Створи:

```python
def group_patients_by_status(
    patients: list[dict],
) -> dict[str, list[str]]:
    ...
```

Вхід:

```python
patients = [
    {"name": "Ivan", "temperature": 36.6},
    {"name": "Olena", "temperature": 38.2},
    {"name": "Petro", "temperature": 39.1},
    {"name": "Hanna", "temperature": 37.0},
]
```

Результат:

```python
{
    "normal": ["Ivan", "Hanna"],
    "fever": ["Olena"],
    "high_fever": ["Petro"],
}
```

**Не дублюй температурні пороги.**

Використай:

```python
classify_temperature()
```

---

# 🚀 Challenge №7 — Junior+

Створи:

```python
def get_unique_symptoms(
    patients: list[dict],
) -> set[str]:
    ...
```

Вхід:

```python
patients = [
    {
        "name": "Ivan",
        "symptoms": ["fever", "cough"],
    },
    {
        "name": "Olena",
        "symptoms": ["cough", "pain"],
    },
    {
        "name": "Petro",
        "symptoms": ["fever", "pain"],
    },
]
```

Результат:

```python
{
    "fever",
    "cough",
    "pain",
}
```

Тут тренуємо:

```text
nested structures
+
for
+
set
+
set.add()
```

---

# 🔥 Challenge №8 — найважливіше сьогодні

Зроби дві версії:

### Version A

```python
def group_patients_by_status(...)
```

через звичайний `for`.

### Version B

Спробуй максимально використати:

* `dict`;
* `setdefault()`;
* comprehension там, де це справді читабельно.

Порівняй обидва варіанти.

Тут мене цікавитиме вже не лише **"працює / не працює"**, а **чому ти вибрав саме таку структуру даних**.

---

# 🏥 Як це пов'язано з AI/ML

Сьогоднішня концепція:

```text
Python collections
       ↓
nested data
       ↓
JSON
       ↓
API
       ↓
Pandas
       ↓
datasets
       ↓
ML preprocessing
```

Наприклад, реальний API може повернути структуру:

```python
{
    "patient": {
        "id": 101,
        "measurements": [
            {
                "type": "temperature",
                "value": 38.2,
            },
            {
                "type": "weight",
                "value": 82,
            },
        ],
    }
}
```

Тому до переходу в NumPy/Pandas потрібно **дуже добре відчувати `list` / `dict` / `tuple` / `set`**.

---
