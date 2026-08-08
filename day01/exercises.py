# Практика №1
print("Мене звати ...")
print("Я вивчаю Python")
print("Я хочу стати AI Engineer")

# ==============================================

# Практика №2
name = input("Ваше ім'я: ")

print(f"Привіт, {name}!")

# ==============================================

# Практика №3

name = input("Ваше ім'я: ")
city = input("Ваше місто: ")

print(f"Мене звати, {name}")
print(f"Я живу у, {city}")
print("Приємно познайомитися!")

# ==============================================

# Практика №4


def get_number(prompt, is_float=False):
    "Запитує число і перевіряє, чи введено коректне значення."
    while True:
        value = input(prompt)
        try:
            if is_float:
                return float(value)
            else:
                return int(value)
        except ValueError:
            print("⚠ Помилка: введіть, будь ласка, число.\n")


# --- Збір даних ---
name = input("Введіть ваше ім'я: ")
age = get_number("Введіть ваш вік (років): ")
height = get_number("Введіть ваш зріст (см): ", is_float=True)
weight = get_number("Введіть вашу вагу (кг): ", is_float=True)

# --- Красивий вивід ---
lines = [
    f"Ім'я:   {name}",
    f"Вік:    {age} років",
    f"Зріст:  {height} см",
    f"Вага:   {weight} кг",
]

width = max(len(line) for line in lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  МІНІ-АНКЕТА".center(width) + "│")
print("├" + "─" * width + "┤")
for line in lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")


"""
Введіть ваше ім'я: Hrigoriu
Введіть ваш вік (років): 42.3
⚠ Помилка: введіть, будь ласка, число.

Введіть ваш вік (років): 42
Введіть ваш зріст (см): 185.6
Введіть вашу вагу (кг): 45.2

┌────────────────────┐
│     МІНІ-АНКЕТА    │
├────────────────────┤
│  Ім'я:   Hrigoriu  │
│  Вік:    42 років  │
│  Зріст:  185.6 см  │
│  Вага:   45.2 кг   │
└────────────────────┘
"""

# ==============================================

# Практика №5


class PatientCard:
    "Клас для зберігання даних пацієнта та виводу медичної картки."

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height  # у см
        self.weight = weight  # у кг

    @staticmethod
    def get_number(prompt, is_float=False):
        "Запитує число і перевіряє, чи введено коректне значення."
        while True:
            value = input(prompt)
            try:
                number = float(value) if is_float else int(value)
                if number <= 0:
                    print("⚠ Значення має бути більшим за нуль.\n")
                    continue
                return number
            except ValueError:
                print("⚠ Помилка: введіть, будь ласка, число.\n")

    @classmethod
    def from_input(cls):
        "Створює картку пацієнта на основі введених користувачем даних."
        name = input("Введіть ім'я: ").strip()
        while not name:
            name = input("Ім'я не може бути порожнім. Введіть ім'я: ").strip()

        age = cls.get_number("Вік: ")
        height = cls.get_number("Зріст (см): ", is_float=True)
        weight = cls.get_number("Вага (кг): ", is_float=True)

        return cls(name, age, height, weight)

    def calculate_bmi(self):
        "Розраховує індекс маси тіла (ІМТ)."
        height_m = self.height / 100
        return self.weight / (height_m**2)

    def bmi_category(self, bmi):
        "Визначає категорію за ІМТ."
        if bmi < 18.5:
            return "недостатня вага"
        elif bmi < 25:
            return "норма"
        elif bmi < 30:
            return "надлишкова вага"
        else:
            return "ожиріння"

    def display(self):
        "Виводить красиво оформлену медичну картку."
        bmi = self.calculate_bmi()
        category = self.bmi_category(bmi)

        lines = [
            f"Ім'я:   {self.name}",
            f"Вік:    {self.age} років",
            f"Зріст:  {self.height} см",
            f"Вага:   {self.weight} кг",
            f"ІМТ:    {bmi:.1f} ({category})",
        ]

        width = max(len(line) for line in lines) + 4

        print("\n╔" + "═" * width + "╗")
        print("║" + "  МЕДИЧНА КАРТКА".center(width) + "║")
        print("╠" + "═" * width + "╣")
        for line in lines:
            print("║  " + line.ljust(width - 2) + "║")
        print("╚" + "═" * width + "╝")


# --- Запуск програми ---
patient = PatientCard.from_input()
patient.print_card()


"""
Введіть ім'я: Hrigoriu
Вік: 42
Зріст (см): df
⚠ Помилка: введіть, будь ласка, число.

Зріст (см): 183
Вага (кг): 92

╔══════════════════════════════════╗
║           МЕДИЧНА КАРТКА         ║
╠══════════════════════════════════╣
║  Ім'я:   Hrigoriu                ║
║  Вік:    42 років                ║
║  Зріст:  183.0 см                ║
║  Вага:   92.0 кг                 ║
║  ІМТ:    27.5 (надлишкова вага)  ║
"""
# ==============================================
