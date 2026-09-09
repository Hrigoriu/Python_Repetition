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
