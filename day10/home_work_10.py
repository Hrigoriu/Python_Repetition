"""
## !Challenge 1 — MedAssistant modules!

Створи:
home_work_10/
├── medassistant.py
├── patient_utils.py
├── statistics_utils.py
└── data/

У patient_utils.py:
def find_patient(
    patients: list[dict],
    name: str,
) -> dict | None:
    ...

У statistics_utils.py:
def average_age(patients: list[dict]) -> float:
    ...

def average_temperature(patients: list[dict]) -> float:
    ...

def oldest_patient(patients: list[dict]) -> dict:
    ...

У medassistant.py:
from patient_utils import find_patient
from statistics_utils import (
    average_age,
    average_temperature,
    oldest_patient,
)

і побудуй невеликий application.
"""
#1.
#data/patients.json
"""
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
  },
  {
    "id": 4,
    "name": "Hanna",
    "age": 29,
    "diagnosis": "otitis",
    "temperature": 37.9
  }
]
"""

#2.
"""patient_utils.py

Patient lookup utilities for MedAssistant.
"""


def find_patient(patients: list[dict], name: str) -> dict | None:
    """Find a patient by name (case-insensitive).

    Args:
        patients: A list of patient records.
        name: The name to search for.

    Returns:
        dict | None: The matching patient record, or None if not found.
    """
    for patient in patients:
        if patient["name"].lower() == name.lower():
            return patient
    return None

#3.
"""statistics_utils.py

Aggregate statistics over a list of patient records, for MedAssistant.
"""


def average_age(patients: list[dict]) -> float:
    """Compute the average age across all patients.

    Args:
        patients: A list of patient records (must include "age").

    Returns:
        float: The average age.
    """
    return sum(p["age"] for p in patients) / len(patients)


def average_temperature(patients: list[dict]) -> float:
    """Compute the average temperature across all patients.

    Args:
        patients: A list of patient records (must include "temperature").

    Returns:
        float: The average temperature.
    """
    return sum(p["temperature"] for p in patients) / len(patients)


def oldest_patient(patients: list[dict]) -> dict:
    """Find the oldest patient in the list.

    Args:
        patients: A list of patient records (must include "age").

    Returns:
        dict: The patient record with the highest age.
    """
    return max(patients, key=lambda p: p["age"])

#4.
"""medassistant.py

MedAssistant application entry point:
    imports -> data (load) -> calls (statistics + lookup) -> output (print + save report)
"""

import json

from patient_utils import find_patient
from statistics_utils import (
    average_age,
    average_temperature,
    oldest_patient,
)


# ═══════════════════════════════════════════
# LOAD
# ═══════════════════════════════════════════
def load_patients(path: str) -> list[dict] | None:
    """Load patient records from a JSON file, handling common errors.

    Args:
        path: Path to the JSON file.

    Returns:
        list[dict] | None: The records, or None on failure.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"⚠ Error: file '{path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"⚠ Error: file '{path}' contains invalid JSON ({e}).")
        return None


# ═══════════════════════════════════════════
# GENERATE REPORT
# ═══════════════════════════════════════════
def generate_report(patients: list[dict], searched_patient: dict | None, search_name: str) -> str:
    """Build a human-readable text report.

    Args:
        patients: All loaded patient records.
        searched_patient: Result of find_patient(), or None.
        search_name: The name that was searched for.

    Returns:
        str: The full report text.
    """
    title = "MEDASSISTANT REPORT"
    oldest = oldest_patient(patients)

    search_line = (
        f"{searched_patient['name']}, age {searched_patient['age']}, "
        f"diagnosis: {searched_patient['diagnosis']}"
        if searched_patient is not None
        else f"'{search_name}' not found"
    )

    return (
        f"{title}\n"
        f"{'=' * len(title)}\n\n"
        f"Total patients: {len(patients)}\n"
        f"Average age: {average_age(patients):.1f}\n"
        f"Average temperature: {average_temperature(patients):.1f}\n"
        f"Oldest patient: {oldest['name']} ({oldest['age']})\n\n"
        f"Search result for '{search_name}': {search_line}\n"
    )


# ═══════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════
def save_report(path: str, report: str) -> None:
    """Save a text report to disk.

    Args:
        path: Destination file path.
        report: The report content.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(report)


# ═══════════════════════════════════════════
# MAIN — orchestrates the pipeline only
# ═══════════════════════════════════════════
def main() -> None:
    patients = load_patients("data/patients.json")
    if patients is None:
        return

    search_name = "Petro"
    searched_patient = find_patient(patients, search_name)

    report = generate_report(patients, searched_patient, search_name)
    save_report("data/report.txt", report)

    # --- Verify by reading the saved report back and printing it framed ---
    with open("data/report.txt", "r", encoding="utf-8") as file:
        saved_report = file.read()

    lines = saved_report.rstrip("\n").split("\n")
    width = max(len(line) for line in lines) + 4

    print("\n┌" + "─" * width + "┐")
    print("│" + "  data/report.txt".center(width) + "│")
    print("├" + "─" * width + "┤")
    for line in lines:
        print("│  " + line.ljust(width - 2) + "│")
    print("└" + "─" * width + "┘")


if __name__ == "__main__":
    main()

"""
┌──────────────────────────────────────────────────────────────────┐
│                          data/report.txt                         │
├──────────────────────────────────────────────────────────────────┤
│  MEDASSISTANT REPORT                                             │
│  ===================                                             │
│                                                                  │
│  Total patients: 4                                               │
│  Average age: 41.8                                               │
│  Average temperature: 37.6                                       │
│  Oldest patient: Petro (61)                                      │
│                                                                  │
│  Search result for 'Petro': Petro, age 61, diagnosis: sinusitis  │
└──────────────────────────────────────────────────────────────────┘
"""

"""
#*Чому межі модулів накреслені саме так:
patient_utils.py      → вміє ЗНАЙТИ окремого пацієнта (find_patient)
statistics_utils.py   → вміє ЗБИРАТИ ДАНІ щодо багатьох пацієнтів (average_*, oldest_*)
medassistant.py        → НІЧОГО не знає про саму логіку роботи з пацієнтами — він лише
                          завантажує дані, викликає два модулі-утиліти та
                          обробляє введення-виведення (читання/запис файлів)

Це точно віддзеркалює реструктуризацію файлу day10/class_work_10.py із Завдання 7 (імпорт → дані → виклики → вихідні дані), масштабовану до рівня реального «додатка»: файл medassistant.py ніколи сам не обчислює середнє значення та не здійснює пошук у списку — він лише координує виклики до двох допоміжних модулів, застосовуючи той самий принцип розділення відповідальності, що й на рівні файлів.

#*Чому find_patient() повертає dict | None, і як generate_report() обробляє обидва випадки:
searched_patient = find_patient(patients, «Petro»)   # → словник, оскільки Petro існує

search_line = (
    f"{searched_patient['name']}, age {searched_patient['age']}, "
    f"diagnosis: {searched_patient['diagnosis']}"
    if searched_patient is not None     # ← явна перевірка на None перед використанням словника
    else f"'{search_name}' not found"
)

Це той самий захисний алгоритм, що й у попередньому завданні «find_patient» — генератор звіту ніколи не припускає, що пошук завершився успішно; він явно виконує розгалуження у випадку значення None, тож відсутність пацієнта призводить до виведення чіткого повідомлення замість помилки TypeError, яка виникає при спробі індексації за None.

Чому конвеєр все ще дотримується послідовності «завантаження → обчислення → фільтрація/пошук → генерація → збереження»:

Це та сама п’ятиетапна архітектура, що й у завданні «MedAssistant Data Pipeline» з дня 09 — load_patients() (введення-виведення), дві функції statistics_utils (чисті обчислення), find_patient() (чистий пошук), generate_report() (чисте форматування), save_report() (введення-виведення). Кожен етап можна тестувати незалежно, і в кожного є лише одна причина для зміни.
"""

# ==============================================================================
# ==============================================================================

"""
## !Challenge 2 — DRY!

Порівняй два підходи.

Варіант A
Все в одному файлі:
medassistant.py

Варіант B
medassistant.py
patient_utils.py
statistics_utils.py

Поясни:
де менше дублювання;
де простіше тестувати;
де простіше розширювати проєкт.
"""

"""
#*Варіант A (все в одному файлі) vs Варіант B (три файли)
            1. Де менше дублювання

Варіант B виграє, але не автоматично — сам факт розбиття на файли не усуває дублювання, він лише робить повторне використання зручнішим і природнішим.

# Варіант A — усе в medassistant.py:
def find_patient(patients, name):
    for p in patients:
        if p["name"].lower() == name.lower():
            return p
    return None

# ... 200 рядків нижче, комусь треба знайти пацієнта ЗА ДІАГНОЗОМ,
# і найпростіший шлях — СКОПІЮВАТИ цикл вище і трохи змінити:
def find_by_diagnosis(patients, diagnosis):
    for p in patients:
        if p["diagnosis"].lower() == diagnosis.lower():   # ← майже той самий код!
            return p
    return None

У великому одному файлі "шлях найменшого спротиву" — це скопіювати сусідній блок і трохи підправити, бо шукати "чи є вже щось подібне" серед сотень рядків незручно.

# Варіант B — patient_utils.py вже МАЄ знайому структуру:
def find_patient(patients, name): ...

# Наступний розробник ВІДКРИВАЄ саме ЦЕЙ файл (він короткий, у ньому
# ЛИШЕ функції пошуку) і одразу бачить: "о, тут вже є шаблон для пошуку" —
# і пише find_by_diagnosis() ПОРЯД, за тим самим шаблоном, замість
# копіювання з абсолютно іншого місця величезного файлу

#*Важливе застереження: 
розбиття на файли само по собі — це організаційна межа, а не технічна гарантія проти дублювання. Можна так само дублювати код і між трьома файлами. Реальна перевага — психологічна: коротший, тематично цільний файл легше проглянути перед тим, як писати щось нове, тому шанс "не помітити, що це вже є" — нижчий.

            2. Де простіше тестувати
Тут перевага Варіанту B — вже не "ймовірна", а структурна.

# Варіант A — щоб протестувати average_age(), треба ІМПОРТУВАТИ medassistant.py:
import medassistant   # ⚠️ це виконає ВЕСЬ файл, включно з load_patients(),
                        #    save_report(), і, якщо немає if __name__ == "__main__",
                        #    можливо, навіть file I/O одразу при імпорті!

# Тест стає "крихким": залежить від того, чи ІСНУЄ data/patients.json на диску,
# хоча тестуємо ЛИШЕ математичну формулу середнього віку

# Варіант B — average_age() ізольована, БЕЗ побічних ефектів:
from statistics_utils import average_age

def test_average_age():
    fake_patients = [{"age": 20}, {"age": 30}, {"age": 40}]
    assert average_age(fake_patients) == 30.0
    # ЖОДНОГО файлу, ЖОДНОГО print() — чиста функція, чистий тест

#*Ключова причина: 
# statistics_utils.py не має побічних ефектів (I/O, print) — лише чисті функції "дані на вході → дані на виході". Це саме те, що робить unit-тестування тривіальним: не потрібні "заглушки" файлової системи, не потрібно імітувати консольний вивід. У Варіанті A відділити "чисту математику" від "роботи з файлами" технічно можливо, але вимагає такої самої дисципліни, яку природно нав'язує вже сам факт окремого файлу.

            3. Де простіше розширювати проєкт

Варіант B масштабується краще, коли проєкт росте (а MedAssistant — саме такий випадок, бо йде на GitHub і буде розвиватись далі):
Хочеш додати:            Варіант A                      Варіант B
─────────────────────────────────────────────────────────────────────────────────────────
Нову статистику          правиш ВЕЛИКИЙ файл            правиш statistics_utils.py,
(напр. median_age)       (ризик зачепити щось           НІЧОГО іншого не чіпаєш
                          непов'язане)

Новий тип пошуку         те саме                        правиш patient_utils.py

Роботу в команді         усі правлять ОДИН файл →       різні люди працюють у
                         постійні merge conflicts       РІЗНИХ файлах паралельно

Найважливіший практичний доказ ти вже отримав сьогодні: коли class_work_10.py (day10) знадобилось перебудувати так, щоб він містив лише imports → data → calls → output (Task 7) — це стало можливим саме тому, що patient_utils.py і statistics_utils.py вже існували окремо. Якби все було в одному файлі, "перебудова" означала б переписування половини логіки, а не просто "додати два import".

Чесний контраргумент — коли Варіант B це переоверенджиніринг (YAGNI)

Для справді малого, одноразового скрипта (5-10 функцій, ніхто інший його не використовує, розширювати не плануєш) розбиття на три файли — це зайва складність: три файли для розуміння замість одного, зайві import, потрібно пам'ятати, "в якому файлі яка функція". Тут YAGNI підказує: не розбивай завчасно, поки реально не відчуваєш болю від монолітного файлу.

#*Головний критерій вибору:
1.Якщо проєкт житиме довго, розвиватиметься (нові функції, нові типи пошуку/статистики) і/або тестуватиметься — Варіант B окупається майже одразу. 
2.Якщо це одноразовий скрипт "на сьогодні" — Варіант A простіший і чесніший вибір.

Для MedAssistant (публікація на GitHub, магістерська робота, планований розвиток) — Варіант B, який ти вже реалізував, є правильним вибором за суттю задачі, а не просто "тому що так прийнято".
"""

# ==============================================================================
# ==============================================================================

"""
## !Challenge 3 — reusable module!

Створи:
string_utils.py

з:
def normalize_text(text: str) -> str:
    ...

def word_count(text: str) -> int:
    ...

def contains_keyword(text: str, keyword: str) -> bool:
    ...

Потім використовуй цей модуль у головній програмі.
"""

#1.
# string_utils.py
"""Утилітарні функції для базової обробки тексту."""

import re


def normalize_text(text: str) -> str:
    """Прибирає зайві пробіли та переводить текст у нижній регістр.

    Той самий підхід, що вже застосовувався для normalize_medical_text():
    strip() по краях + split()/join() для схлопування подвійних пробілів.
    """
    cleaned = text.strip()
    return " ".join(cleaned.lower().split())


def word_count(text: str) -> int:
    """Рахує кількість токенів у тексті (слова + окремі розділові знаки).

    Регекс-токенізація: \\w+ ловить слова, [^\\w\\s] ловить кожен
    розділовий знак ОКРЕМО (те саме, що в Medical Text Analyzer).
    """
    tokens = re.findall(r"\w+|[^\w\s]", text)
    return len(tokens)


def contains_keyword(text: str, keyword: str) -> bool:
    """Перевіряє, чи міститься ключове слово в тексті (нечутливо до регістру)."""
    return keyword.lower() in text.lower()


if __name__ == "__main__":
    sample = "  Patient   complains of FEVER and sinusitis.  "
    print(normalize_text(sample))
    print(word_count(sample))
    print(contains_keyword(sample, "fever"))

#2.
# main.py
"""Демонстрація роботи модуля string_utils."""

from string_utils import normalize_text, word_count, contains_keyword

# --- Дані ---
medical_notes = [
    "  Patient   complains of FEVER and sinusitis.  ",
    "No symptoms reported during examination.",
    "Persistent COUGH, mild pain in the throat.",
]
keywords = ["fever", "cough", "pain", "sinusitis"]

# --- Виклики ---
results = []
for note in medical_notes:
    normalized = normalize_text(note)
    count = word_count(note)
    found_keywords = [kw for kw in keywords if contains_keyword(note, kw)]
    results.append((note, normalized, count, found_keywords))

# --- Вивід у рамці ---
lines = []
for original, normalized, count, found in results:
    lines.append(f"Оригінал:      {original!r}")
    lines.append(f"  normalize_text(): {normalized!r}")
    lines.append(f"  word_count():      {count}")
    lines.append(f"  Знайдені слова:    {found if found else 'немає'}")
    lines.append("─" * 55)
lines.pop()   # прибираємо зайвий розділювач після останнього запису

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  STRING_UTILS — ДЕМОНСТРАЦІЯ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────────────────────────────────────────────────────┐
│                     STRING_UTILS — ДЕМОНСТРАЦІЯ                    │
├────────────────────────────────────────────────────────────────────┤
│  Оригінал:      '  Patient   complains of FEVER and sinusitis.  '  │
│    normalize_text(): 'patient complains of fever and sinusitis.'   │
│    word_count():      7                                            │
│    Знайдені слова:    ['fever', 'sinusitis']                       │
│  ───────────────────────────────────────────────────────           │
│  Оригінал:      'No symptoms reported during examination.'         │
│    normalize_text(): 'no symptoms reported during examination.'    │
│    word_count():      6                                            │
│    Знайдені слова:    немає                                        │
│  ───────────────────────────────────────────────────────           │
│  Оригінал:      'Persistent COUGH, mild pain in the throat.'       │
│    normalize_text(): 'persistent cough, mild pain in the throat.'  │
│    word_count():      9                                            │
│    Знайдені слова:    ['cough', 'pain']                            │
└────────────────────────────────────────────────────────────────────┘
"""

"""
#*Пояснення кожної функції:
normalize_text("  Patient   HAS Fever  ")
# strip():        "Patient   HAS Fever"
# .lower():        "patient   has fever"
# split()+join():   "patient has fever"    ← готовий, чистий текст

word_count("Patient has fever.")
# re.findall(r"\w+|[^\w\s]", ...)
# → ["Patient", "has", "fever", "."]
# → len(...) = 4   (крапка рахується ЯК ОКРЕМИЙ токен, не приліплена до "fever")

contains_keyword("Patient has FEVER.", "fever")
# "fever" in "patient has fever."   ← обидва боки .lower()
# → True

#*Чому саме такий поділ відповідальностей у string_utils.py:
normalize_text()      # "приведи текст у канонічну форму"
word_count()           # "порахуй щось про текст"
contains_keyword()      # "перевір щось про текст"

Кожна функція робить рівно одну річ і не залежить від виклику інших двох — можна викликати word_count() без попереднього normalize_text(), і навпаки. Це навмисно: contains_keyword() сам робить .lower() всередині, а не покладається на те, що текст уже був нормалізований кимось іншим раніше — так функцію можна безпечно викликати напряму, з будь-яким сирим текстом, без прихованих залежностей від порядку виклику.

#*Зв'язок із Medical Text Analyzer (попередній день):
Це той самий алгоритм токенізації та нормалізації, що вже застосовувався в analyze_medical_text() — тепер розбитий на три незалежні, багаторазово використовувані функції в окремому модулі, замість того, щоб бути "зашитим" всередину однієї великої функції. Якщо завтра захочеш лише порахувати слова (без пошуку ключових слів) — просто імпортуєш word_count() окремо, не тягнучи за собою решту логіки.

#*Практична перевага модульності для MedAssistant:
# У будь-якому іншому файлі MedAssistant можна тепер написати:
from string_utils import contains_keyword

if contains_keyword(diagnosis_note, "sinusitis"):
    ...

Без потреби копіювати логіку keyword.lower() in text.lower() щоразу — вона живе в одному місці, готова до перевикористання будь-де в проєкті.
"""

# ==============================================================================
# ==============================================================================

"""
## !Challenge 4 — module API!

Не імпортуй зайвого.

Порівняй:
import patient_utils

і:
from patient_utils import find_patient

та поясни, коли кожен варіант має сенс.
"""

"""
#*Порівняння: `import patient_utils` vs `from patient_utils import find_patient`

**Ключова умова завдання — "не імпортуй зайвого":**
# patient_utils.py (після Challenge 1) містить ЛИШЕ одну функцію:
def find_patient(patients, name):
    ...

### Варіант A: `import patient_utils`
import patient_utils

patient = patient_utils.find_patient(patients, "Ivan")
#         ↑
#     ЗАВЖДИ через префікс "patient_utils."

**Що це означає технічно:** Python завантажує **весь модуль** як єдиний об'єкт і "прив'язує" до нього ім'я `patient_utils`. Усе, що є в модулі (навіть якщо там 50 функцій), стає доступним через крапку — але **використовуєш** ти лише те, що явно викликаєш.


### Варіант B: `from patient_utils import find_patient`
from patient_utils import find_patient

patient = find_patient(patients, "Ivan")
#         ↑
#     БЕЗ префікса — ім'я забирається З модуля напряму в поточний простір імен
```

#*Що це означає технічно:* 
Python усе одно завантажує **весь файл** `patient_utils.py` (це відбувається завжди, незалежно від синтаксису імпорту), але після завантаження в поточному файлі створюється **лише одне** нове ім'я — `find_patient` — без потреби писати `patient_utils.` щоразу.

### Чому "не імпортуй зайвого" стосується ОБОХ варіантів однаково

#*Це важливий нюанс: 
**обсяг завантаженого коду** — однаковий в обох випадках. 
Різниця **не** в тому, скільки коду виконується, а в тому, **скільки імен додається** в поточний простір і **як вони виглядають при використанні**:

# Варіант A — додає ОДНЕ ім'я: "patient_utils"
# (усі функції модуля доступні, але ЧЕРЕЗ префікс)
import patient_utils
patient_utils.find_patient(...)   # ясно, звідки функція

# Варіант B — додає ОДНЕ ім'я: "find_patient"
# (тільки ЦЯ функція напряму, без префікса)
from patient_utils import find_patient
find_patient(...)                  # коротше, але без "адреси походження"

#*"Не імпортуй зайвого" тут означає: 
якщо в модулі **кілька** функцій, а тобі потрібна **лише одна** — обирай `from patient_utils import find_patient`, а **не** `from patient_utils import *` (зірочка імпортує **все**, включно з тим, що ти ніколи не використаєш, і засмічує простір імен).

#* Коли кожен варіант має сенс
Ситуація                        Обери

Модуль має багато функцій,      import patient_utils — префікс patient_utils.
ти використовуєш кілька         одразу показує, звідки кожна функція
з різних місць коду             

Модуль малий (як зараз —        from patient_utils import find_patient —
рівно одна функція), і          префікс був би зайвим "шумом"
ти використовуєш лише її

Пишеш велику програму з         import X — читаючи код, завжди ясно, 
багатьмабагатьма модулями       з якого саме модуля прийшла функція,
(patient_utils,                 навіть якщо в різних модулях є функції 
statistics_utils,               з однаковими назвами
string_utils...)

Пишеш короткий скрипт           from X import ... — код коротший і
із 1-2 імпортованими            читабельніший, ризик конфлікту імен низький
функціями з одного джерела

#**Практичний приклад ризику, що виникає при "неправильному" виборі:**
# Якщо в майбутньому patient_utils.py матиме ще й normalize_name(),
# а string_utils.py матиме normalize_text() —
# з import X завжди ясно, яка функція з якого модуля:
import patient_utils
import string_utils

patient_utils.normalize_name(...)     # ясно: це про ІМ'Я пацієнта
string_utils.normalize_text(...)       # ясно: це про ТЕКСТ загалом

# А з from X import * — ризик конфлікту:
from patient_utils import *
from string_utils import *
normalize_name(...)   # ✅ ще працює
# але якщо ОБИДВА модулі мали б функцію з ОДНАКОВОЮ назвою —
# друга ЗАМІНИЛА б першу, ТИХО, без жодної помилки чи попередження

*# Висновок саме для цього конкретного модуля
Для `patient_utils.py` **зараз** (одна функція `find_patient`) — `from patient_utils import find_patient` є **правильним, "неперевантаженим"** вибором: він явно каже "мені потрібна рівно ця одна річ", без зайвого `patient_utils.` префікса, і без ризику "зайвого імпорту" (`*`), проти якого й попереджає умова завдання. Якщо ж `patient_utils.py` **виросте** до кількох функцій, які використовуються в **різних** частинах великої програми — тоді варто переглянути рішення на `import patient_utils`, щоб зберегти "адресність" кожного виклику.

"""

# ==============================================================================
# ==============================================================================
"""

🔥 Challenge 5 — MedAssistant v2

Це головне завдання.

Перероби твій День 9 pipeline:
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

у модульну структуру:
day10/
├── main.py
├── patient_utils.py
├── statistics_utils.py
├── report_utils.py
└── data/
    └── medassistant_patients.json

patient_utils.py
Робота з пацієнтами.

statistics_utils.py
Статистика.

report_utils.py
Генерація звітів.

main.py
Лише orchestration.

Тобто:
def main():
    ...

має читатися майже як сценарій:
load patients
calculate statistics
filter patients
generate report
save report

Це буде твій перший маленький модульний application.
"""

#1.
#data/medassistant_patients.json
"""
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
"""

#2.
#patient_utils.py - все, що стосується пошуку та відбору пацієнтів:
"""patient_utils.py

Loading, searching, and filtering patient records for MedAssistant.
"""

import json


def load_patients(path: str) -> list[dict] | None:
    """Load patient records from a JSON file, handling common errors.

    Args:
        path: Path to the JSON file.

    Returns:
        list[dict] | None: The records, or None on failure.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"⚠ Error: file '{path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"⚠ Error: file '{path}' contains invalid JSON ({e}).")
        return None


def find_patient(patients: list[dict], name: str) -> dict | None:
    """Find a patient by name (case-insensitive).

    Args:
        patients: A list of patient records.
        name: The name to search for.

    Returns:
        dict | None: The matching record, or None if not found.
    """
    for patient in patients:
        if patient["name"].lower() == name.lower():
            return patient
    return None


def filter_by_temperature(patients: list[dict], threshold: float) -> list[dict]:
    """Return patients whose temperature is at or above a threshold.

    Args:
        patients: A list of patient records (must include "temperature").
        threshold: Minimum temperature (inclusive) to be included.

    Returns:
        list[dict]: Matching records.
    """
    return [p for p in patients if p["temperature"] >= threshold]


def filter_by_diagnosis(patients: list[dict], diagnosis: str) -> list[dict]:
    """Return patients matching a given diagnosis (case-insensitive).

    Mirrors filter_by_temperature() for symmetry.

    Args:
        patients: A list of patient records (must include "diagnosis").
        diagnosis: The diagnosis to match.

    Returns:
        list[dict]: Matching records.
    """
    return [p for p in patients if p["diagnosis"].lower() == diagnosis.lower()]

#3.
#statistics_utils.py — виключно обчислення сумарних значень, без операцій вводу-виводу:
"""statistics_utils.py

Aggregate statistics over a list of patient records, for MedAssistant.
"""


def average_age(patients: list[dict]) -> float:
    """Compute the average age across all patients."""
    return sum(p["age"] for p in patients) / len(patients)


def average_temperature(patients: list[dict]) -> float:
    """Compute the average temperature across all patients."""
    return sum(p["temperature"] for p in patients) / len(patients)


def oldest_patient(patients: list[dict]) -> dict:
    """Find the oldest patient in the list."""
    return max(patients, key=lambda p: p["age"])

#4.
#report_utils.py — все про перетворення результатів у звіт:
"""report_utils.py

Report generation and saving for MedAssistant.
"""

import json


def generate_text_report(
    total_patients: int,
    avg_age: float,
    avg_temp: float,
    oldest: dict,
    high_temp_patients: list[dict],
    sinusitis_patients: list[dict],
) -> str:
    """Build a human-readable text report."""
    title = "MEDASSISTANT PATIENT REPORT"

    high_temp_names = ", ".join(p["name"] for p in high_temp_patients) or "none"
    sinusitis_names = ", ".join(p["name"] for p in sinusitis_patients) or "none"

    return (
        f"{title}\n"
        f"{'=' * len(title)}\n\n"
        f"Total patients: {total_patients}\n"
        f"Average age: {avg_age:.1f}\n"
        f"Average temperature: {avg_temp:.1f}\n"
        f"Oldest patient: {oldest['name']} ({oldest['age']})\n\n"
        f"Patients with temperature >= 38.0: {high_temp_names}\n"
        f"Patients with sinusitis: {sinusitis_names}\n"
    )


def generate_json_report(
    total_patients: int,
    avg_age: float,
    avg_temp: float,
    oldest: dict,
    high_temp_patients: list[dict],
    sinusitis_patients: list[dict],
) -> dict:
    """Build a machine-readable JSON-ready report."""
    return {
        "total_patients": total_patients,
        "average_age": round(avg_age, 1),
        "average_temperature": round(avg_temp, 1),
        "oldest_patient": oldest["name"],
        "high_temperature_patients": [p["name"] for p in high_temp_patients],
        "sinusitis_patients": [p["name"] for p in sinusitis_patients],
    }


def save_report(path: str, report: str | dict) -> None:
    """Save a report to disk, as plain text or JSON.

    A str report is written as-is; a dict report is serialized
    with json.dump() — one function instead of two near-duplicates.
    """
    with open(path, "w", encoding="utf-8") as file:
        if isinstance(report, dict):
            json.dump(report, file, indent=2, ensure_ascii=False)
        else:
            file.write(report)

#5.
#main.py — виключно для координації, читається як скрипт:
"""main.py

MedAssistant v2 — modular pipeline entry point.
"""

"""main.py

MedAssistant v2 — modular pipeline entry point.
"""

import json

from patient_utils import (
    load_patients,
    filter_by_temperature,
    filter_by_diagnosis,
)
from statistics_utils import average_age, average_temperature, oldest_patient
from report_utils import generate_text_report, generate_json_report, save_report


def main() -> None:
    # load patients
    patients = load_patients("data/medassistant_patients.json")
    if patients is None:
        return

    # calculate statistics
    total_patients = len(patients)
    avg_age = average_age(patients)
    avg_temp = average_temperature(patients)
    oldest = oldest_patient(patients)

    # filter patients
    high_temp_patients = filter_by_temperature(patients, threshold=38.0)
    sinusitis_patients = filter_by_diagnosis(patients, diagnosis="sinusitis")

    # generate report
    text_report = generate_text_report(
        total_patients, avg_age, avg_temp, oldest, high_temp_patients, sinusitis_patients
    )
    json_report = generate_json_report(
        total_patients, avg_age, avg_temp, oldest, high_temp_patients, sinusitis_patients
    )

    # save report
    save_report("data/report.txt", text_report)
    save_report("data/report.json", json_report)

    # --- verify by reading back and printing ---
    with open("data/report.txt", "r", encoding="utf-8") as file:
        saved_text = file.read()

    lines = saved_text.rstrip("\n").split("\n")
    width = max(len(line) for line in lines) + 4

    print("\n┌" + "─" * width + "┐")
    print("│" + "  data/report.txt".center(width) + "│")
    print("├" + "─" * width + "┤")
    for line in lines:
        print("│  " + line.ljust(width - 2) + "│")
    print("└" + "─" * width + "┘")

    print(f"\ndata/report.json:\n{json.dumps(json_report, indent=2)}")


if __name__ == "__main__":
    main()


"""
┌────────────────────────────────────────────┐
│               data/report.txt              │
├────────────────────────────────────────────┤
│  MEDASSISTANT PATIENT REPORT               │
│  ===========================               │
│                                            │
│  Total patients: 3                         │
│  Average age: 46.0                         │
│  Average temperature: 37.5                 │
│  Oldest patient: Petro (61)                │
│                                            │
│  Patients with temperature >= 38.0: Petro  │
│  Patients with sinusitis: Ivan, Petro      │
└────────────────────────────────────────────┘

data/report.json:
{
  "total_patients": 3,
  "average_age": 46.0,
  "average_temperature": 37.5,
  "oldest_patient": "Petro",
  "high_temperature_patients": [
    "Petro"
  ],
  "sinusitis_patients": [
    "Ivan",
    "Petro"
  ]
}
"""


"""
#*Чому функція main() майже нагадує саму схему конвеєра:
def main():
    patients = load_patients(...)         # load patients
    if patients is None:
        return

    avg_age = average_age(patients)         # calculate statistics
    avg_temp = average_temperature(patients)
    oldest = oldest_patient(patients)

    high_temp = filter_by_temperature(...)   # filter patients
    sinusitis = filter_by_diagnosis(...)

    text_report = generate_text_report(...)   # generate report
    json_report = generate_json_report(...)

    save_report(..., text_report)              # save report
    save_report(..., json_report)

Кожен рядок — це окремий виклик функції з описовою назвою: тут зовсім немає арифметичних операцій, форматування рядків, а також викликів open() чи json.load(). Той, хто вперше читає функцію main(), може зрозуміти поведінку всієї програми за п’ять рядків, не відкриваючи жодного з інших трьох файлів.

#*Чому призначення кожного файлу безпосередньо відповідає його назві:
Файл                    Відповідає за                           НЕ відповідає за
patient_utils.py        завантаження, пошук, фільтрування       статистика, текст/формат звіту
                        необроблених даних про пацієнтів

statistics_utils.py     чиста математика над списками           введення-виведення файлів, 
                        пацієнтів                               форматування

report_utils.py         перетворення чисел у текст              логіка обробки даних про пацієнтів, 
                        або JSON, збереження на диск            логіка статистики

main.py                 послідовне виконання вищезазначених     будь-які фактичні обчислення
                        операцій, нічого іншого

#*Чому функції filter_by_temperature() та filter_by_diagnosis() розміщені у файлі patient_utils.py, а не у report_utils.py:

Фільтрування — це питання про те, які пацієнти відповідають критеріям; 
це логіка домену пацієнтів, яка належить до тієї ж категорії, що й функція find_patient(). 
Це не має нічого спільного з тим, як виглядає звіт, а саме це є єдиною сферою відповідальності файлу report_utils.py. Збереження функцій фільтрування в цьому модулі означає, що якщо завтра вам знадобиться filter_by_temperature() десь, де це не має нічого спільного зі звітами (наприклад, у динамічній інформаційній панелі), ви зможете імпортувати її з patient_utils, не затягуючи при цьому жодного коду, пов’язаного зі звітами.
"""

# ==============================================================================
# ==============================================================================

