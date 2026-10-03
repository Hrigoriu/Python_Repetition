# День 5 — Цикли та ітерації в Python

Сьогодні переходимо від **умов** до **повторення дій**. Це фундамент для обробки масивів даних, циклів у preprocessing та подальшої роботи з Pandas/NumPy.

Твій рівень після Дня 4 дозволяє одразу працювати не лише з простим `for`, а й із Pythonic-підходами.

## 🎯 Мета Дня 5

Після уроку ти маєш впевнено розуміти:

* `for`
* `while`
* `range()`
* `break`
* `continue`
* `else` у циклах
* вкладені цикли
* `enumerate()`
* `zip()`
* `reversed()`
* `sum()`, `min()`, `max()`
* коли використовувати `for`, а коли `while`

---

# 1. Цикл `for`

Найпростіший приклад:

```python
for number in [1, 2, 3, 4, 5]:
    print(number)
```

Python бере елементи **по одному**:

```text
1
2
3
4
5
```

---

# 2. `range()`

Найчастіше `for` використовується разом із `range()`.

```python
for number in range(5):
    print(number)
```

Результат:

```text
0
1
2
3
4
```

### Важливо

`range(5)` означає:

```text
0 ... 4
```

верхня межа **не включається**.

---

## `range(start, stop)`

```python
for number in range(2, 6):
    print(number)
```

```text
2
3
4
5
```

---

## `range(start, stop, step)`

```python
for number in range(0, 10, 2):
    print(number)
```

```text
0
2
4
6
8
```

---

# 3. Цикл по рядку

```python
word = "Python"

for char in word:
    print(char)
```

Цикл проходить по кожному символу.

Це безпосередньо пов'язано з тим, що ми вивчали на День 3.

---

# 4. Цикл по списку

```python
symptoms = ["fever", "cough", "pain"]

for symptom in symptoms:
    print(symptom)
```

---

# 5. `while`

`while` виконує код, **поки умова True**.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Результат:

```text
1
2
3
4
5
```

---

# 6. `for` чи `while`?

### `for`

Коли ти знаєш, що потрібно пройти по колекції або певній кількості елементів:

```python
for patient in patients:
    ...
```

### `while`

Коли повторення залежить від умови:

```python
while password != "secret":
    ...
```

---

# 7. `break`

Негайно припиняє цикл.

```python
for number in range(10):
    if number == 5:
        break

    print(number)
```

Результат:

```text
0
1
2
3
4
```

---

# 8. `continue`

Пропускає поточну ітерацію.

```python
for number in range(5):
    if number == 2:
        continue

    print(number)
```

Результат:

```text
0
1
3
4
```

---

# 9. `else` у циклі

Цікава конструкція Python:

```python
for number in range(5):
    print(number)
else:
    print("Finished")
```

`else` виконається, якщо цикл завершився **нормально**.

Але:

```python
for number in range(5):
    if number == 2:
        break
else:
    print("Finished")
```

Тут `else` **не виконається**, бо був `break`.

Це часто використовують для пошуку.

---

# 10. Пошук пацієнта

```python
patients = ["Ivan", "Olena", "Petro"]

for patient in patients:
    if patient == "Olena":
        print("Patient found")
        break
```

---

# 11. `enumerate()`

Не потрібно робити:

```python
index = 0

for patient in patients:
    print(index, patient)
    index += 1
```

Pythonic:

```python
for index, patient in enumerate(patients):
    print(index, patient)
```

Результат:

```text
0 Ivan
1 Olena
2 Petro
```

Можна почати з `1`:

```python
for index, patient in enumerate(patients, start=1):
    print(index, patient)
```

```text
1 Ivan
2 Olena
3 Petro
```

---

# 12. `zip()`

Дозволяє проходити кілька послідовностей одночасно.

```python
names = ["Ivan", "Olena", "Petro"]
ages = [42, 35, 28]

for name, age in zip(names, ages):
    print(name, age)
```

Результат:

```text
Ivan 42
Olena 35
Petro 28
```

Це дуже важливо для подальшої роботи з даними.

---

# 13. `reversed()`

```python
numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number)
```

```text
5
4
3
2
1
```

---

# 14. Вкладені цикли

```python
for patient in range(3):
    for symptom in range(2):
        print(patient, symptom)
```

Це дає комбінації:

```text
0 0
0 1
1 0
1 1
2 0
2 1
```

Вкладені цикли потрібні, наприклад, для роботи з двовимірними структурами.

---

# 15. `sum()`, `min()`, `max()`

Не завжди потрібно писати цикл вручну.

```python
temperatures = [36.6, 37.2, 38.5, 39.0]

print(sum(temperatures))
print(min(temperatures))
print(max(temperatures))
```

Для середнього:

```python
average = sum(temperatures) / len(temperatures)
```

---

# 16. Дуже важливий Pythonic принцип

Не роби так:

```python
numbers = [1, 2, 3, 4, 5]

total = 0

for number in numbers:
    total += number
```

коли завдання просто знайти суму.

Краще:

```python
total = sum(numbers)
```

Це коротше та виразніше.

Але цикл потрібно розуміти, тому що `sum()` не замінює всю логіку обробки.

---

# 17. `break` + `continue`

Наприклад, обробляємо температури:

```python
temperatures = [36.6, 37.2, 38.5, 40.1, 35.8]

for temperature in temperatures:
    if temperature < 36:
        continue

    if temperature >= 40:
        print("Critical:", temperature)
        break

    print("Process:", temperature)
```

---

# Практика №1 — `for`

Створи:

```python
numbers = [2, 4, 6, 8, 10]
```

За допомогою `for` виведи кожне число.

---

# Практика №2 — `range()`

Виведи всі числа від `1` до `20`, які діляться на `2`.

Очікувано:

```text
2
4
6
...
20
```

---

# Практика №3 — сума

Створи:

```python
numbers = [5, 10, 15, 20, 25]
```

Знайди:

* суму;
* мінімум;
* максимум;
* середнє арифметичне.

Використай `sum()`, `min()`, `max()` там, де це доцільно.

---

# Практика №4 — пошук

Є:

```python
patients = [
    "Ivan",
    "Olena",
    "Petro",
    "Hanna",
]
```

Знайди `"Petro"` за допомогою циклу.

Після знаходження:

```text
Patient found
```

і припини цикл.

---

# Практика №5 — `enumerate()`

Виведи список пацієнтів так:

```text
1. Ivan
2. Olena
3. Petro
4. Hanna
```

Використай саме `enumerate()`.

---

# Практика №6 — `zip()`

Маємо:

```python
names = ["Ivan", "Olena", "Petro"]
temperatures = [36.6, 38.2, 37.4]
```

Виведи:

```text
Ivan → 36.6 °C
Olena → 38.2 °C
Petro → 37.4 °C
```

Використай `zip()`.

---

# Практика №7 — `while`

Напиши програму, яка просить користувача ввести пароль.

Правильний пароль:

```text
Python2026
```

Поки пароль неправильний:

```text
Wrong password
```

Коли правильний:

```text
Access granted
```

---

# Практика №8 — `continue`

Маємо:

```python
temperatures = [36.6, 35.8, 37.2, 38.1, 39.2, 34.9]
```

Пропусти всі значення `< 36.0`.

Для інших виведи:

```text
Temperature: ...
```

---

# 🧠 Challenge №1 — співбесіда

Не запускаючи код, скажи результат:

```python
for number in range(5):
    if number == 3:
        break
    print(number)
else:
    print("Finished")
```

Питання:

**Чому `Finished` не виводиться?**

---

# 🧠 Challenge №2

Що буде?

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        continue

    print(number)
```

---

# 🧠 Challenge №3

Знайди помилку:

```python
count = 1

while count <= 5:
    print(count)
```

Що станеться при запуску?

Як це виправити?

---

# 🚀 Challenge №4 — `MedAssistant`

Створи:

```python
temperatures = [
    36.6,
    37.2,
    38.1,
    39.0,
    37.8,
    36.4,
]
```

Програма повинна пройти по всіх температурах і визначити:

```text
< 37.5      → Normal
37.5–38.9   → Fever
39+         → High fever
```

Приклад:

```text
36.6 → Normal
37.2 → Normal
38.1 → Fever
39.0 → High fever
37.8 → Fever
36.4 → Normal
```

---

# 🏥 Challenge №5 — Junior+

Створи:

```python
patients = [
    ("Ivan", 36.6),
    ("Olena", 38.2),
    ("Petro", 39.1),
    ("Hanna", 37.0),
]
```

Використовуючи `for` та `enumerate()`, виведи таблицю:

```text
#   Patient   Temperature   Status
1   Ivan      36.6          Normal
2   Olena     38.2          Fever
3   Petro     39.1          High fever
4   Hanna     37.0          Normal
```

Тут тобі доведеться одночасно використати:

```text
enumerate()
for
if / elif / else
f-string
```

---

# 🚀 Challenge №6 — логіка пошуку

Є:

```python
patients = [
    "Ivan",
    "Olena",
    "Petro",
    "Hanna",
]
```

Користувач вводить ім'я.

Програма повинна:

* пройти список;
* знайти пацієнта;
* вивести `"Patient found"`;
* використати `break`;
* якщо пацієнта немає — вивести `"Patient not found"`.

**Підказка:** тут дуже добре підходить `for ... else`.

---

# Що маєш запам'ятати сьогодні

```text
for       → пройти колекцію / задану кількість разів
while     → повторювати, поки умова True
break     → повністю зупинити цикл
continue  → перейти до наступної ітерації
enumerate → отримати індекс + значення
zip       → обробляти кілька послідовностей разом
```

І головне:

```python
for item in collection:
```

— це одна з найважливіших конструкцій у всьому Python.
