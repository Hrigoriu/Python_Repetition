# День 4 — Умови та логічне мислення в Python

Сьогодні переходимо від роботи з даними до **прийняття рішень програмою**.

З огляду на твої результати за перші 3 дні, базовий рівень пропускаємо швидко й одразу будуємо фундамент для подальшої роботи з **ML/AI-логікою**.

## 🎯 Цілі Дня 4

Ти маєш впевнено використовувати:

* `if`
* `elif`
* `else`
* `>`, `<`, `>=`, `<=`, `==`, `!=`
* `and`
* `or`
* `not`
* truthy / falsy
* вкладені умови
* тернарний оператор
* `match/case`
* guard clauses
* складні Boolean expressions

---

# 1. Порівняння

```python
age = 42

print(age > 18)
print(age < 18)
print(age == 42)
print(age != 30)
print(age >= 40)
print(age <= 50)
```

Результат кожного порівняння — `bool`:

```python
True
False
True
True
True
True
```

---

# 2. `if`

Найпростіше рішення:

```python
age = 42

if age >= 18:
    print("Adult")
```

Схема:

```text
             age >= 18?
                │
          ┌─────┴─────┐
         True        False
          │             │
        print          нічого
```

---

# 3. `if / else`

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

# 4. `if / elif / else`

```python
temperature = 38.5

if temperature >= 39:
    print("High fever")
elif temperature >= 38:
    print("Fever")
else:
    print("Normal")
```

Python перевіряє умови **зверху вниз** і виконує першу істинну.

---

# 5. Логічні оператори

## `and`

Обидві умови повинні бути `True`.

```python
age = 42
has_license = True

if age >= 18 and has_license:
    print("Allowed")
```

---

## `or`

Достатньо однієї істинної умови.

```python
temperature = 38.5
has_cough = True

if temperature >= 38 or has_cough:
    print("Possible infection")
```

---

## `not`

Заперечення.

```python
is_empty = False

if not is_empty:
    print("Data available")
```

---

# 6. Truthy / Falsy

У Python не обов'язково писати:

```python
if name != "":
```

Можна:

```python
if name:
    print("Name entered")
```

Порожні значення зазвичай `False`:

```python
False
None
0
0.0
""
[]
{}
set()
```

Наприклад:

```python
name = ""

if not name:
    print("Name is empty")
```

---

# 7. Дуже важлива різниця

```python
if age == 18:
```

означає **порівняння**.

А:

```python
age = 18
```

означає **присвоювання**.

Це одна з найпоширеніших помилок початківців.

---

# 8. Складні умови

Наприклад, оцінка BMI:

```python
bmi = 24.5

if bmi >= 18.5 and bmi < 25:
    print("Normal")
```

Можна записати Pythonic-варіант:

```python
if 18.5 <= bmi < 25:
    print("Normal")
```

Це називається **chained comparison**.

---

# 9. Медичний приклад

```python
temperature = 38.7
cough = True
sore_throat = True

if temperature >= 38 and cough and sore_throat:
    print("Symptoms require attention")
```

Тут три умови повинні бути `True`.

---

# 10. Вкладені `if`

Можна робити:

```python
age = 42
has_symptoms = True

if age >= 18:
    if has_symptoms:
        print("Adult with symptoms")
```

Але часто краще:

```python
if age >= 18 and has_symptoms:
    print("Adult with symptoms")
```

### Правило

Не створюй вкладені `if`, якщо їх можна зробити простішою логічною умовою.

---

# 11. Guard Clause

Дуже корисна практика.

Замість:

```python
def process_patient(patient):
    if patient:
        if patient.age > 0:
            ...
```

можна:

```python
def process_patient(patient):
    if not patient:
        return

    if patient.age <= 0:
        return

    ...
```

Це зменшує вкладеність.

---

# 12. Тернарний оператор

Замість:

```python
if age >= 18:
    category = "adult"
else:
    category = "minor"
```

можна:

```python
category = "adult" if age >= 18 else "minor"
```

Не варто використовувати його для складної логіки.

---

# 13. `match / case`

Сучасний Python має pattern matching.

```python
status = "critical"

match status:
    case "normal":
        print("Normal")
    case "warning":
        print("Warning")
    case "critical":
        print("Critical")
    case _:
        print("Unknown")
```

`_` означає "будь-який інший випадок".

Це особливо зручно, коли є багато дискретних варіантів.

---

# 14. `match` із кількома варіантами

```python
status = "fever"

match status:
    case "fever" | "cough":
        print("Respiratory symptom")
    case "pain":
        print("Pain")
    case _:
        print("Other")
```

---

# 15. Boolean expressions

Розглянемо:

```python
age = 42
has_symptoms = True
temperature = 38.5
```

Умова:

```python
age >= 18 and (temperature >= 38 or has_symptoms)
```

Спочатку Python обчислює:

```text
age >= 18
        ↓
      True

temperature >= 38
        ↓
      True

True or True
        ↓
      True

True and True
        ↓
      True
```

---

# Практика №1 — базові умови

Створи:

```python
age = 42
```

Напиши програму, яка визначає:

```text
< 18       → Minor
18–64      → Adult
65+        → Senior
```

---

# Практика №2 — BMI

Створи:

```python
bmi = 27.4
```

Визнач категорію:

```text
< 18.5       Underweight
18.5–24.9    Normal
25–29.9      Overweight
30+          Obesity
```

**Важливо:** зроби межі без перекриттів.

---

# Практика №3 — температура

Користувач вводить температуру.

Програма повинна визначити:

```text
< 36.0        Low
36.0–37.4     Normal
37.5–38.9     Fever
39+           High fever
```

Не забудь перетворити `input()` у `float`.

---

# Практика №4 — логічні оператори

Створи:

```python
age = 42
has_id = True
is_banned = False
```

Умова доступу:

* вік ≥ 18;
* є ID;
* користувач не заблокований.

Виведи:

```text
Access granted
```

або:

```text
Access denied
```

---

# Практика №5 — медична логіка

Створи:

```python
temperature = 38.7
cough = True
sore_throat = True
```

Правило:

```text
temperature >= 38
AND
cough == True
AND
sore_throat == True
```

→

```text
Respiratory symptoms detected
```

Інакше:

```text
Criteria not met
```

---

# Практика №6 — `match/case`

Створи:

```python
severity = "moderate"
```

Використовуючи `match/case`, виведи:

```text
mild     → Low priority
moderate → Medium priority
severe   → High priority
critical → Emergency
```

---

# 🧠 Challenge №1 — співбесіда

**Не запускай код. Спочатку спрогнозуй результат.**

```python
x = 10

if x > 5 and x < 15:
    print("A")
elif x == 10:
    print("B")
else:
    print("C")
```

Що буде виведено?

І головне:

**чому `B` не буде виведено?**

---

# 🧠 Challenge №2 — Boolean Logic

Не запускаючи код, визнач результат кожного:

```python
print(bool(""))
print(bool("Python"))
print(bool(0))
print(bool(42))
print(bool([]))
print(bool([1, 2, 3]))
print(bool(None))
```

Поясни правило, за яким Python визначає `True` / `False`.

---

# 🧠 Challenge №3 — знайди помилку

Що не так?

```python
age = 17

if age = 18:
    print("Adult")
```

Виправ код.

---

# 🚀 Challenge №4 — рівень Junior+

Напиши функцію:

```python
def classify_patient(
    age: int,
    temperature: float,
    has_cough: bool,
    has_sore_throat: bool,
) -> str:
    ...
```

Вона повинна повертати:

```text
"normal"
"attention"
"high_risk"
```

Запропонуй **власні логічні правила** для класифікації.

Тут мене цікавить не медична правильність алгоритму, а саме **якість Python-логіки**.

---

# 🏥 Мініпроєкт `MedAssistant`

Сьогодні додаємо першу логіку до нашого проєкту:

```text
Patient
   │
   ├── age
   ├── temperature
   ├── cough
   └── sore_throat
          │
          ▼
     Classification
          │
     ┌────┼────┐
     ▼    ▼    ▼
  normal attention high_risk
```

Поки що **не потрібно** створювати складну архітектуру. Нам важливо відпрацювати саме умови.

---
