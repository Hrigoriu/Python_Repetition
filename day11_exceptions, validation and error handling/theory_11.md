# 🐍 День 11 — Exceptions, `try/except` та надійний Python-код

Після Дня 10 ти вже вмієш розділяти програму на модулі. Наступний логічний крок — навчитися робити ці модулі **стійкими до помилкових або неочікуваних даних**.

Сьогодні переходимо від:

```text
"код працює на правильному input"
```

до:

```text
"код коректно поводиться, коли щось пішло не так"
```

Для твого майбутнього MedTech/AI напряму це особливо важливо: файли можуть бути відсутні, JSON — пошкоджений, користувач — ввести неправильне значення, а дані — мати неочікуваний формат.

---

# 🎯 Цілі Дня 11

Після завершення дня ти повинен розуміти й уміти використовувати:

* `try`;
* `except`;
* `else`;
* `finally`;
* конкретні типи винятків;
* `raise`;
* створення власних помилок через `ValueError`, `TypeError` тощо;
* перевірку вхідних даних;
* exception handling у функціях;
* різницю між **обробити помилку** та **приховати помилку**;
* будувати надійніший `MedAssistant`.

---

# 1. Що таке exception

Розглянемо:

```python
age = int("abc")
```

Python отримає:

```text
ValueError
```

або:

```python
numbers = [1, 2, 3]
print(numbers[10])
```

отримаємо:

```text
IndexError
```

або:

```python
patient = {"name": "Ivan"}
print(patient["age"])
```

отримаємо:

```text
KeyError
```

---

# 2. Базовий `try/except`

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a number.")
```

Якщо користувач введе:

```text
42
```

код продовжиться.

Якщо:

```text
abc
```

програма не впаде з `ValueError`, а перейде в `except`.

---

# 3. Обробляй конкретні exceptions

Поганий варіант:

```python
try:
    ...
except:
    print("Something went wrong")
```

Ще гірше:

```python
try:
    ...
except Exception:
    pass
```

Ти втрачаєш інформацію про реальну проблему.

Краще:

```python
try:
    age = int(value)
except ValueError:
    print("Age must be an integer.")
```

---

# 4. Кілька `except`

```python
try:
    ...
except ValueError:
    ...
except KeyError:
    ...
except FileNotFoundError:
    ...
```

Наприклад:

```python
try:
    with open("patient.json", encoding="utf-8") as file:
        patient = json.load(file)
except FileNotFoundError:
    print("File not found.")
except json.JSONDecodeError:
    print("Invalid JSON.")
```

Це ти вже частково використовував на Дні 9.

Сьогодні потрібно **систематизувати цю тему**.

---

# 5. `else`

`else` виконується тільки тоді, коли помилки **не сталося**:

```python
try:
    age = int("42")
except ValueError:
    print("Invalid age")
else:
    print(f"Valid age: {age}")
```

Логіка:

```text
try
 ↓
error?
 ├── yes → except
 └── no  → else
```

---

# 6. `finally`

`finally` виконується **в будь-якому випадку**:

```python
try:
    file = open("patients.txt")
except FileNotFoundError:
    print("Not found")
finally:
    print("Operation finished")
```

Типовий сенс:

```text
try
 ↓
success/error
 ↓
finally → cleanup
```

З файлами більшість часу краще використовувати:

```python
with open(...) as file:
```

бо `with` вже правильно керує ресурсом.

---

# 7. `raise`

Тепер важливий перехід.

Не всі помилки виникають автоматично. Іноді **ми самі повинні повідомити, що дані некоректні**.

```python
def calculate_bmi(weight: float, height: float) -> float:
    if weight <= 0:
        raise ValueError("Weight must be greater than 0.")

    if height <= 0:
        raise ValueError("Height must be greater than 0.")

    return weight / height**2
```

Тут ми не чекаємо, поки Python випадково отримає неправильний результат.

Ми явно визначаємо правило.

---

# 8. `ValueError` vs `TypeError`

Це потрібно добре запам'ятати.

### `ValueError`

Тип правильний, значення неправильне:

```python
int("abc")
```

`"abc"` — `str`, але його неможливо перетворити на `int`.

### `TypeError`

Тип не підходить:

```python
"42" + 10
```

Тут проблема саме в типах.

---

# 9. Валідація

Наприклад:

```python
def calculate_bmi(weight: float, height: float) -> float:
    if weight <= 0:
        raise ValueError("Weight must be positive.")

    if height <= 0:
        raise ValueError("Height must be positive.")

    return weight / height**2
```

А зовнішній код:

```python
try:
    bmi = calculate_bmi(-10, 1.8)
except ValueError as error:
    print(error)
```

Це вже хороший патерн:

```text
function
   ↓
validate
   ↓
raise
   ↓
caller handles
```

---

# 10. Не плутай `raise` та `try/except`

Це принципово.

### `raise`

каже:

> «Ці дані некоректні — повідом про проблему».

### `try/except`

каже:

> «Я знаю, як поводитися з цією проблемою».

Наприклад:

```python
def calculate_bmi(weight, height):
    if weight <= 0:
        raise ValueError("Invalid weight")

    return weight / height**2
```

а зовні:

```python
try:
    bmi = calculate_bmi(-5, 1.8)
except ValueError as error:
    print(f"BMI calculation failed: {error}")
```

---

# 🏫 CLASS WORK

## Task 1 — basic ValueError

Створи:

```python
def parse_age(value: str) -> int:
    ...
```

Функція повинна:

1. перетворити рядок у `int`;
2. повернути число;
3. якщо перетворення неможливе — підняти `ValueError`.

---

## Task 2 — positive age

Розшир функцію:

```python
def parse_age(value: str) -> int:
    ...
```

Правила:

```text
"42" → 42
"0" → ValueError
"-5" → ValueError
"abc" → ValueError
```

Тобто:

```python
if age <= 0:
    raise ValueError(...)
```

---

## Task 3 — safe input

Напиши:

```python
def safe_parse_age(value: str) -> int | None:
    ...
```

Функція повинна:

* використати `try/except`;
* повернути число при успіху;
* повернути `None`, якщо input неправильний.

---

## Task 4 — several exceptions

Створи:

```python
def get_patient_age(patient: dict) -> int:
    ...
```

Протестуй:

```python
{"name": "Ivan", "age": 42}
```

```python
{"name": "Olena"}
```

```python
{"name": "Petro", "age": "61"}
```

Оброби ситуації:

* `KeyError`;
* `TypeError` або `ValueError`, де це доречно.

---

## Task 5 — `else`

Створи програму:

```text
Enter age
    ↓
try int()
    ↓
except ValueError
    ↓
else → print valid age
```

Тут важливо побачити різницю між кодом, який **може впасти**, та кодом, який виконується після успішного виконання.

---

## Task 6 — `finally`

Зроби демонстрацію:

```python
try:
    ...
except ValueError:
    ...
finally:
    print("Validation finished")
```

Перевір обидва випадки:

```text
correct input
incorrect input
```

---

# ⚔️ CHALLENGES

## Challenge 1 — robust BMI

Створи:

```python
def calculate_bmi_safe(
    weight: float,
    height: float,
) -> float:
    ...
```

Правила:

```text
weight <= 0 → ValueError
height <= 0 → ValueError
нечислові типи → TypeError
```

Повернення:

```python
float
```

---

# Challenge 2 — safe JSON loader

Створи:

```python
def load_json_safe(
    path: str,
) -> dict | list | None:
    ...
```

Оброби:

```text
FileNotFoundError
json.JSONDecodeError
OSError
```

Але не ховай усі можливі помилки під:

```python
except Exception:
```

---

# Challenge 3 — patient validator

Створи:

```python
def validate_patient(patient: dict) -> None:
    ...
```

Перевір:

```text
id
name
age
temperature
```

Наприклад:

```python
{
    "id": 1,
    "name": "Ivan",
    "age": 42,
    "temperature": 36.8,
}
```

Коректний patient → нічого не повертає.

Некоректний → `raise ValueError(...)`.

---

# Challenge 4 — controlled errors

Зроби:

```python
def find_patient(
    patients: list[dict],
    name: str,
) -> dict:
    ...
```

На відміну від Дня 10, ця версія повинна:

```text
пацієнта знайдено → return patient
не знайдено → raise ValueError
```

Потім окремо оброби помилку в `main()`.

Це дозволить тобі побачити два різні API-підходи:

```text
dict | None
```

та:

```text
dict + exception
```

---

# 🔥 Challenge 5 — MedAssistant Error Handling

Створи pipeline:

```text
JSON
 ↓
load
 ↓
validate
 ↓
process
 ↓
report
```

При цьому:

```text
missing file
      ↓
FileNotFoundError

invalid JSON
      ↓
JSONDecodeError

invalid patient
      ↓
ValueError
```

Програма **не повинна падати неконтрольовано**.

Приклад поведінки:

```text
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
```

або:

```text
MEDASSISTANT
============

Loading patients...
✗ File not found:
  data/patients.json
```

---

# 🧠 Challenge 6 — централізований error handling

Це вже складніше.

Зроби:

```python
def main() -> None:
    try:
        ...
    except FileNotFoundError:
        ...
    except json.JSONDecodeError:
        ...
    except ValueError:
        ...
```

При цьому допоміжні функції повинні **піднімати exceptions**, а не друкувати повідомлення.

Тобто:

```text
patient_utils.py
      ↓
raise ValueError
      ↓
main.py
      ↓
handle error
```

Це дуже важливий engineering pattern.

---

# 🧩 HOMEWORK

Створи:

```text
day11/
├── class_work_11.py
├── home_work_11.py
├── patient_utils.py
├── validation_utils.py
└── data/
```

У `validation_utils.py` зроби:

```python
validate_age()
validate_weight()
validate_height()
validate_temperature()
validate_patient()
```

У `patient_utils.py`:

```python
find_patient()
calculate_bmi()
```

У `home_work_11.py`:

```text
load JSON
    ↓
validate patients
    ↓
process
    ↓
generate statistics
    ↓
handle errors
    ↓
save report
```

---

# 🎯 Що я очікую від тебе сьогодні

Не намагайся зробити код максимально складним.

Головна мета Дня 11:

```text
try
except
raise
ValueError
TypeError
FileNotFoundError
JSONDecodeError
else
finally
```

і головне — розуміти **де саме повинна виникати помилка і де її потрібно обробляти**.

---

# 🔬 Зв'язок з твоїм майбутнім ML/Medical Imaging

Через кілька етапів принцип буде виглядати вже так:

```text
CT / MRI data
      ↓
load
      ↓
validate
      ↓
preprocess
      ↓
model inference
      ↓
validate output
      ↓
save prediction
```

І всюди можуть виникати:

```text
file errors
data errors
shape errors
type errors
model errors
configuration errors
```

Тому хороший AI Engineer повинен уміти не тільки написати:

```python
prediction = model(image)
```

а й продумати:

```text
Що буде, якщо image відсутнє?
Що буде, якщо формат неправильний?
Що буде, якщо shape не той?
Що буде, якщо model повернула некоректний результат?
```

Саме це ми починаємо тренувати на **Дні 11**.

## ✅ Результат Дня 11

До завершення дня ти повинен перейти від:

```text
"Я знаю try/except"
```

до:

```text
"Я вмію проєктувати контроль помилок у Python-програмі."
```
