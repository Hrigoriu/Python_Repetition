# День 3 — Рядки (`str`) у Python

Сьогодні переходимо до однієї з найважливіших тем Python. З огляду на твої результати за Дні 1–2, я одразу даю матеріал не на рівні абсолютного новачка, а **Python Junior → Junior+**.

## 🎯 Мета дня

Після уроку ти маєш впевнено працювати з:

* `str`;
* індексацією;
* slicing;
* основними string methods;
* `f-string`;
* пошуком і заміною тексту;
* очищенням введення;
* перевіркою рядків;
* Unicode;
* immutable nature `str`;
* практичною обробкою медичних текстів.

---

# 1. Що таке `str`

Рядок — це послідовність Unicode-символів.

```python
name = "Hrigoriu"
```

Перевіримо:

```python
print(type(name))
```

```text
<class 'str'>
```

Рядок може містити:

```python
name = "Hrigoriu"
city = "Kyiv"
diagnosis = "Гострий риносинусит"
```

---

# 2. Одинарні та подвійні лапки

Обидва варіанти правильні:

```python
name = "Hrigoriu"
name = 'Hrigoriu'
```

Це особливо корисно, коли всередині рядка є апостроф:

```python
text = "Пацієнт сказав: 'болить горло'"
```

або:

```python
text = 'Пацієнт сказав: "болить горло"'
```

---

# 3. Довгі рядки

```python
text = """
Пацієнт:
Вік: 42
Скарги: біль у горлі
Температура: 38.2
"""
```

---

# 4. Довжина рядка

```python
text = "Python"

print(len(text))
```

Результат:

```text
6
```

`len()` повертає кількість символів.

---

# 5. Індексація

Python використовує індексацію з **нуля**.

```python
text = "Python"
```

```text
 P  y  t  h  o  n
 0  1  2  3  4  5
```

Тому:

```python
print(text[0])
print(text[1])
print(text[5])
```

отримаємо:

```text
P
y
n
```

---

# 6. Від'ємна індексація

Можна рахувати з кінця:

```python
text = "Python"
```

```text
 P   y   t   h   o   n
-6  -5  -4  -3  -2  -1
```

Тому:

```python
print(text[-1])
```

отримаємо:

```text
n
```

---

# 7. Slicing

Це дуже важлива концепція.

```python
text[start:stop]
```

`stop` **не включається**.

```python
text = "Python"

print(text[0:2])
```

Результат:

```text
Py
```

---

### Приклади

```python
text[:3]
```

```text
Pyt
```

```python
text[2:]
```

```text
thon
```

```python
text[:]
```

```text
Python
```

---

# 8. Step

Можна вказати третій параметр:

```python
text[start:stop:step]
```

Наприклад:

```python
text = "Python"

print(text[::2])
```

Результат:

```text
Pto
```

---

## Реверс рядка

Дуже популярна конструкція:

```python
text[::-1]
```

Наприклад:

```python
print("Python"[::-1])
```

```text
nohtyP
```

---

# 9. `upper()` / `lower()`

```python
text = "Python"

print(text.upper())
print(text.lower())
```

Результат:

```text
PYTHON
python
```

---

# 10. `capitalize()` та `title()`

```python
text = "medical artificial intelligence"

print(text.capitalize())
print(text.title())
```

---

# 11. `strip()`

Дуже важливий метод для роботи з `input()`.

```python
name = "   Hrigoriu   "

print(name.strip())
```

Результат:

```text
Hrigoriu
```

Є також:

```python
lstrip()
rstrip()
```

---

# 12. `replace()`

```python
text = "Python is difficult"

text = text.replace("difficult", "powerful")

print(text)
```

Результат:

```text
Python is powerful
```

---

# 13. `find()`

```python
text = "Medical AI Engineer"

position = text.find("AI")

print(position)
```

Результат:

```text
8
```

Якщо підрядок не знайдений:

```python
text.find("Python")
```

поверне:

```text
-1
```

---

# 14. `in`

Часто краще використовувати:

```python
if "AI" in text:
    print("Found")
```

Наприклад:

```python
diagnosis = "Гострий бактеріальний риносинусит"

if "бактеріальний" in diagnosis:
    print("Виявлено ключове слово")
```

---

# 15. `startswith()` / `endswith()`

```python
filename = "patient_data.csv"

print(filename.startswith("patient"))
print(filename.endswith(".csv"))
```

---

# 16. `split()`

Один із найважливіших методів для Data/AI.

```python
text = "Python AI Machine Learning"

words = text.split()

print(words)
```

Результат:

```python
['Python', 'AI', 'Machine', 'Learning']
```

Можна вказати роздільник:

```python
data = "Ivan,42,Kyiv"

print(data.split(","))
```

---

# 17. `join()`

Зворотна операція.

```python
words = ["Python", "AI", "Engineer"]

text = " ".join(words)

print(text)
```

Результат:

```text
Python AI Engineer
```

---

# 18. `count()`

```python
text = "Python is powerful"

print(text.count("o"))
```

---

# 19. `isdigit()`, `isalpha()`, `isalnum()`

Це корисно при валідації.

```python
value = "123"

print(value.isdigit())
```

```text
True
```

А:

```python
value = "42kg"

print(value.isdigit())
```

```text
False
```

---

# 20. Важлива властивість `str`

Рядки **immutable**.

Тобто:

```python
text = "Python"
```

не можна зробити:

```python
text[0] = "J"
```

Це викличе:

```text
TypeError
```

Замість цього:

```python
text = "J" + text[1:]

print(text)
```

```text
Jython
```

Або:

```python
text = text.replace("P", "J")
```

---

# 21. F-string

Ти вже використовував їх у попередніх завданнях.

```python
name = "Hrigoriu"
age = 42

message = f"Мене звати {name}, мені {age} років."

print(message)
```

Це **основний сучасний спосіб** форматування рядків у Python.

---

## Форматування чисел

```python
bmi = 25.67891

print(f"BMI: {bmi:.1f}")
```

Результат:

```text
BMI: 25.7
```

---

## Відсотки

```python
accuracy = 0.9567

print(f"Accuracy: {accuracy:.2%}")
```

```text
Accuracy: 95.67%
```

Це стане дуже корисним у Machine Learning.

---

# 22. Unicode

Python чудово працює з українською мовою:

```python
text = "Отоларингологія — штучний інтелект"
```

Можна отримати Unicode-код:

```python
print(ord("А"))
```

А назад:

```python
print(chr(1040))
```

---

# Практика №1

Створи:

```python
text = "Artificial Intelligence"
```

Виведи:

1. довжину;
2. перший символ;
3. останній символ;
4. перші 5 символів;
5. останні 5 символів;
6. рядок у зворотному порядку.

---

# Практика №2

Створи:

```python
diagnosis = "   Гострий бактеріальний риносинусит   "
```

Виконай:

* прибери пробіли;
* переведи в lowercase;
* заміни `"бактеріальний"` на `"вірусний"`;
* перевір, чи містить рядок `"риносинусит"`.

---

# Практика №3

Є:

```python
full_name = "Hrigoriu Ivanov"
```

Отримай окремо:

```text
First name
Last name
```

Використай `split()`.

---

# Практика №4

Є список:

```python
words = ["Python", "AI", "Computer", "Vision"]
```

Створи з нього:

```text
Python → AI → Computer → Vision
```

Використай `join()`.

---

# Практика №5

Створи медичний звіт:

```python
patient = "Ivan"
age = 42
diagnosis = "Acute sinusitis"
bmi = 25.678
```

За допомогою **одного f-string** сформуй:

```text
Patient: Ivan
Age: 42
Diagnosis: Acute sinusitis
BMI: 25.7
```

---

# Challenge — рівень Junior+

## Medical Text Analyzer

Напиши функцію:

```python
def analyze_medical_text(text: str) -> None:
    ...
```

Вона повинна:

1. прибрати зайві пробіли;
2. показати кількість символів;
3. показати кількість слів;
4. перевести текст у lowercase;
5. перевірити наявність слів:

```text
pain
fever
cough
sinusitis
```

6. показати, які з них знайдені.

Наприклад:

```text
Вхід:
" Patient complains of fever and sinusitis. "

Результат:

Characters: 45
Words: 7
Found:
- fever
- sinusitis
```

---

# 🧠 Challenge №2 — співбесіда

Не запускаючи код, спрогнозуй результат:

```python
text = "Python"

print(text[1:5])
print(text[-3:])
print(text[::-1])
print("py" in text.lower())
```

І поясни **кожен результат**.

---

# Мініпроєкт `MedAssistant`

Сьогодні додаємо до нашого проєкту **медичний текстовий модуль**.

Наприклад:

```python
class MedicalNote:
    def __init__(self, text: str):
        self.text = text.strip()

    @property
    def word_count(self) -> int:
        return len(self.text.split())
```

Поки що не потрібно робити повноцінний клас. Це буде поступово розвиватися протягом наступних днів.

---
