# 🐍 День 10 — Модулі, імпорти та організація Python-проєкту

Після Дня 9 ти вже вмієш працювати з даними на диску. Тепер наступний крок — навчитися **розділяти програму на логічні модулі**, щоб код не перетворювався на один великий `.py` файл.

Це фундамент для переходу від навчальних скриптів до нормальних Python-проєктів.

---

## 🎯 Цілі Дня 10

Сьогодні ти відпрацюєш:

* `import`;
* `from ... import ...`;
* `as`;
* власні модулі;
* `__name__`;
* `if __name__ == "__main__":`;
* повторне використання функцій між файлами;
* базову структуру Python-проєкту;
* принцип **DRY** через модулі;
* розділення **logic / data / presentation**.

---

# 1. Що таке модуль

Будь-який файл:

```text
something.py
```

може бути Python-модулем.

Наприклад:

```text
math_utils.py
```

```python
def add(a: int, b: int) -> int:
    return a + b
```

Інший файл:

```text
main.py
```

може використати його:

```python
from math_utils import add

print(add(2, 3))
```

Результат:

```text
5
```

---

# 2. `import`

Можна імпортувати весь модуль:

```python
import math

print(math.sqrt(25))
```

Тут:

```text
math
```

— модуль,

```text
sqrt
```

— функція всередині модуля.

---

# 3. `from ... import ...`

Можна імпортувати конкретну функцію:

```python
from math import sqrt

print(sqrt(25))
```

Але не треба імпортувати все підряд без необхідності.

Погана звичка:

```python
from math import *
```

Краще явно:

```python
from math import sqrt, ceil
```

---

# 4. `as`

Аліас:

```python
import math as m

print(m.sqrt(25))
```

Це особливо часто зустрічатиметься пізніше:

```python
import numpy as np
import pandas as pd
```

Тому сьогоднішня тема безпосередньо готує тебе до:

```text
NumPy
Pandas
Matplotlib
scikit-learn
PyTorch
```

---

# 5. Власний модуль

Створи:

```text
day10/
├── main.py
└── patient_utils.py
```

`patient_utils.py`:

```python
def normalize_name(name: str) -> str:
    return name.strip().title()


def is_adult(age: int) -> bool:
    return age >= 18
```

`main.py`:

```python
from patient_utils import normalize_name, is_adult

name = normalize_name("  ivan  ")

print(name)
print(is_adult(42))
```

---

# 6. `__name__`

Це одна з найважливіших концепцій дня.

Кожен Python-модуль має спеціальну змінну:

```python
__name__
```

Якщо файл запускається безпосередньо:

```bash
python main.py
```

то:

```python
__name__ == "__main__"
```

Якщо цей файл імпортується:

```python
import main
```

тоді `__name__` матиме ім'я модуля.

Тому:

```python
if __name__ == "__main__":
    main()
```

означає:

> виконуй цю частину тільки тоді, коли файл запускають безпосередньо.

---

# 7. Чому це важливо

Уявімо:

```python
# patient_utils.py

print("Loading patient module...")
```

Тепер:

```python
from patient_utils import normalize_name
```

під час імпорту виконається `print()`.

Тому executable-код краще захищати:

```python
def main():
    print("Application started")


if __name__ == "__main__":
    main()
```

Тоді при імпорті модуль просто надає свої функції.

---

# 8. Організація проєкту

Сьогодні почнемо переходити до такої структури:

```text
day10/
├── main.py
├── patient_utils.py
├── statistics_utils.py
└── data/
```

Це вже значно ближче до реального проєкту.

---

# 🏫 CLASS WORK

## Task 1 — стандартний модуль `math`

Створи `class_work_10.py`.

Використай:

```python
import math
```

та виведи:

* `sqrt(144)`;
* `ceil(4.2)`;
* `floor(4.8)`;
* `pi`.

---

## Task 2 — `from ... import`

Зроби те саме, але імпортуй конкретні функції:

```python
from math import sqrt, ceil, floor, pi
```

Порівняй синтаксис.

---

## Task 3 — власний модуль

Створи:

```text
patient_utils.py
```

з функціями:

```python
def normalize_name(name: str) -> str:
    ...


def is_adult(age: int) -> bool:
    ...


def calculate_bmi(weight: float, height: float) -> float:
    ...
```

Формула:

```text
BMI = weight / height²
```

де `height` у метрах.

---

## Task 4 — імпорт власного модуля

У `class_work_10.py`:

```python
from patient_utils import (
    normalize_name,
    is_adult,
    calculate_bmi,
)
```

Продемонструй роботу всіх трьох функцій.

---

## Task 5 — `__name__`

У `patient_utils.py` додай:

```python
print(f"Module name: {__name__}")
```

Запусти `class_work_10.py` і подивись результат.

Потім зроби:

```python
if __name__ == "__main__":
    print("patient_utils.py launched directly")
```

та поясни різницю.

---

## Task 6 — окремий модуль статистики

Створи:

```text
statistics_utils.py
```

з функціями:

```python
def average(numbers: list[float]) -> float:
    ...


def maximum(numbers: list[float]) -> float:
    ...


def minimum(numbers: list[float]) -> float:
    ...
```

Потім імпортуй їх у `class_work_10.py`.

---

## Task 7 — правильна структура

Перебудуй код так:

```text
day10/
├── class_work_10.py
├── patient_utils.py
└── statistics_utils.py
```

У `class_work_10.py` повинні залишитися переважно:

```text
imports
↓
data
↓
calls
↓
output
```

А не реалізації всіх функцій.

---

# ⚔️ CHALLENGES

## Challenge 1 — `MedAssistant` modules

Створи:

```text
day10/
├── medassistant.py
├── patient_utils.py
├── statistics_utils.py
└── data/
```

У `patient_utils.py`:

```python
def find_patient(
    patients: list[dict],
    name: str,
) -> dict | None:
    ...
```

---

У `statistics_utils.py`:

```python
def average_age(patients: list[dict]) -> float:
    ...


def average_temperature(patients: list[dict]) -> float:
    ...


def oldest_patient(patients: list[dict]) -> dict:
    ...
```

---

У `medassistant.py`:

```python
from patient_utils import find_patient
from statistics_utils import (
    average_age,
    average_temperature,
    oldest_patient,
)
```

і побудуй невеликий application.

---

# Challenge 2 — DRY

Порівняй два підходи.

### Варіант A

Все в одному файлі:

```text
medassistant.py
```

### Варіант B

```text
medassistant.py
patient_utils.py
statistics_utils.py
```

Поясни:

* де менше дублювання;
* де простіше тестувати;
* де простіше розширювати проєкт.

---

# Challenge 3 — reusable module

Створи:

```text
string_utils.py
```

з:

```python
def normalize_text(text: str) -> str:
    ...


def word_count(text: str) -> int:
    ...


def contains_keyword(text: str, keyword: str) -> bool:
    ...
```

Потім використовуй цей модуль у головній програмі.

---

# Challenge 4 — module API

Не імпортуй зайвого.

Порівняй:

```python
import patient_utils
```

і:

```python
from patient_utils import find_patient
```

та поясни, коли кожен варіант має сенс.

---

# 🔥 Challenge 5 — MedAssistant v2

Це головне завдання.

Перероби твій День 9 pipeline:

```text
JSON
 ↓
load
 ↓
statistics
 ↓
filter
 ↓
report
 ↓
save
```

у модульну структуру:

```text
day10/
├── main.py
├── patient_utils.py
├── statistics_utils.py
├── report_utils.py
└── data/
    └── medassistant_patients.json
```

### `patient_utils.py`

Робота з пацієнтами.

### `statistics_utils.py`

Статистика.

### `report_utils.py`

Генерація звітів.

### `main.py`

Лише orchestration.

Тобто:

```python
def main():
    ...
```

має читатися майже як сценарій:

```text
load patients
calculate statistics
filter patients
generate report
save report
```

Це буде твій перший маленький **модульний application**.

---

# 🏠 HOMEWORK

У `home_work_10.py` зроби власний варіант.

Обов'язкові компоненти:

```text
patient_utils.py
statistics_utils.py
report_utils.py
home_work_10.py
```

Реалізуй мінімум:

```python
load_patients()
find_patient()
filter_patients()
calculate_statistics()
generate_report()
save_report()
```

і з'єднай їх через імпорти.

---

# 🧠 80/20 Дня 10

Запам'ятай насамперед:

```python
import module
```

```python
from module import function
```

```python
import module as alias
```

```python
if __name__ == "__main__":
```

та принцип:

```text
ONE FILE
    ↓
MODULES
    ↓
SEPARATE RESPONSIBILITIES
    ↓
REUSABLE CODE
```

А для твого майбутнього AI/ML це стане:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

Тобто те, що сьогодні здається просто синтаксисом `import`, через кілька етапів стане основою твоєї роботи з **NumPy, Pandas, scikit-learn і PyTorch**.
