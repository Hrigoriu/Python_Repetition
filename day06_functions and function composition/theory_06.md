# День 6 — Функції в Python

День 5 ми завершили циклами. Тепер переходимо до однієї з **найважливіших тем Python** — функцій.

Саме функції дозволяють перейти від набору команд до **структурованого програмного коду**. Для подальшого AI/ML це критично: preprocessing, feature engineering, evaluation, inference — усе буде побудовано з функцій та їхніх композицій.

---

## 🎯 Цілі Дня 6

Сьогодні опрацюємо:

* `def`
* параметри та аргументи;
* `return`;
* локальні та глобальні змінні;
* positional / keyword arguments;
* default parameters;
* `*args`;
* `**kwargs`;
* type hints;
* docstrings;
* функції як об'єкти;
* lambda;
* функції, що приймають інші функції;
* guard clauses;
* чисті функції;
* базову композицію функцій.

---

# 1. Що таке функція?

Функція — це повторно використовуваний блок коду.

```python
def greet():
    print("Hello!")
```

Виклик:

```python
greet()
```

Результат:

```text
Hello!
```

---

# 2. Параметри

```python
def greet(name):
    print(f"Hello, {name}!")
```

Тепер:

```python
greet("Ivan")
greet("Olena")
```

Параметр:

```python
name
```

Аргумент:

```python
"Ivan"
```

---

# 3. `return`

Це фундаментально важливо.

```python
def add(a, b):
    return a + b
```

Тепер:

```python
result = add(10, 20)

print(result)
```

```text
30
```

### `print()` ≠ `return`

```python
def add(a, b):
    print(a + b)
```

Ця функція **друкує** результат.

А:

```python
def add(a, b):
    return a + b
```

**повертає** результат програмі.

---

# 4. Функція може повернути кілька значень

```python
def get_patient():
    return "Ivan", 42
```

Python фактично повертає tuple:

```python
name, age = get_patient()
```

---

# 5. Type hints

Ти вже використовував їх у попередніх днях.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Для рядка:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

Для списку:

```python
def calculate_average(values: list[float]) -> float:
    return sum(values) / len(values)
```

Type hints **не змінюють поведінку Python автоматично**. Вони допомагають:

* IDE;
* type checkers;
* читабельності;
* документації;
* командній розробці.

---

# 6. Docstring

Хороша функція повинна пояснювати своє призначення.

```python
def calculate_bmi(weight: float, height: float) -> float:
    """Calculate BMI from weight in kg and height in cm."""
    height_m = height / 100
    return weight / height_m**2
```

Побачити документацію:

```python
help(calculate_bmi)
```

---

# 7. Default parameters

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"
```

Можна:

```python
greet("Ivan")
```

або:

```python
greet("Ivan", "Good morning")
```

---

# 8. Positional arguments

```python
def patient_info(name, age):
    return f"{name}: {age}"
```

```python
patient_info("Ivan", 42)
```

Python передає:

```text
name = "Ivan"
age = 42
```

за позицією.

---

# 9. Keyword arguments

Можна явно вказати параметри:

```python
patient_info(
    name="Ivan",
    age=42,
)
```

Це часто робить код читабельнішим.

---

# 10. Positional + keyword

```python
def create_patient(name: str, age: int, city: str = "Kyiv"):
    ...
```

Можна:

```python
create_patient("Ivan", 42, city="Kyiv")
```

Але не можна бездумно міняти порядок positional/keyword аргументів.

---

# 11. `*args`

Дозволяє передати довільну кількість **позиційних аргументів**.

```python
def calculate_sum(*numbers):
    return sum(numbers)
```

Тепер:

```python
calculate_sum(1, 2)
calculate_sum(1, 2, 3, 4, 5)
```

Всередині:

```python
numbers
```

є tuple.

---

# 12. `**kwargs`

Дозволяє передати довільну кількість **іменованих аргументів**.

```python
def show_patient(**data):
    print(data)
```

Виклик:

```python
show_patient(
    name="Ivan",
    age=42,
    city="Kyiv",
)
```

Всередині:

```python
data
```

буде `dict`.

---

# 13. `*args` + `**kwargs`

```python
def debug(*args, **kwargs):
    print("ARGS:", args)
    print("KWARGS:", kwargs)
```

```python
debug(
    10,
    20,
    name="Ivan",
    age=42,
)
```

Результат концептуально:

```text
ARGS: (10, 20)
KWARGS: {'name': 'Ivan', 'age': 42}
```

---

# 14. Keyword-only parameters

Дуже корисна сучасна конструкція.

```python
def create_patient(name: str, *, age: int, city: str):
    ...
```

Тепер:

```python
create_patient(
    "Ivan",
    age=42,
    city="Kyiv",
)
```

А ось так:

```python
create_patient("Ivan", 42, "Kyiv")
```

буде помилкою.

`*` означає:

> усі параметри після нього повинні передаватися за іменем.

---

# 15. Локальні змінні

```python
def calculate():
    result = 10 + 20
    return result
```

`result` існує всередині функції.

```python
calculate()

print(result)
```

дасть:

```text
NameError
```

---

# 16. Не зловживай `global`

Поганий стиль:

```python
counter = 0

def increment():
    global counter
    counter += 1
```

Краще:

```python
def increment(counter: int) -> int:
    return counter + 1
```

Функція отримує дані → обробляє → повертає результат.

---

# 17. Чиста функція

Наприклад:

```python
def square(number: int) -> int:
    return number ** 2
```

Однаковий input:

```python
square(5)
```

завжди дає:

```text
25
```

І функція не змінює зовнішній стан.

Це **pure function**.

Такі функції особливо зручні для тестування.

---

# 18. Функція з валідацією

```python
def calculate_bmi(weight: float, height: float) -> float:
    if weight <= 0:
        raise ValueError("Weight must be positive")

    if height <= 0:
        raise ValueError("Height must be positive")

    height_m = height / 100

    return weight / height_m**2
```

Тут:

```python
raise ValueError(...)
```

явно повідомляє про неправильні вхідні дані.

---

# 19. Guard clause

Ти вже використовував цей стиль.

Замість:

```python
def process_patient(patient):
    if patient:
        if patient.age > 0:
            if patient.temperature > 0:
                ...
```

краще:

```python
def process_patient(patient):
    if not patient:
        return

    if patient.age <= 0:
        return

    if patient.temperature <= 0:
        return

    ...
```

Менше вкладеності → легше читати.

---

# 20. Lambda

Lambda — маленька анонімна функція.

```python
square = lambda x: x ** 2
```

```python
print(square(5))
```

Але якщо логіка складна:

```python
def square(x):
    return x ** 2
```

краще використовувати звичайну `def`.

---

# 21. Функції як об'єкти

У Python функцію можна передати іншій функції.

```python
def square(x):
    return x ** 2


def apply_function(value, function):
    return function(value)
```

Тепер:

```python
result = apply_function(5, square)
```

→ `25`.

Це фундамент для **higher-order functions**.

---

# 22. `map()`

Наприклад:

```python
numbers = [1, 2, 3, 4]

squared = map(lambda x: x ** 2, numbers)

print(list(squared))
```

Результат:

```text
[1, 4, 9, 16]
```

Але Pythonic-варіант часто простіший:

```python
squared = [x ** 2 for x in numbers]
```

Тобто:

> знати `map()` потрібно, але не використовувати його лише заради використання.

---

# 23. `filter()`

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(
    lambda x: x % 2 == 0,
    numbers,
)

print(list(even_numbers))
```

Результат:

```text
[2, 4, 6]
```

Але:

```python
even_numbers = [x for x in numbers if x % 2 == 0]
```

часто читати легше.

---

# Практика №1 — проста функція

Напиши:

```python
def greet(name: str) -> str:
    ...
```

яка повертає:

```text
Hello, Hrigoriu!
```

Не використовуй `print()` всередині функції.

---

# Практика №2 — математичні функції

Створи:

```python
def add(a: float, b: float) -> float:
    ...

def subtract(a: float, b: float) -> float:
    ...

def multiply(a: float, b: float) -> float:
    ...

def divide(a: float, b: float) -> float:
    ...
```

Для `divide()` передбач:

```python
ZeroDivisionError
```

або власну перевірку.

---

# Практика №3 — BMI

Створи:

```python
def calculate_bmi(
    weight: float,
    height_cm: float,
) -> float:
    ...
```

Вимоги:

* `weight > 0`;
* `height_cm > 0`;
* повернути BMI;
* результат округляти **не всередині функції**.

Наприклад:

```python
bmi = calculate_bmi(82, 180)

print(f"BMI: {bmi:.1f}")
```

---

# Практика №4 — категорія BMI

Створи окрему функцію:

```python
def bmi_category(bmi: float) -> str:
    ...
```

Вона повинна повертати:

```text
Underweight
Normal
Overweight
Obesity
```

### Важливо

Не змішуй:

```python
calculate_bmi()
```

та:

```python
bmi_category()
```

в одну функцію.

Це перше практичне тренування **separation of concerns**.

---

# Практика №5 — `*args`

Напиши:

```python
def calculate_average(*numbers: float) -> float:
    ...
```

Приклади:

```python
calculate_average(10, 20)
```

→ `15`

```python
calculate_average(10, 20, 30, 40)
```

→ `25`

Якщо аргументів немає — придумай коректну поведінку.

---

# Практика №6 — `**kwargs`

Створи:

```python
def create_patient_report(**patient_data):
    ...
```

Наприклад:

```python
create_patient_report(
    name="Ivan",
    age=42,
    diagnosis="Sinusitis",
)
```

Функція повинна сформувати читабельний текстовий звіт.

---

# Практика №7 — keyword-only

Створи:

```python
def create_measurement(
    patient_name: str,
    *,
    weight: float,
    height: float,
):
    ...
```

Правильний виклик:

```python
create_measurement(
    "Ivan",
    weight=82,
    height=180,
)
```

Спробуй пояснити, **навіщо тут `*`**.

---

# Практика №8 — функція як аргумент

Створи:

```python
def apply_operation(
    value: float,
    operation,
) -> float:
    ...
```

і функції:

```python
def double(x):
    return x * 2


def square(x):
    return x ** 2
```

Потім:

```python
apply_operation(5, double)
apply_operation(5, square)
```

---

# 🧠 Challenge №1 — знайди проблему

Що не так?

```python
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / height_m ** 2
    print(bmi)


result = calculate_bmi(82, 180)

print(result)
```

Питання:

**Що буде в `result` і чому?**

Виправ функцію.

---

# 🧠 Challenge №2 — mutable default argument

Не запускай код. Спрогнозуй:

```python
def add_patient(name, patients=[]):
    patients.append(name)
    return patients


print(add_patient("Ivan"))
print(add_patient("Olena"))
print(add_patient("Petro"))
```

Який буде результат?

І головне:

**чому це небезпечний шаблон?**

---

# 🚀 Challenge №3 — Medical Text

Створи:

```python
def normalize_medical_text(text: str) -> str:
    ...
```

Функція повинна:

1. прибрати пробіли на початку/кінці;
2. перевести текст у lowercase;
3. замінити декілька пробілів одним;
4. повернути очищений текст.

Наприклад:

```text
"   Patient   has   fever   "
```

→

```text
"patient has fever"
```

Підказка: можеш використати вже знайомі тобі `strip()`, `split()` і `join()`.

---

# 🚀 Challenge №4 — `MedAssistant`

Створи три окремі функції:

```python
def calculate_bmi(weight: float, height: float) -> float:
    ...


def bmi_category(bmi: float) -> str:
    ...


def create_patient_summary(
    name: str,
    age: int,
    weight: float,
    height: float,
) -> str:
    ...
```

`create_patient_summary()` повинна використовувати **перші дві функції**, а не дублювати їхню логіку.

Приклад результату:

```text
Patient: Ivan
Age: 42
BMI: 25.3
Category: Overweight
```

Це перше завдання, де ми свідомо тренуємо:

```text
function
   ↓
function
   ↓
function
   ↓
final result
```

---

# 🧠 Challenge №5 — рівень Junior+

Створи функцію:

```python
def analyze_temperatures(
    temperatures: list[float],
) -> dict:
    ...
```

Вона повинна повернути:

```python
{
    "normal": 3,
    "fever": 2,
    "high_fever": 1,
}
```

Використовуй **окрему функцію**:

```python
classify_temperature()
```

яку ти вже створив у День 5.

Тобто цього разу ми починаємо **перевикористовувати код із попередніх днів**.

Це дуже важливий момент.

---

# 🏥 Мініпроєкт `MedAssistant`

Після Дня 6 структура нашої логіки починає виглядати так:

```text
MedAssistant
│
├── calculate_bmi()
│
├── bmi_category()
│
├── normalize_medical_text()
│
├── classify_temperature()
│
├── analyze_temperatures()
│
└── create_patient_summary()
```

Пізніше ми перенесемо ці функції в окремі модулі:

```text
medassistant/
│
├── patient.py
├── measurements.py
├── text.py
├── analysis.py
└── main.py
```

Але **сьогодні цього ще не робимо**.

---

# 🔥 Головна концепція Дня 6

Запам'ятай:

> **Хороша функція робить одну зрозумілу річ.**

Наприклад:

```python
calculate_bmi()
```

не повинна одночасно:

* рахувати BMI;
* визначати категорію;
* друкувати рамку;
* запитувати `input()`;
* записувати файл.

Краще:

```text
input
 ↓
calculate_bmi()
 ↓
bmi_category()
 ↓
create_patient_summary()
 ↓
print()
```

Це вже початок **модульного мислення**.

---
