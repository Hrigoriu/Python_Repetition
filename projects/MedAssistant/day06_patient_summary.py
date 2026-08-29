"""patient_summary.py

Three composable functions for MedAssistant, demonstrating function
composition: each function does ONE job, and the top-level function
orchestrates them without duplicating their logic.

    calculate_bmi()
          ↓  (returns a float)
    bmi_category()
          ↓  (returns a str)
    create_patient_summary()
          ↓  (returns the final formatted report)
    "Patient: Ivan / Age: 42 / BMI: 25.3 / Category: Overweight"
"""


def calculate_bmi(weight: float, height: float) -> float:
    """Calculate BMI from weight (kg) and height (cm).

    Args:
        weight: Patient's weight in kilograms. Must be > 0.
        height: Patient's height in centimeters. Must be > 0.

    Returns:
        float: The raw, unrounded BMI value.
    """
    assert weight > 0, "weight must be greater than 0"
    assert height > 0, "height must be greater than 0"

    height_m = height / 100
    return weight / (height_m ** 2)


def bmi_category(bmi: float) -> str:
    """Classify a BMI value into a standard category.

    Args:
        bmi: A BMI value, typically from calculate_bmi().

    Returns:
        str: "Underweight", "Normal", "Overweight", or "Obesity".
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def create_patient_summary(
    name: str,
    age: int,
    weight: float,
    height: float,
) -> str:
    """Build a formatted patient summary.

    Orchestrates calculate_bmi() and bmi_category() — it does NOT
    recompute BMI logic or reimplement category thresholds itself.
    This is the "function → function → function → final result"
    chain: each step's output becomes the next step's input.

    Args:
        name: Patient's name.
        age: Patient's age in years.
        weight: Patient's weight in kilograms.
        height: Patient's height in centimeters.

    Returns:
        str: A multi-line summary report.
    """
    bmi = calculate_bmi(weight, height)         # step 1 → float
    category = bmi_category(bmi)                # step 2 → str (uses step 1's output)

    return (                                    # step 3 → final formatted string
        f"Patient: {name}\n"
        f"Age: {age}\n"
        f"BMI: {bmi:.1f}\n"
        f"Category: {category}"
    )


# --- Demo ---
patients = [
    ("Ivan", 42, 82, 180),
    ("Olena", 35, 55, 165),
    ("Petro", 58, 95, 175),
]

summaries = [create_patient_summary(*p) for p in patients]

# --- Framed output ---
all_lines = []
for summary in summaries:
    all_lines.extend(summary.split("\n"))
    all_lines.append("─" * 20)
all_lines.pop()   # drop the trailing separator

width = max(len(line) for line in all_lines) + 4

print("\n┌" + "─" * width + "┐")
print("│" + "  PATIENT SUMMARIES".center(width) + "│")
print("├" + "─" * width + "┤")
for line in all_lines:
    print("│  " + line.ljust(width - 2) + "│")
print("└" + "─" * width + "┘")

"""
┌────────────────────────┐
│    PATIENT SUMMARIES   │
├────────────────────────┤
│  Patient: Ivan         │
│  Age: 42               │
│  BMI: 25.3             │
│  Category: Overweight  │
│  ────────────────────  │
│  Patient: Olena        │
│  Age: 35               │
│  BMI: 20.2             │
│  Category: Normal      │
│  ────────────────────  │
│  Patient: Petro        │
│  Age: 58               │
│  BMI: 31.0             │
│  Category: Obesity     │
└────────────────────────┘
"""

"""
Ланцюжок композиції, викладений явно:
def create_patient_summary(name, age, weight, height):
    bmi = calculate_bmi(weight, height)     # ① weight, height → float
    category = bmi_category(bmi)            # ② that float → str
    return f"...{bmi:.1f}...{category}..."  # ③ both combined → final string

Функція «create_patient_summary()» ніколи не перераховує значення «weight / (height/100)**2» і ніколи не перезаписує порогові значення < 18,5 / < 25 / < 30 — вона просто викликає дві функції, які вже вміють це робити, і передає дані між ними. Це DRY у найчистішому вигляді: формула ІМТ та порогові значення категорій існують саме в одному місці у всій програмі.

Чому це важливо — що станеться, якщо ви, навпаки, продублюєте цю логіку:

# ❌ ПОГАНО — дублювання логіки:
def create_patient_summary(name, age, weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)              # ← дублікат calculate_bmi()
    if bmi < 18.5:                              # ← дублікат bmi_category()
        category = "Underweight"
    # ...

# А тепер уявіть, що клініка вирішила, що для категорій BMI слід використовувати
# дещо інші порогові значення, запропоновані ВООЗ. Вам доведеться знайти й виправити цю
# логіку в КОЖНІЙ функції, де вона повторюється — легко пропустити одну,
# і тоді різні частини програми перестануть узгоджуватися між собою.

Чому *p у create_patient_summary(*p): 
p — це кортеж, наприклад, («Ivan», 42, 82, 180). 
Символ * розпаковує його на чотири окремі позиційні аргументи — це той самий механізм розпакування, що й у *args, тільки тут він використовується у зворотному напрямку 
(розподіляючи кортеж, а не об’єднуючи аргументи в один).
"""