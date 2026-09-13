# main.py
"""Демонстрація роботи модуля string_utils."""

from string_utils import contains_keyword, normalize_text, word_count

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
lines.pop()  # прибираємо зайвий розділювач після останнього запису

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
