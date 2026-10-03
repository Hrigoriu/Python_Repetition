# 🐍 День 9 — Файли, JSON та обробка даних

Сьогодні переходимо від роботи з даними **в пам’яті** до роботи з даними, які потрібно **зберігати, завантажувати та передавати між програмами**.

Це важливий етап перед `NumPy → Pandas → ML`, тому що в реальних AI/ML-проєктах дані майже ніколи не існують лише як змінні Python.

## 🎯 Цілі Дня 9

Після сьогоднішньої практики ти повинен уміти:

1. працювати з файлами через `open()`;
2. використовувати `with open(...)`;
3. читати та записувати `.txt`;
4. розуміти режими `r`, `w`, `a`;
5. працювати з `pathlib`;
6. читати та записувати JSON;
7. перетворювати JSON ↔ Python `dict/list`;
8. обробляти помилки при роботі з файлами;
9. будувати простий pipeline **load → process → save**.

---

# 1. Теорія 80/20

## 1.1. Відкриття файлу

```python
file = open("patients.txt", "r")
content = file.read()
file.close()
```

Працює, але вручну викликати `close()` — не найкраща практика.

Правильний варіант:

```python
with open("patients.txt", "r") as file:
    content = file.read()
```

Після завершення блоку файл автоматично закриється.

---

# 2. Режими файлів

| Режим | Значення                |
| ----- | ----------------------- |
| `r`   | читання                 |
| `w`   | запис, перезаписує файл |
| `a`   | додавання в кінець      |
| `r+`  | читання + запис         |

Приклад:

```python
with open("patients.txt", "w") as file:
    file.write("Ivan\n")
    file.write("Olena\n")
```

Додавання:

```python
with open("patients.txt", "a") as file:
    file.write("Petro\n")
```

---

# 3. Читання файлу

### `read()`

```python
with open("patients.txt", "r") as file:
    content = file.read()

print(content)
```

### `readlines()`

```python
with open("patients.txt", "r") as file:
    patients = file.readlines()

print(patients)
```

Результат приблизно:

```python
["Ivan\n", "Olena\n", "Petro\n"]
```

Тому часто використовують:

```python
patients = [line.strip() for line in file]
```

---

# 4. `pathlib`

Для сучасного Python рекомендую поступово звикати до:

```python
from pathlib import Path

path = Path("patients.txt")

print(path.exists())
print(path.name)
print(path.suffix)
```

Створення:

```python
path.write_text("Ivan\nOlena\nPetro\n", encoding="utf-8")
```

Читання:

```python
content = path.read_text(encoding="utf-8")
```

Це дуже корисно для майбутніх ML-проєктів, де з'являться:

```text
data/
models/
results/
logs/
configs/
```

---

# 5. JSON — дуже важлива тема

JSON часто використовується для:

* конфігурацій;
* API;
* metadata;
* збереження структурованих даних;
* передачі даних між системами.

Наприклад:

```json
{
    "name": "Ivan",
    "age": 45,
    "diagnoses": [
        "rhinitis",
        "sinusitis"
    ]
}
```

У Python це:

```python
{
    "name": "Ivan",
    "age": 45,
    "diagnoses": ["rhinitis", "sinusitis"]
}
```

---

# 6. `json.dumps()` та `json.loads()`

Python → JSON:

```python
import json

patient = {
    "name": "Ivan",
    "age": 45,
    "diagnoses": ["rhinitis", "sinusitis"],
}

json_string = json.dumps(patient, indent=4)

print(json_string)
```

JSON → Python:

```python
data = json.loads(json_string)

print(data["name"])
```

---

# 7. Робота з JSON-файлом

### Запис

```python
import json

patient = {
    "name": "Ivan",
    "age": 45,
    "diagnoses": ["rhinitis", "sinusitis"],
}

with open("patient.json", "w", encoding="utf-8") as file:
    json.dump(patient, file, indent=4, ensure_ascii=False)
```

### Читання

```python
with open("patient.json", "r", encoding="utf-8") as file:
    patient = json.load(file)

print(patient["name"])
```

### Важливий момент

```python
ensure_ascii=False
```

дозволяє нормально зберігати український текст:

```python
{
    "name": "Іван",
    "diagnosis": "Гайморит"
}
```

---

# 8. Обробка помилок

Під час роботи з файлами помилки — нормальна ситуація.

Наприклад:

```python
try:
    with open("unknown.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("Файл не знайдено")
```

Для JSON:

```python
try:
    with open("patient.json", "r", encoding="utf-8") as file:
        patient = json.load(file)
except FileNotFoundError:
    print("Файл не знайдено")
except json.JSONDecodeError:
    print("Некоректний JSON")
```

Це вже важлива частина production-oriented Python.

---

# 🧠 Практика

Створи папку:

```text
day09/
```

Всередині:

```text
day09/
├── class_work_09.py
├── home_work_09.py
└── data/
```

---

# 🏫 CLASS WORK

## Task 1 — створення текстового файлу

Створи `patients.txt`:

```text
Ivan
Olena
Petro
Hanna
Andrii
```

Прочитай його через `with open()` та виведи весь вміст.

---

## Task 2 — список пацієнтів

Прочитай `patients.txt` і сформуй:

```python
patients = ["Ivan", "Olena", "Petro", "Hanna", "Andrii"]
```

Не повинно бути `\n`.

Підказка:

```python
line.strip()
```

---

## Task 3 — статистика

На основі `patients.txt` визнач:

* кількість пацієнтів;
* найдовше ім'я;
* найкоротше ім'я.

Очікувано:

```text
Patients: 5
Longest name: Andrii
Shortest name: Ivan
```

---

## Task 4 — append

Додай до існуючого файлу:

```text
Sofia
Mykola
```

Після цього прочитай файл ще раз.

---

## Task 5 — JSON patient

Створи:

```python
patient = {
    "id": 101,
    "name": "Ivan",
    "age": 42,
    "diagnoses": [
        "sinusitis",
        "rhinitis"
    ],
    "is_active": True
}
```

Збережи його в:

```text
data/patient.json
```

---

## Task 6 — JSON reading

Завантаж `patient.json` назад у Python.

Виведи:

```text
Patient: Ivan
Age: 42
Diagnoses: sinusitis, rhinitis
Active: True
```

---

## Task 7 — JSON collection

Створи файл:

```text
data/patients.json
```

з масивом:

```json
[
    {
        "id": 1,
        "name": "Ivan",
        "age": 42
    },
    {
        "id": 2,
        "name": "Olena",
        "age": 35
    },
    {
        "id": 3,
        "name": "Petro",
        "age": 51
    }
]
```

Завантаж його Python та:

1. порахуй кількість пацієнтів;
2. знайди середній вік;
3. знайди найстаршого;
4. виведи список імен.

---

# ⚔️ CHALLENGES

## Challenge 1 — Patient Search from JSON

Створи функцію:

```python
def find_patient(
    patients: list[dict],
    name: str,
) -> dict | None:
    ...
```

Вона повинна знаходити пацієнта за ім'ям.

Наприклад:

```python
patient = find_patient(patients, "Olena")
```

Результат:

```python
{
    "id": 2,
    "name": "Olena",
    "age": 35
}
```

Якщо пацієнта немає:

```python
None
```

---

# Challenge 2 — JSON update

Завантаж:

```text
patients.json
```

Зміни вік:

```text
Ivan → 43
```

та збережи файл назад.

Тут важливий pipeline:

```text
JSON file
    ↓
load
    ↓
Python objects
    ↓
modify
    ↓
dump
    ↓
JSON file
```

---

# Challenge 3 — filtering

Знайди всіх пацієнтів:

```text
age >= 40
```

Очікуваний результат:

```python
[
    {"id": 1, "name": "Ivan", "age": 43},
    {"id": 3, "name": "Petro", "age": 51},
]
```

---

# Challenge 4 — statistics report

Створи файл:

```text
data/report.txt
```

Приблизний результат:

```text
PATIENT REPORT
==============

Total patients: 3
Average age: 43.0
Oldest patient: Petro
Oldest age: 51
```

---

# Challenge 5 — error handling

Напиши функцію:

```python
def load_json(path: str) -> dict | list | None:
    ...
```

Вона повинна коректно обробляти:

```text
FileNotFoundError
JSONDecodeError
```

та повертати:

```python
None
```

у випадку помилки.

---

# 🔥 Challenge 6 — MedAssistant Data Pipeline

Це головне завдання дня.

Створи:

```text
data/medassistant_patients.json
```

з пацієнтами:

```python
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
```

Програма повинна:

```text
load JSON
   ↓
calculate statistics
   ↓
filter patients
   ↓
generate report
   ↓
save report
```

Звіт повинен містити:

* кількість пацієнтів;
* середній вік;
* середню температуру;
* пацієнтів із температурою `>= 38.0`;
* пацієнтів із `sinusitis`.

---

# 🧩 Структура коду

Прагни поступово перейти до такої архітектури:

```python
def load_patients(path):
    ...


def save_report(path, report):
    ...


def calculate_statistics(patients):
    ...


def filter_by_temperature(patients, threshold):
    ...


def main():
    ...


if __name__ == "__main__":
    main()
```

Це важливий крок: ми вже починаємо будувати не просто набір вправ, а **структурований Python application**.

---

# 🏠 HOMEWORK

У `home_work_09.py` зроби власну версію:

### 1.

Функція:

```python
load_json()
```

### 2.

Функція:

```python
save_json()
```

### 3.

Функція:

```python
find_patient()
```

### 4.

Функція:

```python
get_patients_by_diagnosis()
```

### 5.

Функція:

```python
get_average_age()
```

### 6.

Функція:

```python
generate_report()
```

### 7.

Фінальна програма:

```text
MedAssistant
     ↓
Load patients
     ↓
Search / Filter
     ↓
Statistics
     ↓
Generate report
     ↓
Save JSON + TXT
```

---

# 📌 Що сьогодні потрібно запам'ятати

Для твого майбутнього AI/ML шляху найважливіші 20%:

```python
with open(...)
```

```python
Path(...)
```

```python
json.load(...)
```

```python
json.dump(...)
```

```python
try / except
```

і головний pipeline:

```text
FILE
 ↓
LOAD
 ↓
PYTHON DATA
 ↓
PROCESS
 ↓
SAVE
```

Саме цей принцип пізніше повториться у значно складніших формах:

```text
CSV
 ↓
Pandas DataFrame
 ↓
cleaning
 ↓
feature engineering
 ↓
ML model
 ↓
prediction
 ↓
saved results
```
