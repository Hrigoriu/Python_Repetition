# День 7 — функції: поглиблення + колекції + comprehension

Після Дня 6 ти вже впевнено працюєш із функціями, тому сьогодні не будемо просто повторювати `def` і `return`. Основна мета — навчитися **комбінувати функції з колекціями** та писати коротший, але читабельний Python-код.

## 🎯 Що вивчаємо сьогодні

1. List comprehension
2. Dict comprehension
3. Set comprehension
4. `map()` / `filter()`
5. Nested comprehensions
6. Функції з колекціями
7. `any()` / `all()`
8. `sorted()` + `key`
9. `Callable` у Type Hints
10. Практичні задачі для `MedAssistant`

---

# 1. List comprehension

Ти вже використовував його:

```python
squared = [x ** 2 for x in numbers]
```

Звичайний цикл:

```python
squared = []

for x in numbers:
    squared.append(x ** 2)
```

Comprehension робить ту саму операцію компактніше.

### Загальна форма

```python
[expression for item in iterable]
```

---

# 2. Comprehension + умова

```python
numbers = [1, 2, 3, 4, 5, 6]

even = [x for x in numbers if x % 2 == 0]
```

Результат:

```text
[2, 4, 6]
```

Структура:

```text
[що отримати | для кожного елемента | якщо умова]
```

---

# 3. Dict comprehension

```python
numbers = [1, 2, 3, 4]

squares = {x: x ** 2 for x in numbers}
```

Результат:

```python
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
}
```

---

# 4. Set comprehension

```python
numbers = [1, 2, 2, 3, 3, 3]

unique_squares = {x ** 2 for x in numbers}
```

Результат:

```text
{1, 4, 9}
```

---

# 5. Comprehension з функцією

Це вже безпосередньо пов'язано з Днем 6.

```python
def square(x: int) -> int:
    return x ** 2


numbers = [1, 2, 3, 4]

squares = [square(x) for x in numbers]
```

Тут:

```text
list
 ↓
for
 ↓
function
 ↓
new list
```

Це дуже важливий патерн для Data/ML.

---

# 6. `map()`

Альтернатива:

```python
squares = list(map(square, numbers))
```

Технічно це правильно.

Але:

```python
squares = [square(x) for x in numbers]
```

часто простіше читати.

---

# 7. `filter()`

```python
def is_even(x: int) -> bool:
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(is_even, numbers))
```

Або comprehension:

```python
even = [x for x in numbers if is_even(x)]
```

---

# 8. `any()`

Перевіряє, чи є **хоча б одне** `True`.

```python
temperatures = [36.6, 37.0, 38.5]

has_fever = any(temp >= 38 for temp in temperatures)
```

Результат:

```text
True
```

Це дуже корисно.

Замість:

```python
found = False

for temp in temperatures:
    if temp >= 38:
        found = True
        break
```

можна:

```python
has_fever = any(temp >= 38 for temp in temperatures)
```

---

# 9. `all()`

Перевіряє, чи **всі** значення `True`.

```python
temperatures = [36.6, 36.8, 37.0]

all_normal = all(temp < 37.5 for temp in temperatures)
```

→ `True`.

---

# 10. `any()` vs `all()`

| Функція | Сенс        |
| ------- | ----------- |
| `any()` | хоча б один |
| `all()` | усі         |

Медична аналогія:

```python
any(temp >= 38 for temp in temperatures)
```

→ чи є хоча б один пацієнт із температурою ≥ 38?

```python
all(temp < 37.5 for temp in temperatures)
```

→ чи всі пацієнти мають нормальну температуру?

---

# 11. `sorted()`

```python
temperatures = [38.1, 36.6, 39.2, 37.4]

sorted_temperatures = sorted(temperatures)

print(sorted_temperatures)
```

```text
[36.6, 37.4, 38.1, 39.2]
```

Зворотний порядок:

```python
sorted(
    temperatures,
    reverse=True,
)
```

---

# 12. `sorted()` + `key`

Це дуже важливий патерн.

Є:

```python
patients = [
    ("Ivan", 42),
    ("Olena", 35),
    ("Petro", 58),
]
```

Сортувати за віком:

```python
sorted_patients = sorted(
    patients,
    key=lambda patient: patient[1],
)
```

Результат:

```text
Olena
Ivan
Petro
```

---

# 13. Сортування через іменовану функцію

Можна:

```python
def get_age(patient: tuple[str, int]) -> int:
    return patient[1]


sorted_patients = sorted(
    patients,
    key=get_age,
)
```

Це особливо корисно, коли логіка сортування складніша.

---

# 14. `Callable`

Ти вже зустрічав функцію як аргумент.

Тепер додамо точну типізацію:

```python
from collections.abc import Callable


def apply_operation(
    value: float,
    operation: Callable[[float], float],
) -> float:
    return operation(value)
```

Це означає:

```text
operation:
float → float
```

Тобто функція повинна прийняти `float` і повернути `float`.

---

# 15. Практика з `Callable`

```python
def double(x: float) -> float:
    return x * 2


def square(x: float) -> float:
    return x ** 2
```

Тепер:

```python
apply_operation(5, double)
apply_operation(5, square)
```

---

# 16. Nested comprehension

Наприклад:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
```

Отримати всі числа:

```python
flattened = [
    number
    for row in matrix
    for number in row
]
```

Результат:

```text
[1, 2, 3, 4, 5, 6]
```

Це потужна конструкція.

Але:

> якщо comprehension стає важко читати — використовуй звичайний `for`.

**Readability > cleverness.**

---

# 17. Функція + comprehension + фільтрація

```python
def normalize_name(name: str) -> str:
    return name.strip().title()


names = [
    "ivan",
    " OLENA ",
    "petro",
]

normalized = [
    normalize_name(name)
    for name in names
]
```

Результат:

```text
["Ivan", "Olena", "Petro"]
```

Це вже типовий preprocessing pipeline.

---

# Практика №1

Створи:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

За допомогою list comprehension створи:

```text
[2, 4, 6, 8, 10]
```

---

# Практика №2

Створи:

```python
numbers = [1, 2, 3, 4, 5]
```

отримай:

```text
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25,
}
```

Використай dict comprehension.

---

# Практика №3

Є:

```python
names = [
    " Ivan ",
    "OLENA",
    " petro",
    "HANNA ",
]
```

Створи функцію:

```python
def normalize_name(name: str) -> str:
    ...
```

і сформуй новий список нормалізованих імен.

Очікувано:

```text
["Ivan", "Olena", "Petro", "Hanna"]
```

---

# Практика №4

Є:

```python
temperatures = [
    36.6,
    37.2,
    38.1,
    39.0,
    37.8,
]
```

За допомогою comprehension створи список температур ≥ `38.0`.

Очікувано:

```text
[38.1, 39.0]
```

---

# Практика №5

Використай `any()`:

Чи є в списку температура ≥ `39.0`?

```python
temperatures = [
    36.6,
    37.2,
    38.1,
    39.0,
]
```

---

# Практика №6

Використай `all()`:

Чи всі температури нижчі за `37.5`?

---

# Практика №7

Є:

```python
patients = [
    ("Ivan", 42),
    ("Olena", 35),
    ("Petro", 58),
    ("Hanna", 29),
]
```

Відсортуй пацієнтів:

1. за віком від молодшого до старшого;
2. за віком від старшого до молодшого.

Використай `sorted()` + `key`.

---

# Практика №8

Створи функцію:

```python
def apply_operation(
    value: float,
    operation: Callable[[float], float],
) -> float:
    ...
```

і застосуй:

```python
double
square
```

---

# 🧠 Challenge №1 — comprehension

Не запускаючи код, визнач результат:

```python
numbers = [1, 2, 3, 4, 5]

result = [
    x * 2
    for x in numbers
    if x % 2 == 1
]
```

---

# 🧠 Challenge №2 — `any()`

Що буде?

```python
values = [2, 4, 6, 8]

result = any(x > 5 for x in values)

print(result)
```

Поясни чому.

---

# 🧠 Challenge №3 — `all()`

```python
values = [2, 4, 6, 8]

result = all(x % 2 == 0 for x in values)

print(result)
```

---

# 🧠 Challenge №4 — `sorted()`

Що буде?

```python
patients = [
    ("Ivan", 42),
    ("Olena", 35),
    ("Petro", 58),
]

result = sorted(
    patients,
    key=lambda patient: patient[1],
)

print(result)
```

---

# 🚀 Challenge №5 — MedAssistant

Створи:

```python
def classify_temperature(temp: float) -> str:
    ...
```

з уже знайомими правилами:

```text
< 37.5 → normal
< 39.0 → fever
39+    → high_fever
```

Потім:

```python
def classify_all(
    temperatures: list[float],
) -> list[str]:
    ...
```

Функція повинна використовувати `classify_temperature()`.

Для:

```python
[
    36.6,
    38.1,
    39.2,
    37.0,
]
```

повернути:

```python
[
    "normal",
    "fever",
    "high_fever",
    "normal",
]
```

---

# 🚀 Challenge №6 — Junior+

Створи:

```python
def analyze_patients(
    patients: list[tuple[str, float]],
) -> dict:
    ...
```

Вхід:

```python
patients = [
    ("Ivan", 36.6),
    ("Olena", 38.2),
    ("Petro", 39.1),
    ("Hanna", 37.0),
]
```

Результат:

```python
{
    "normal": 2,
    "fever": 1,
    "high_fever": 1,
}
```

### Обов'язково:

`analyze_patients()` повинна використовувати:

```python
classify_temperature()
```

а не дублювати логіку температурних меж.

---

# 🔥 Challenge №7 — рівень Junior+

Створи:

```python
def get_high_risk_patients(
    patients: list[tuple[str, float]],
) -> list[str]:
    ...
```

Вона повинна повернути імена пацієнтів із температурою `>= 39.0`.

Для:

```python
[
    ("Ivan", 36.6),
    ("Olena", 38.2),
    ("Petro", 39.1),
    ("Hanna", 37.0),
    ("Dmytro", 39.5),
]
```

результат:

```python
["Petro", "Dmytro"]
```

Постарайся використати **list comprehension**.

---

# 🏥 Мініпроєкт `MedAssistant`

Після сьогоднішнього дня у нас вже вимальовується pipeline:

```text
raw data
   ↓
normalize
   ↓
classify
   ↓
filter
   ↓
aggregate
   ↓
report
```

Наприклад:

```text
temperatures
     ↓
classify_temperature()
     ↓
["normal", "fever", "high_fever"]
     ↓
analyze_temperatures()
     ↓
{"normal": 1, "fever": 1, "high_fever": 1}
```

Це дуже близько до того, як ми пізніше будемо будувати **data preprocessing pipelines** для ML.

---

# ⚠️ Важливе правило Дня 7

Не перетворюй кожну задачу на one-liner.

Наприклад:

```python
result = [f(x) for x in data if condition(x)]
```

може бути чудово.

Але якщо ти отримав:

```python
result = [
    transform(x, normalize(x))
    for x in data
    if validate(x) and condition(x) and ...
]
```

і це вже важко читати — **зупинись і напиши звичайний `for`**.

Для твого майбутнього AI/ML-коду це особливо важливо: **читабельність і тестованість важливіші за максимально короткий код**.

---
