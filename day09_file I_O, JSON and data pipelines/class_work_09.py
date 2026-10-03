"""
# !Task 1 — створення текстового файлу!

Створи patients.txt:
Ivan
Olena
Petro
Hanna
Andrii

Прочитай його через with open() та виведи весь вміст.
"""

# --- Дані для файлу ---
patient_names = ["Ivan", "Olena", "Petro", "Hanna", "Andrii"]

# --- Крок 1: створення файлу через with open() ---
# "w" — режим запису (write): якщо файл існує, ПЕРЕЗАПИШЕ його;
#       якщо не існує — СТВОРИТЬ новий
# encoding="utf-8" — на випадок кириличних імен чи символів у майбутньому
with open("data/patients.txt", "w", encoding="utf-8") as file:
    file.writelines(name + "\n" for name in patient_names)

# --- Крок 2: читання файлу через with open() ---
# "r" — режим читання (read), за замовчуванням, можна не писати явно
with open("data/patients.txt", "r", encoding="utf-8") as file:
    content = file.read()  # читає ВЕСЬ вміст файлу як ОДИН рядок

# --- Вивід прочитаного вмісту у рамці ---
lines = content.strip().split("\n")  # розбиваємо назад на окремі імена для рамки
width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  PATIENTS.TXT".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌──────────┐
│  PATIENTS.TXT│
├──────────┤
│  Ivan    │
│  Olena   │
│  Petro   │
│  Hanna   │
│  Andrii  │
└──────────┘
"""

"""
*Пояснення with open() — навіщо саме так:
with open("data/patients.txt", "w", encoding="utf-8") as file:
    file.write(...)
# файл АВТОМАТИЧНО закривається тут, навіть якщо всередині сталась помилка

*with — це контекстний менеджер: 
гарантує, що файл буде закритий, щойно код виходить із блоку with — незалежно від того, чи все пройшло успішно, чи виникла помилка (винятковий стан). Це критично важливо для файлів: незакритий файл може призвести до втрати даних (не всі записи "скинуться" на диск) або до блокування файлу для інших процесів.

# ❌ Без with — треба ВРУЧНУ закривати, легко забути:
file = open("data/patients.txt", "w")
file.write("Ivan\n")
file.close()   # якщо забудеш цей рядок — файл може лишитись "напівзаписаним"

# ✅ З with — закриття відбувається АВТОМАТИЧНО:
with open("data/patients.txt", "w") as file:
    file.write("Ivan\n")
# тут file вже гарантовано закритий, навіть без явного .close()

*Режими відкриття файлу:
Режим	        Що робить
"r" (read)	    читає файл; помилка, якщо файл не існує
"w" (write)	    створює новий АБО перезаписує існуючий файл повністю
"a" (append)	дописує в кінець існуючого файлу, не стираючи вміст

*Режим	Значення
r	    читання
w	    запис, перезаписує файл
a	    додавання в кінець
r+	    читання + запис


*Чому потрібна папка data/ перед запуском:
Твоя структура day09/class_work_09.py та day09/data/ означає, що скрипт очікує папку data/ поруч із собою. Якщо запускаєш class_work_09.py з папки day09/, шлях "data/patients.txt" спрацює коректно — Python шукає відносно поточної робочої директорії (звідки запущено скрипт), а не відносно самого файлу .py.

*⚠️ Важливо: 
переконайся, що папка data/ вже існує перед запуском, інакше open(..., "w") видасть помилку FileNotFoundError (Python не створює папки автоматично, лише файли всередині вже існуючих папок).

*Читання через .read() vs інші способи (для довідки):
content = file.read()        # ← весь вміст ОДНИМ рядком (як у цій задачі)
lines = file.readlines()      # ← список РЯДКІВ (з символами \n на кінці кожного)
for line in file:              # ← ітерація по файлу РЯДОК ЗА РЯДКОМ (найекономніша пам'ять)
    print(line.strip())
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 2 — список пацієнтів!

Прочитай patients.txt і сформуй:
patients = ["Ivan", "Olena", "Petro", "Hanna", "Andrii"]

Не повинно бути \n.

Підказка:
line.strip()
"""

# class_work_09.py (продовження)

# --- Варіант 1: list comprehension ---
with open("data/patients.txt", "r", encoding="utf-8") as file:
    patients_comprehension = [line.strip() for line in file]

# --- Варіант 2: звичайний for-цикл ---
with open("data/patients.txt", "r", encoding="utf-8") as file:
    patients_for_loop = []
    for line in file:
        patients_for_loop.append(line.strip())

# --- Вивід у рамці ---
lines = [
    f"List comprehension:  {patients_comprehension}",
    f"Звичайний for:       {patients_for_loop}",
    f"Однакові результати? {patients_comprehension == patients_for_loop}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  СПИСОК ПАЦІЄНТІВ З ФАЙЛУ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌──────────────────────────────────────────────────────────────────────┐
│                        СПИСОК ПАЦІЄНТІВ З ФАЙЛУ                      │
├──────────────────────────────────────────────────────────────────────┤
│  List comprehension:  ['Ivan', 'Olena', 'Petro', 'Hanna', 'Andrii']  │
│  Звичайний for:       ['Ivan', 'Olena', 'Petro', 'Hanna', 'Andrii']  │
│  Однакові результати? True                                           │
└──────────────────────────────────────────────────────────────────────┘
"""

"""
*Пояснення for line in file — ітерація по файлу:
with open("data/patients.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(repr(line))

Коли ти пишеш for line in file, Python автоматично читає файл рядок за рядком — не потрібно викликати .readlines() чи .read() окремо. На кожній ітерації line — це один рядок файлу, і він включає символ переносу рядка \n у кінці (крім, можливо, останнього рядка файлу):

# Файл patients.txt виглядає так (кожне ім'я на новому рядку):
# Ivan
# Olena
# Petro
# Hanna
# Andrii

# Але Python БАЧИТЬ це так (з явним \n):
"Ivan\n"
"Olena\n"
"Petro\n"
"Hanna\n"
"Andrii\n"   # (або без \n, якщо це останній рядок файлу без завершального переносу)

*Чому потрібен .strip():
line = "Ivan\n"
line.strip()   # → "Ivan"   ← прибирає \n (і зайві пробіли з країв, якщо є)

patients = ["Ivan\n", "Olena\n", ...]     # ❌ БЕЗ strip() — зайвий \n у кожному імені
patients = ["Ivan", "Olena", ...]          # ✅ З strip() — чисті імена

*Без .strip() порівняння чи пошук за іменем зламався б непомітно:
"Ivan" == "Ivan\n"   # False!  ← виглядає однаково при print(), але РІЗНІ рядки

*Порівняння двох варіантів формування списку:
# --- List comprehension — компактно ---
patients = [line.strip() for line in file]

# --- Звичайний for — те саме, довшим шляхом ---
patients = []
for line in file:
    patients.append(line.strip())

Обидва варіанти дають абсолютно однаковий результат — for line in file усередині обох підходів працює однаково, різниться лише спосіб зібрати результати (одразу в comprehension, чи через append() у циклі).

*Зв'язок із минулими задачами: 
це той самий підхід, що вже неодноразово застосовувався — [вираз for елемент in джерело], де тепер джерелом виступає не список чи range(), а сам відкритий файл. Python дозволяє ітерувати по файлу так само природно, як по будь-якій іншій послідовності.
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 3 — статистика!

На основі patients.txt визнач:
кількість пацієнтів;
найдовше ім'я;
найкоротше ім'я.

Очікувано:
Patients: 5
Longest name: Andrii
Shortest name: Ivan
"""

# class_work_09.py (продовження)

with open("data/patients.txt", "r", encoding="utf-8") as file:
    patients = [line.strip() for line in file]

# --- Варіант 1: min()/max() з key=len ---
patient_count = len(patients)
longest_name_v1 = max(patients, key=len)
shortest_name_v1 = min(patients, key=len)

# --- Варіант 2: звичайний for-цикл ---
longest_name_v2 = patients[0]     # починаємо з першого як "поточний рекорд"
shortest_name_v2 = patients[0]

for name in patients:
    if len(name) > len(longest_name_v2):
        longest_name_v2 = name
    if len(name) < len(shortest_name_v2):
        shortest_name_v2 = name

# --- Вивід у рамці ---
lines = [
    f"Кількість пацієнтів:  {patient_count}",
    f"Найдовше ім'я:        {longest_name_v1}",
    f"Найкоротше ім'я:      {shortest_name_v1}",
    "─" * 30,
    f"(перевірка через for): найдовше = {longest_name_v2}, найкоротше = {shortest_name_v2}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  СТАТИСТИКА ПАЦІЄНТІВ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌───────────────────────────────────────────────────────────────┐
│                       СТАТИСТИКА ПАЦІЄНТІВ                    │
├───────────────────────────────────────────────────────────────┤
│  Кількість пацієнтів:  5                                      │
│  Найдовше ім'я:        Andrii                                 │
│  Найкоротше ім'я:      Ivan                                   │
│  ──────────────────────────────                               │
│  (перевірка через for): найдовше = Andrii, найкоротше = Ivan  │
└───────────────────────────────────────────────────────────────┘
"""

"""
*Пояснення max()/min() з key=len:
patients = ["Ivan", "Olena", "Petro", "Hanna", "Andrii"]

max(patients, key=len)
#            ↑
#     для КОЖНОГО імені рахуємо len(ім'я),
#     і повертаємо те ім'я, де ЦЕ ЧИСЛО найбільше

# len("Ivan")=4, len("Olena")=5, len("Petro")=5, len("Hanna")=5, len("Andrii")=6
# max за len → "Andrii" (6 символів — найбільше)
# min за len → "Ivan"   (4 символи — найменше)

Це та сама ідея key, що вже зустрічалась у sorted() (Практика №7 з попереднього дня) — тільки тепер застосована до max()/min(): не порівнюємо рядки безпосередньо (що дало б алфавітний порядок), а порівнюємо результат функції len(), застосованої до кожного рядка.

max(patients)           # ⚠️ без key — порівняв би рядки АЛФАВІТНО: "Petro" (найбільша літера)
max(patients, key=len)  # ✅ з key=len — порівнює ДОВЖИНУ: "Andrii" (найбільше символів)

*Пояснення звичайного for-циклу — "пошук рекорду":
longest_name = patients[0]   # СТАРТУЄМО з першого елемента як "поточний найдовший"

for name in patients:
    if len(name) > len(longest_name):   # якщо ЗНАЙШЛИ довше за поточний рекорд
        longest_name = name              # ОНОВЛЮЄМО рекорд

# Крок за кроком:
# longest_name = "Ivan" (старт, довжина 4)
# name="Ivan":   4 > 4? Ні
# name="Olena":  5 > 4? Так → longest_name = "Olena"
# name="Petro":  5 > 5? Ні (рівно, не більше)
# name="Hanna":  5 > 5? Ні
# name="Andrii": 6 > 5? Так → longest_name = "Andrii"
# Фінал: longest_name = "Andrii"

*Чому старт саме з patients[0], а не з 0 чи "":
# ❌ Якби стартували з порожнього рядка:
longest_name = ""
for name in patients:
    if len(name) > len(longest_name):   # завжди True на першому кроці — ОК, працює
        longest_name = name
# Це теж СПРАЦЮВАЛО Б для цього завдання, але:

# ✅ Краще стартувати з РЕАЛЬНОГО елемента списку (patients[0]):
# — гарантує, що РЕЗУЛЬТАТ завжди буде ІЗ СПИСКУ, а не якимось "фіктивним" стартовим значенням
# — якщо список ПОРОЖНІЙ — краще одразу впасти з зрозумілою помилкою (IndexError на patients[0]),
#   ніж тихо повернути "" як "найдовше ім'я"

*Порівняння двох підходів:
	                max(patients, key=len)	     Звичайний for
Рядків коду	        1	                         5+
Читабельність	    ✅ одразу видно намір	    потрібно "прочитати" логіку
Що робити з 	    ValueError: max() arg	     IndexError на patients[0]
порожнім списком     is an empty sequence
Коли обирати	    стандартний випадок	         коли треба додаткова логіка всередині циклу 
                                                 (напр., рахувати щось ще одночасно)
"""

# ==============================================================================
# ==============================================================================
"""
# !1Task 4 — append!

Додай до існуючого файлу:
Sofia
Mykola

Після цього прочитай файл ще раз.
"""

new_names = ["Sofia", "Mykola"]

# --- Варіант 1: writelines() — одним блоком ---
# "a" (append) — дописує в КІНЕЦЬ файлу, НЕ стираючи наявний вміст
with open("data/patients.txt", "a", encoding="utf-8") as file:
    # writelines() приймає СПИСОК рядків і записує їх ПІДРЯД
    # ВАЖЛИВО: writelines() САМ НЕ додає \n — треба додати вручну
    file.writelines(name + "\n" for name in new_names)

# --- Варіант 2: write() — окремим викликом для кожного імені ---
# (якщо не буже закоментовано, то додасть імена ДВІЧІ — це альтернатива Варіанту 1)
with open("data/patients.txt", "a", encoding="utf-8") as file:
    for name in new_names:
        file.write(name + "\n")  # write() записує ОДИН рядок за раз, треба викликати для кожного  

# --- Читання файлу після append ---
with open("data/patients.txt", "r", encoding="utf-8") as file:
    updated_patients = [line.strip() for line in file]

# --- Вивід у рамці ---
lines = [f"{i}. {name}" for i, name in enumerate(updated_patients, start=1)]
lines.append(f"Всього: {len(updated_patients)}")

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  PATIENTS.TXT (після append)".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌─────────────┐
│  PATIENTS.TXT (після append)│
├─────────────┤
│  1. Ivan    │
│  2. Olena   │
│  3. Petro   │
│  4. Hanna   │
│  5. Andrii  │
│  6. Sofia   │
│  7. Mykola  │
│  8. Sofia   │
│  9. Mykola  │
│  Всього: 9  │
└─────────────┘
"""

"""
*Пояснення режиму "a" (append) — головна відмінність від "w":
# "w" (write) — Task 1: СТИРАЄ весь наявний вміст перед записом
with open("data/patients.txt", "w") as file:
    file.write("Ivan\n")   # якщо файл ВЖЕ мав дані — вони ЗНИКНУТЬ

# "a" (append) — Task 4: ДОПИСУЄ в кінець, наявний вміст ЗБЕРІГАЄТЬСЯ
with open("data/patients.txt", "a") as file:
    file.write("Sofia\n")   # старі імена ЗАЛИШАЮТЬСЯ, нове ДОДАЄТЬСЯ ПІСЛЯ них

*⚠️ Найпоширеніша пастка новачків: 
якщо випадково використати "w" замість "a" у Task 4, весь файл перезапишеться — і всі п'ять попередніх імен (Ivan, Olena, Petro, Hanna, Andrii) зникнуть безповоротно, залишаться лише Sofia та Mykola.

*Пояснення writelines() — компактний спосіб записати кілька рядків:
new_names = ["Sofia", "Mykola"]

file.writelines(name + "\n" for name in new_names)
#               ↑
#     генераторний вираз — те саме, що ["Sofia\n", "Mykola\n"]

# Це РІВНОЦІННО:
for name in new_names:
    file.write(name + "\n")

*⚠️ Важлива деталь: 
writelines() НЕ додає \n автоматично, на відміну від того, що можна очікувати з назви методу. 
Якщо забути + "\n", усі імена "злипнуться" в один рядок файлу:

file.writelines(new_names)          # ❌ БЕЗ \n → "SofiaMykola" (одним рядком!)
file.writelines(n + "\n" for n in new_names)   # ✅ З \n → кожне ім'я на своєму рядку

*Порівняння двох способів запису кількох рядків:
	            writelines()	                    write() у циклі
Синтаксис	    один виклик з генератором/списком	окремий виклик на кожен елемент
Продуктивність	трохи ефективніше 	                звичайна
                для великої кількості рядків
Читабельність	компактніше	                        явно видно КОЖЕН крок запису

*Важливо:
— запускай Task 4 лише ОДИН раз (або будь обережним):

Оскільки режим "a" дописує щоразу, повторний запуск цього скрипту ще раз додасть Sofia та Mykola вдруге (файл матиме їх по 2 копії). Це нормально для навчальної демонстрації, але варто пам'ятати про цю особливість append-режиму на практиці.
"""

# ==============================================================================
# ==============================================================================
"""
# !Task 5 — JSON patient!

Створи:
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

Збережи його в:
data/patient.json
"""

# class_work_09.py (продовження)

import json

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

# --- Збереження словника у JSON-файл ---
# json.dump() записує dict У ВІДКРИТИЙ ФАЙЛ (на відміну від json.dumps(),
# яка повертає РЯДОК — саме "s" на кінці означає "string")
with open("data/patient.json", "w", encoding="utf-8") as file:
    json.dump(patient, file, indent=2, ensure_ascii=False)

# --- Читання файлу назад для перевірки ---
with open("data/patient.json", "r", encoding="utf-8") as file:
    loaded_patient = json.load(file)   # перетворює JSON назад на Python dict

# --- Вивід у рамці ---
with open("data/patient.json", "r", encoding="utf-8") as file:
    raw_content = file.read()   # для показу СИРОГО вмісту файлу

file_lines = raw_content.split("\n")
width = max(len(line) for line in file_lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  DATA/PATIENT.JSON".center(width) + "│")
print("├" + "─" * width + "┤")
for line in file_lines:
    print("│  " + line.ljust(width - 2) + "│")
print("├" + "─" * width + "┤")
print("│  " + f"loaded_patient == patient: {loaded_patient == patient}".ljust(width - 2) + "│")
print("│  " + f"Тип: {type(loaded_patient)}".ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌───────────────────────┐
│    DATA/PATIENT.JSON  │
├───────────────────────┤
│  {                    │
│    "id": 101,         │
│    "name": "Ivan",    │
│    "age": 42,         │
│    "diagnoses": [     │
│      "sinusitis",     │
│      "rhinitis"       │
│    ],                 │
│    "is_active": true  │
│  }                    │
├───────────────────────┤
│  loaded_patient == patient: True│
│  Тип: <class 'dict'>  │
└───────────────────────┘
"""

"""
*Пояснення json.dump() — ключові параметри:
json.dump(patient, file, indent=2, ensure_ascii=False)
#          ↑        ↑      ↑            ↑
#        ЩО      КУДИ    форматування  дозволити НЕ-ASCII символи
#     зберігаємо  (файл)  (відступи)   (кирилиця, якщо буде)
indent=2 — робить JSON читабельним для людини, з відступами по 2 пробіли на кожен рівень вкладеності. Без цього параметра весь файл записався б одним суцільним рядком.
ensure_ascii=False — без цього параметра будь-які не-ASCII символи (наприклад, кирилиця) записались би як '\\uXXXX'-коди замість реальних літер. Тут даних кирилицею немає, але це гарна звичка для проєкту, де такі дані можуть з'явитись пізніше.

*Різниця json.dump() vs json.dumps() — типова плутанина новачків:
json.dump(patient, file)     # записує ПРЯМО у ВІДКРИТИЙ ФАЙЛ, нічого не повертає
json_string = json.dumps(patient)   # повертає РЯДОК (str), файл НЕ чіпає
#                    ↑
#                 "s" = string

# Якщо треба ЗБЕРЕГТИ рядок у файл САМОСТІЙНО:
with open("data/patient.json", "w") as file:
    file.write(json.dumps(patient, indent=2))   # те саме, що json.dump(patient, file, indent=2)

*Пояснення json.load() (читання назад):
with open("data/patient.json", "r", encoding="utf-8") as file:
    loaded_patient = json.load(file)   # JSON-текст → Python dict

type(loaded_patient)   # <class 'dict'> — звичайний Python-словник,
                         # з яким можна працювати як і з будь-яким dict

*Важливий нюанс — не все зберігається "один в один":
patient["is_active"]         # True  (Python bool)
loaded_patient["is_active"]  # True  (той самий bool — JSON має власний true/false,
                               #        який Python автоматично конвертує назад)

# Але, наприклад, tuple ПЕРЕТВОРЮЄТЬСЯ на list при збереженні в JSON:
# JSON НЕ МАЄ поняття "tuple" — лише "array" (що відповідає list)

Для цієї конкретної задачі всі типи (int, str, list, bool) зберігаються й читаються без втрат, тому loaded_patient == patient дасть True.

*Зв'язок із попереднім днем: 
цей формат .json — саме той, у якому MedicalMeasurement.to_json() та MedicalNote.to_json() формували свої звіти (через json.dumps()). Тепер додається інша половина цієї теми: реальне збереження на диск і читання назад із файлу, а не лише генерація рядка в пам'яті.
"""

# ==============================================================================
# ==============================================================================

"""
# !Task 6 — JSON reading!

Завантаж patient.json назад у Python.

Виведи:
Patient: Ivan
Age: 42
Diagnoses: sinusitis, rhinitis
Active: True
"""

import json

# --- Завантаження patient.json назад у Python ---
with open("data/patient.json", "r", encoding="utf-8") as file:
    patient = json.load(file)   # JSON-текст → Python dict

# --- Варіант 1: join() — гнучкий, працює для БУДЬ-ЯКОЇ кількості діагнозів ---
diagnoses_joined = ", ".join(patient["diagnoses"])

# --- Варіант 2: доступ за індексом — працює ЛИШЕ якщо рівно 2 діагнози ---
diagnoses_indexed = f"{patient['diagnoses'][0]}, {patient['diagnoses'][1]}"

# --- Вивід у рамці ---
lines = [
    f"Patient: {patient['name']}",
    f"Age: {patient['age']}",
    f"Diagnoses: {diagnoses_joined}",
    f"Active: {patient['is_active']}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  PATIENT INFO".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

print(f"\nПеревірка: join() == індексація? {diagnoses_joined == diagnoses_indexed}")

"""
┌──────────────────────────────────┐
│            PATIENT INFO          │
├──────────────────────────────────┤
│  Patient: Ivan                   │
│  Age: 42                         │
│  Diagnoses: sinusitis, rhinitis  │
│  Active: True                    │
└──────────────────────────────────┘

Перевірка: join() == індексація? True
"""

"""
*Пояснення двох способів формування "sinusitis, rhinitis":

--Варіант 1 — ", ".join():
patient["diagnoses"]   # → ["sinusitis", "rhinitis"]

", ".join(patient["diagnoses"])
# → "sinusitis, rhinitis"

# Працює для БУДЬ-ЯКОЇ кількості елементів:
", ".join(["sinusitis"])                          # → "sinusitis"
", ".join(["sinusitis", "rhinitis", "otitis"])    # → "sinusitis, rhinitis, otitis"
", ".join([])                                       # → ""  (порожній рядок, без помилки)

--Варіант 2 — доступ за індексом:
f"{patient['diagnoses'][0]}, {patient['diagnoses'][1]}"
#              ↑                          ↑
#         ПЕРШИЙ елемент              ДРУГИЙ елемент

# Працює ТІЛЬКИ якщо у списку РІВНО 2 елементи:
patient["diagnoses"] = ["sinusitis"]
# f"{...[0]}, {...[1]}"  → 💥 IndexError: list index out of range
#                            (бо [1] не існує — елемент лише один!)

*Чому join() — краще рішення на практиці:

	                    ", ".join(diagnoses)	  diagnoses[0], diagnoses[1]
Працює для 1 елемента	✅ так	                ❌ IndexError (якщо звертатись до [1])
Працює для 3+ елементів	✅ так, автоматично	    ❌ треба дописувати [2], [3]... вручну
Гнучкість	            ✅ універсально	        ⚠️ лише для точно відомої кількості
Читабельність коду	    коротко й ясно	          стає громіздким при більшій кількості

*Головний висновок: 
join() — правильний вибір для реальних даних, де кількість елементів списку наперед невідома (у пацієнта може бути один діагноз, а може бути п'ять). Доступ за індексом тут показаний лише для порівняння й розуміння, чому саме join() — надійніший підхід; у реальному коді для змінної кількості елементів завжди варто обирати join().

*Доступ через patient['name'] — одинарні лапки всередині f-string:
f"Patient: {patient['name']}"
#                  ↑      ↑
#            одинарні лапки ВСЕРЕДИНІ f-string,
#            бо ЗОВНІШНІ лапки самого f-string — подвійні

Python дозволяє змішувати типи лапок (одинарні всередині подвійних, і навпаки) — це потрібно, щоб Python не переплутав, де саме закінчується рядок.

*Зв'язок із попередньою задачею: 
тут використовується той самий patient.json, збережений у Task 5 — демонструючи повний цикл: Python dict → JSON-файл на диску → JSON-файл → Python dict знову, з якого потім читаються окремі поля для формування зрозумілого звіту.
"""

# ==============================================================================
# ==============================================================================

"""
# !Task 7 — JSON collection!

Створи файл:
data/patients.json

з масивом:
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

Завантаж його Python та:
-порахуй кількість пацієнтів;
-знайди середній вік;
-знайди найстаршого;
-виведи список імен.

"""

import json

patients_data = [
    {"id": 1, "name": "Ivan", "age": 42},
    {"id": 2, "name": "Olena", "age": 35},
    {"id": 3, "name": "Petro", "age": 51},
]

# --- Збереження масиву у JSON-файл ---
with open("data/patients.json", "w", encoding="utf-8") as file:
    json.dump(patients_data, file, indent=2, ensure_ascii=False)

# --- Завантаження назад ---
with open("data/patients.json", "r", encoding="utf-8") as file:
    patients = json.load(file)   # JSON array → Python list of dicts

# ═══════════════════════════════════════════
# Варіант 1: max()/sum() з comprehension
# ═══════════════════════════════════════════
count_v1 = len(patients)
average_age_v1 = sum(p["age"] for p in patients) / len(patients)
oldest_v1 = max(patients, key=lambda p: p["age"])
names_v1 = [p["name"] for p in patients]

# ═══════════════════════════════════════════
# Варіант 2: звичайний for-цикл для всього
# ═══════════════════════════════════════════
count_v2 = 0
total_age = 0
oldest_v2 = patients[0]
names_v2 = []

for patient in patients:
    count_v2 += 1
    total_age += patient["age"]
    if patient["age"] > oldest_v2["age"]:
        oldest_v2 = patient
    names_v2.append(patient["name"])

average_age_v2 = total_age / count_v2

# --- Вивід у рамці ---
lines = [
    f"Кількість пацієнтів:  {count_v1}",
    f"Середній вік:         {average_age_v1:.1f}",
    f"Найстарший:           {oldest_v1['name']} ({oldest_v1['age']} років)",
    f"Список імен:          {names_v1}",
    "─" * 45,
    f"(перевірка через for): count={count_v2}, avg={average_age_v2:.1f}, ",
    f"oldest={oldest_v2['name']}, names={names_v2}",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  СТАТИСТИКА ПАЦІЄНТІВ (JSON)".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────────────────────────────────────┐
│             СТАТИСТИКА ПАЦІЄНТІВ (JSON)            │
├────────────────────────────────────────────────────┤
│  Кількість пацієнтів:  3                           │
│  Середній вік:         42.7                        │
│  Найстарший:           Petro (51 років)            │
│  Список імен:          ['Ivan', 'Olena', 'Petro']  │
│  ─────────────────────────────────────────────     │
│  (перевірка через for): count=3, avg=42.7,         │
│  oldest=Petro, names=['Ivan', 'Olena', 'Petro']    │
└────────────────────────────────────────────────────┘
"""

"""
*Пояснення json.load() для МАСИВУ (на відміну від Task 6, де був один об'єкт):
# patients.json містить [ {...}, {...}, {...} ]  — JSON array
patients = json.load(file)
# → [{"id": 1, "name": "Ivan", "age": 42}, {"id": 2, ...}, {"id": 3, ...}]
#   ↑
#   Python LIST з DICT всередині — те саме, що ти вже бачив
#   у Challenge №5-8 попереднього дня (list[dict])

*Варіант 1 — вбудовані функції з key/generator:
# sum() з генераторним виразом (без квадратних дужок — та сама ідея, що й у any()/all()):
sum(p["age"] for p in patients)
# → 42 + 35 + 51 = 128

average = 128 / 3   # → 42.67

# max() з key=lambda — той самий підхід, що в Task 3 (max з key=len)
max(patients, key=lambda p: p["age"])
# → шукає СЛОВНИК, де p["age"] найбільше
# → {"id": 3, "name": "Petro", "age": 51}

*Варіант 2 — звичайний for, усе рахується "вручну" за один прохід:
count = 0
total_age = 0
oldest = patients[0]   # стартуємо з ПЕРШОГО пацієнта як "поточний рекорд"

for patient in patients:
    count += 1                                    # рахуємо кількість
    total_age += patient["age"]                    # накопичуємо суму віку
    if patient["age"] > oldest["age"]:              # шукаємо максимум
        oldest = patient
    names.append(patient["name"])                    # збираємо імена

average = total_age / count

*Ключова перевага Варіанту 2 — ОДИН прохід по списку для ВСЬОГО:
---# Варіант 1 — ЧОТИРИ окремих проходи по patients:
count_v1 = len(patients)                         # прохід 1 (внутрішній, у len)
average_age_v1 = sum(...) / len(patients)         # прохід 2 (sum), ще раз len
oldest_v1 = max(patients, key=...)                # прохід 3
names_v1 = [p["name"] for p in patients]           # прохід 4

---# Варіант 2 — ОДИН прохід for робить ВСЕ одразу:
for patient in patients:
    count += 1
    total_age += patient["age"]
    # ... і т.д. — усе в ОДНОМУ циклі

Для списку з 3 елементів різниця в продуктивності непомітна, але для великого списку (тисячі пацієнтів) один прохід замість чотирьох — суттєва економія часу.

*Порівняльна таблиця:
	                Вбудовані функції (max/sum)	               Звичайний for
Читабельність	    ✅ кожен рядок — один чіткий намір	      потрібно "прочитати" всю логіку
Кількість 	        4 окремих 	                               1 
проходів по списку  (по одному на кожну статистику)            (усе одночасно)
Коли обирати	    невеликі списки, 	                        великі списки, 
                    простота коду важливіша                     критична продуктивність

*Зв'язок із попередніми задачами: 
це підсумкове завдання дня — об'єднує json.load() (Task 6), list[dict] (Challenge №6-8 попереднього дня), max()/sum() з key (Task 3 цього дня, Практика №7 попереднього дня) в одну комплексну задачу над реальними даними з файлу.
"""
