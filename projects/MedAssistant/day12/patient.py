"""patient.py

The Patient object model for MedAssistant: state, validation, and
self-contained behavior (is_adult, is_fever, calculate_bmi, summary).
"""


class Patient:
    def __init__(
        self,
        id: int,
        name: str,
        age: int,
        diagnosis: str,
        temperature: float,
        weight: float,
        height: float,
    ):
        """Create a validated patient. Raises ValueError if anything is wrong.

        Collect-all validation: every field is checked, and ALL
        problems are reported together in a single ValueError.
        """
        errors = []
        errors += self._check_id(id)
        errors += self._check_name(name)
        errors += self._check_age(age)
        errors += self._check_diagnosis(diagnosis)
        errors += self._check_temperature(temperature)
        errors += self._check_weight(weight)
        errors += self._check_height(height)

        if errors:
            raise ValueError("Invalid patient data: " + "; ".join(errors))

        self.id = id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.temperature = temperature
        self.weight = weight
        self.height = height

    @staticmethod
    def _check_id(id) -> list[str]:
        if not isinstance(id, int) or isinstance(id, bool) or id <= 0:
            return [f"'id' must be a positive integer, got {id!r}"]
        return []

    @staticmethod
    def _check_name(name) -> list[str]:
        if not isinstance(name, str) or not name.strip():
            return [f"'name' cannot be empty, got {name!r}"]
        return []

    @staticmethod
    def _check_age(age) -> list[str]:
        if not isinstance(age, int) or isinstance(age, bool) or age <= 0:
            return [f"'age' must be a positive integer, got {age!r}"]
        return []

    @staticmethod
    def _check_diagnosis(diagnosis) -> list[str]:
        if not isinstance(diagnosis, str) or not diagnosis.strip():
            return [f"'diagnosis' cannot be empty, got {diagnosis!r}"]
        return []

    @staticmethod
    def _check_temperature(temperature) -> list[str]:
        if not isinstance(temperature, (int, float)) or isinstance(temperature, bool):
            return [f"'temperature' must be a number, got {temperature!r}"]
        if not (25.0 <= temperature <= 45.0):
            return [f"'temperature' must be in range 25.0-45.0, got {temperature}"]
        return []

    @staticmethod
    def _check_weight(weight) -> list[str]:
        if not isinstance(weight, (int, float)) or isinstance(weight, bool) or weight <= 0:
            return [f"'weight' must be a positive number, got {weight!r}"]
        return []

    @staticmethod
    def _check_height(height) -> list[str]:
        if not isinstance(height, (int, float)) or isinstance(height, bool) or height <= 0:
            return [f"'height' must be a positive number, got {height!r}"]
        return []

    def is_adult(self) -> bool:
        """Check whether this patient is 18 or older."""
        return self.age >= 18

    def is_fever(self) -> bool:
        """Check whether this patient's temperature indicates a fever."""
        return self.temperature >= 37.5

    def calculate_bmi(self) -> float:
        """Calculate this patient's BMI from its own weight/height.

        No arguments needed anymore — weight and height are now
        part of the patient's own state.
        """
        return self.weight / (self.height ** 2)

    def summary(self) -> str:
        """Build a short, human-readable summary of this patient."""
        adult_status = "adult" if self.is_adult() else "minor"
        fever_status = "has fever" if self.is_fever() else "no fever"
        bmi = self.calculate_bmi()
        return (
            f"#{self.id} {self.name} ({self.age}, {adult_status}) — "
            f"{self.diagnosis}, {self.temperature}°C ({fever_status}), BMI {bmi:.1f}"
        )

    @classmethod
    def from_dict(cls, data: dict) -> "Patient":
        """Build a Patient from a plain dict (e.g. one JSON record).

        This is the ONLY place that knows how to translate raw JSON
        keys into Patient's constructor — keeps that translation out
        of the loading code entirely.
        """
        return cls(
            id=data["id"],
            name=data["name"],
            age=data["age"],
            diagnosis=data["diagnosis"],
            temperature=data["temperature"],
            weight=data["weight"],
            height=data["height"],
        )

    def __repr__(self) -> str:
        return (
            f"Patient(id={self.id}, name={self.name!r}, age={self.age}, "
            f"diagnosis={self.diagnosis!r}, temperature={self.temperature}, "
            f"weight={self.weight}, height={self.height})"
        )