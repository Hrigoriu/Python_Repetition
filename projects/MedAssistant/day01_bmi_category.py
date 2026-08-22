"""
Створи клас MedicalMeasurement.

Він повинен:

Patient:
Weight:
Height:
BMI:
Object ID:
Weight type:
Height type:
BMI type:

Вимоги:

використовувати @dataclass;
додати type hints;
BMI оформити як @property;
створити метод display();
вивести id() об'єкта;
перевіряти, що зріст і вага більші за нуль (можна через __post_init__).
"""

import json
from dataclasses import asdict, dataclass
from enum import Enum


class BMICategory(Enum):
    """Standard World Health Organization BMI classification categories."""

    UNDERWEIGHT = "Underweight"
    NORMAL = "Normal"
    OVERWEIGHT = "Overweight"
    OBESE = "Obese"


@dataclass
class MedicalMeasurement:
    """Represents a single patient measurement (weight, height) with BMI logic.

    Attributes:
        patient (str): Patient's name.
        weight (float): Patient's weight in kilograms.
        height (float): Patient's height in centimeters.
    """

    patient: str
    weight: float
    height: float

    def __post_init__(self) -> None:
        """Validate measurement values right after object creation.

        Raises:
            ValueError: If weight or height is not greater than zero.
        """
        if self.weight <= 0:
            raise ValueError("Weight must be greater than zero.")
        if self.height <= 0:
            raise ValueError("Height must be greater than zero.")

    @property
    def bmi(self) -> float:
        """Calculate patient's body mass index.

        Returns:
            float: BMI value, computed as weight(kg) / height(m)^2.
        """
        height_m = self.height / 100
        return self.weight / (height_m ** 2)

    @property
    def bmi_category(self) -> BMICategory:
        """Classify the current BMI value into a standard category.

        Returns:
            BMICategory: The category matching the current BMI value.
        """
        bmi = self.bmi
        if bmi < 18.5:
            return BMICategory.UNDERWEIGHT
        elif bmi < 25:
            return BMICategory.NORMAL
        elif bmi < 30:
            return BMICategory.OVERWEIGHT
        else:
            return BMICategory.OBESE

    def to_dict(self) -> dict:
        """Convert the measurement into a plain dictionary.

        Returns:
            dict: All fields plus computed BMI and category (as strings).
        """
        data = asdict(self)
        data["bmi"] = round(self.bmi, 1)
        data["bmi_category"] = self.bmi_category.value
        return data

    def to_json(self) -> str:
        """Serialize the measurement to a JSON-formatted string.

        Returns:
            str: JSON representation of the measurement.
        """
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)

    def __str__(self) -> str:
        """Return a short human-readable summary of the measurement.

        Returns:
            str: e.g. "Ivan: BMI 25.4 (Overweight)".
        """
        return f"{self.patient}: BMI {self.bmi:.1f} ({self.bmi_category.value})"

    def display(self) -> None:
        """Print a formatted, framed report of the measurement to the console."""
        lines = [
            f"Patient:      {self.patient}",
            f"Weight:       {self.weight} kg",
            f"Height:       {self.height} cm",
            f"BMI:          {self.bmi:.1f} ({self.bmi_category.value})",
            f"Object ID:    {id(self)}",
            f"Weight type:  {type(self.weight)}",
            f"Height type:  {type(self.height)}",
            f"BMI type:     {type(self.bmi)}",
        ]

        width = max(len(line) for line in lines) + 4

        print("\n┌" + "─" * width + "┐")
        print("│" + "  MEDICAL MEASUREMENT".center(width) + "│")
        print("├" + "─" * width + "┤")
        for line in lines:
            print("│  " + line.ljust(width - 2) + "│")
        print("└" + "─" * width + "┘")


# --- Usage example ---
measurement = MedicalMeasurement(patient="Ivan", weight=80.5, height=178)

measurement.display()
print(measurement)                 # uses __str__
print(measurement.to_dict())       # uses to_dict()
print(measurement.to_json())       # uses to_json()

# --- Validation example ---
try:
    bad_measurement = MedicalMeasurement(patient="Test", weight=-5, height=170)
except ValueError as e:
    print(f"\nError creating object: {e}")

"""
  
┌───────────────────────────────────┐
│         MEDICAL MEASUREMENT       │
├───────────────────────────────────┤
│  Patient:      Ivan               │
│  Weight:       80.5 kg            │
│  Height:       178 cm             │
│  BMI:          25.4 (Overweight)  │
│  Object ID:    2584590336416      │
│  Weight type:  <class 'float'>    │
│  Height type:  <class 'int'>      │
│  BMI type:     <class 'float'>    │
└───────────────────────────────────┘
Ivan: BMI 25.4 (Overweight)
{'patient': 'Ivan', 'weight': 80.5, 'height': 178, 'bmi': 25.4, 'bmi_category': 'Overweight'}
{
  "patient": "Ivan",
  "weight": 80.5,
  "height": 178,
  "bmi": 25.4,
  "bmi_category": "Overweight"
}

Error creating object: Weight must be greater than zero.
"""
