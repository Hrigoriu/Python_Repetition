# Домашнє завдання №1
"""
Написати програму "Про себе" (5 рядків через print()).
"""

# --- Дані про себе (актуальні) ---
occupation = "лікар-отоларинголог (ЛОР) із 17-річним клінічним досвідом"
education = "здобуваю ступінь магістра Computer Science (AI & ML Engineering) у GoIT Neoversity WOOLF"
study_start = "29 вересня 2026 року"
thesis = "магістерська робота присвячена автоматичному виявленню патологій пазух носа на КТ/МРТ-знімках (архітектура ViT + CNN + XAI)"
goal = "довгострокова мета — перехід у AI Engineering зі спеціалізацією Computer Vision у HealthTech/MedTech"

# --- Формування рядків ---
lines = [
    f"Я {occupation}.",
    f"{education}.",
    f"Навчання розпочинається {study_start}.",
    f"{thesis}.",
    f"{goal}.",
]

# --- Красивий вивід у рамці ---
width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  ПРО СЕБЕ".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")


"""
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                             ПРО СЕБЕ                                                           │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│  Я лікар-отоларинголог (ЛОР) із 17-річним клінічним досвідом.                                                                  │
│  здобуваю ступінь магістра Computer Science (AI & ML Engineering) у GoIT Neoversity WOOLF.                                     │
│  Навчання розпочинається 29 вересня 2026 року.                                                                                 │
│  магістерська робота присвячена автоматичному виявленню патологій пазух носа на КТ/МРТ-знімках (архітектура ViT + CNN + XAI).  │
│  довгострокова мета — перехід у AI Engineering зі спеціалізацією Computer Vision у HealthTech/MedTech.                         │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
"""
# ==============================================
# Домашнє завдання №2
"""
Написати програму, яка запитує ім'я, місто та професію і виводить їх у форматованому реченні.
"""


def get_text(prompt):
    "Запитує текст і перевіряє, що поле не порожнє."
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("⚠ Поле не може бути порожнім. Спробуйте ще раз.\n")


# --- Збір даних ---
name = get_text("Введіть ваше ім'я: ")
city = get_text("Введіть ваше місто: ")
profession = get_text("Введіть вашу професію: ")

# --- Формоване речення ---
sentence = f"{name} живе у місті {city} та працює на посаді «{profession}»."

# --- Красивий вивід у рамці ---
width = len(sentence) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  РЕЗУЛЬТАТ".center(width) + "│")
print("├" + "─" * width + "┤")
print("│  " + sentence.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")


"""
Введіть ваше ім'я: Hrigoriu
Введіть ваше місто:
⚠ Поле не може бути порожнім. Спробуйте ще раз.

Введіть ваше місто: Харків
Введіть вашу професію: Лікар

┌─────────────────────────────────────────────────────────────┐
│                           РЕЗУЛЬТАТ                         │
├─────────────────────────────────────────────────────────────┤
│  Hrigoriu живе у місті Харків та працює на посаді «Лікар».  │
└─────────────────────────────────────────────────────────────┘
"""
# ==============================================
# Домашнє завдання №3
"""Написати програму, яка запитує дані пацієнта (ім'я, вік, зріст, вага) і виводить електронну медичну картку з розрахунком ІМТ та категорії ваги.
Створити Patient Card за зразком вище.
"""
from datetime import datetime, timezone


class PatientCard:
    "Електронна медична картка пацієнта."

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height  # см
        self.weight = weight  # кг
        self.created = datetime.now(timezone.utc).date()

    @staticmethod
    def get_number(prompt, is_float=False):
        while True:
            value = input(prompt)
            try:
                number = float(value) if is_float else int(value)
                if number <= 0:
                    print("   ↳ значення має бути додатним, спробуйте ще раз\n")
                    continue
                return number
            except ValueError:
                print("   ↳ це не схоже на число, спробуйте ще раз\n")

    @classmethod
    def from_input(cls):
        print("── Реєстрація нового пацієнта ──\n")

        name = input("👤  Прізвище та ім'я пацієнта: ").strip()
        while not name:
            name = input("   ↳ поле не може бути порожнім: ").strip()

        age = cls.get_number("🎂  Скільки пацієнту повних років: ")
        height = cls.get_number("📏  Зріст пацієнта (см): ", is_float=True)
        weight = cls.get_number("⚖️   Вага пацієнта (кг): ", is_float=True)

        return cls(name, age, height, weight)

    def calculate_bmi(self):
        height_m = self.height / 100
        return self.weight / (height_m**2)

    def bmi_category(self, bmi):
        if bmi < 18.5:
            return "недостатня вага", "🔵"
        elif bmi < 25:
            return "норма", "🟢"
        elif bmi < 30:
            return "надлишкова вага", "🟡"
        else:
            return "ожиріння", "🔴"

    def print_card(self):
        bmi = self.calculate_bmi()
        category, marker = self.bmi_category(bmi)

        rows = [
            ("Пацієнт", self.name),
            ("Вік", f"{self.age} р."),
            ("Зріст", f"{self.height} см"),
            ("Вага", f"{self.weight} кг"),
            ("ІМТ", f"{bmi:.1f}  {marker} {category}"),
            ("Дата огляду", self.created.strftime("%d.%m.%Y")),
        ]

        label_width = max(len(label) for label, _ in rows)
        value_width = max(len(value) for _, value in rows)
        width = label_width + value_width + 5

        print("\n" + "▄" * (width + 2))
        print("█" + " MEDICAL CARD · МЕДИЧНА КАРТКА ".center(width) + "█")
        print("▀" * (width + 2))
        for label, value in rows:
            print(f" {label.ljust(label_width)} │ {value}")
        print("─" * (width + 2))


# --- Запуск програми ---
patient = PatientCard.from_input()
patient.print_card()


"""
── Реєстрація нового пацієнта ──

👤  Прізвище та ім'я пацієнта: Шаров Григорій Олександрович
🎂  Скільки пацієнту повних років: 42
📏  Зріст пацієнта (см): 183
⚖️   Вага пацієнта (кг):  96,5
   ↳ це не схоже на число, спробуйте ще раз

⚖️   Вага пацієнта (кг):  96.5

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█       MEDICAL CARD · МЕДИЧНА КАРТКА        █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
 Пацієнт     │ Шаров Григорій Олександрович
 Вік         │ 42 р.
 Зріст       │ 183.0 см
 Вага        │ 96.5 кг
 ІМТ         │ 28.8  🟡 надлишкова вага
 Дата огляду │ 02.08.2026
──────────────────────────────────────────────
"""
# ==============================================

# Домашнє завдання №4
"""Написати програму, яка запитує ім'я та вік користувача і виводить повідомлення про те, скільки років буде користувачу через рік.
Програма має перевіряти, чи введено коректне значення віку (тобто число більше нуля). Якщо користувач введе некоректне значення, програма має вивести повідомлення про помилку та повторно запитати вік.
"""

def get_number(prompt):
    "Запитує число і перевіряє, чи введено коректне значення."
    while True:
        value = input(prompt)
        try:
            number = int(value)
            if number <= 0:
                print("⚠ Вік має бути більшим за нуль.\n")
                continue
            return number
        except ValueError:
            print("⚠ Помилка: введіть, будь ласка, число.\n")


def year_word(n):
    "Повертає правильну форму слова 'рік' залежно від числа."
    if 11 <= n % 100 <= 14:
        return "років"
    last_digit = n % 10
    if last_digit == 1:
        return "рік"
    elif 2 <= last_digit <= 4:
        return "роки"
    else:
        return "років"


# --- Збір даних ---
name = input("Введіть ваше ім'я: ").strip()
while not name:
    name = input("Ім'я не може бути порожнім. Введіть ім'я: ").strip()

age = get_number("Введіть ваш вік: ")

# --- Перетворення рядка в число ---
next_age = age + 1  # ключовий момент: input() повертає str, тому age має бути int,
# інакше age + 1 викличе помилку (не можна додати число до рядка)

# --- Формування повідомлення ---
lines = [
    f"Вітаю, {name}!",
    f"Через рік вам буде {next_age} {year_word(next_age)}.",
]

# --- Вивід у рамці ---
width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")


"""
Введіть ваше ім'я: Григорій
Введіть ваш вік: ваі
⚠ Помилка: введіть, будь ласка, число.

Введіть ваш вік: 45.6
⚠ Помилка: введіть, будь ласка, число.

Введіть ваш вік: 42

┌───────────────────────────────┐
│  Вітаю, Григорій!             │
│  Через рік вам буде 43 роки.  │
└───────────────────────────────┘
"""
# ==============================
