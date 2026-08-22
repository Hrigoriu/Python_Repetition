"""medical_note.py

A module for storing, cleaning, and analyzing free-text medical notes
within the MedAssistant project.
"""

import json
from dataclasses import asdict, dataclass
from enum import Enum


class SymptomKeyword(Enum):
    """Symptom keywords that MedicalNote can detect in free text."""

    PAIN = "pain"
    FEVER = "fever"
    COUGH = "cough"
    SINUSITIS = "sinusitis"


@dataclass
class MedicalNote:
    """Represents a single free-text medical note left by a clinician.

    Attributes:
        text (str): The raw note text. Automatically cleaned of extra
            whitespace on creation.
    """

    text: str

    def __post_init__(self) -> None:
        """Normalize whitespace right after object creation.

        Strips leading/trailing spaces and collapses any run of internal
        whitespace (spaces, tabs, newlines) down to a single space.

        Raises:
            ValueError: If the note is empty after cleaning.
        """
        self.text = " ".join(self.text.split())
        if not self.text:
            raise ValueError("Medical note text cannot be empty.")

    @property
    def char_count(self) -> int:
        """Return the number of characters in the cleaned text.

        Returns:
            int: Character count.
        """
        return len(self.text)

    @property
    def word_count(self) -> int:
        """Return the number of words in the cleaned text.

        Returns:
            int: Word count, based on whitespace splitting.
        """
        return len(self.text.split())

    @property
    def lowercase_text(self) -> str:
        """Return the note text in lowercase.

        Returns:
            str: Lowercased version of the cleaned text.
        """
        return self.text.lower()

    def find_symptoms(self) -> list[SymptomKeyword]:
        """Search the note for known symptom keywords.

        Returns:
            list[SymptomKeyword]: Symptoms found in the text, in the
                order defined by SymptomKeyword.
        """
        lowered = self.lowercase_text
        return [
            symptom
            for symptom in SymptomKeyword
            if symptom.value in lowered
        ]

    def to_dict(self) -> dict:
        """Convert the note into a plain dictionary.

        Returns:
            dict: Text plus computed stats (char/word count, symptoms found).
        """
        data = asdict(self)
        data["char_count"] = self.char_count
        data["word_count"] = self.word_count
        data["symptoms_found"] = [s.value for s in self.find_symptoms()]
        return data

    def to_json(self) -> str:
        """Serialize the note to a JSON-formatted string.

        Returns:
            str: JSON representation of the note.
        """
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)

    def __str__(self) -> str:
        """Return a short human-readable summary of the note.

        Returns:
            str: e.g. "12 words, symptoms: fever, sinusitis".
        """
        symptoms = self.find_symptoms()
        symptom_list = ", ".join(s.value for s in symptoms) if symptoms else "none"
        return f"{self.word_count} words, symptoms: {symptom_list}"

    def display(self) -> None:
        """Print a formatted, framed report of the note to the console."""
        symptoms = self.find_symptoms()

        lines = [
            f"Text:      {self.text}",
            f"Characters: {self.char_count}",
            f"Words:      {self.word_count}",
            "Symptoms found:",
        ]
        if symptoms:
            lines += [f"  - {s.value}" for s in symptoms]
        else:
            lines.append("  (none)")

        width = max(len(line) for line in lines) + 4

        print("\n┌" + "─" * width + "┐")
        print("│" + "  MEDICAL NOTE".center(width) + "│")
        print("├" + "─" * width + "┤")
        for line in lines:
            print("│  " + line.ljust(width - 2) + "│")
        print("└" + "─" * width + "┘")


# --- Usage example ---
if __name__ == "__main__":
    note = MedicalNote(" Patient complains of fever and sinusitis. ")

    note.display()
    print(note)                # uses __str__
    print(note.to_dict())      # uses to_dict()
    print(note.to_json())      # uses to_json()

"""
┌────────────────────────────────────────────────────────┐
│                       MEDICAL NOTE                     │
├────────────────────────────────────────────────────────┤
│  Text:      Patient complains of fever and sinusitis.  │
│  Characters: 41                                        │
│  Words:      6                                         │
│  Symptoms found:                                       │
│    - fever                                             │
│    - sinusitis                                         │
└────────────────────────────────────────────────────────┘
6 words, symptoms: fever, sinusitis
{'text': 'Patient complains of fever and sinusitis.', 'char_count': 41, 'word_count': 6, 'symptoms_found': ['fever', 'sinusitis']}
{
  "text": "Patient complains of fever and sinusitis.",
  "char_count": 41,
  "word_count": 6,
  "symptoms_found": [
    "fever",
    "sinusitis"
  ]
}
"""

"""
Що додано і чому саме так:

SymptomKeyword(Enum) — той самий підхід, що й BMICategory у минулому завданні: замість "магічних рядків" типу "fever", розкиданих по коду, всі ключові симптоми зібрані в одному місці. Якщо завтра захочеш додати HEADACHE = "headache" — правиш лише тут, і find_symptoms() автоматично її підхопить (бо for symptom in SymptomKeyword перебирає всі значення enum).

@dataclass + __post_init__ — оригінальний __init__ робив text.strip(). Я замінив на " ".join(text.
split()), бо це прибирає і зайві пробіли по краях, і подвійні пробіли всередині (як у Практиці №2). Додав перевірку на порожній текст після очищення — інакше word_count міг би обчислюватись для "порожнього" пацієнтського запису, що не має сенсу.

Три властивості (@property) — char_count, word_count, lowercase_text — обчислюються "на льоту" з self.text, а не зберігаються окремо. Це гарантує, що вони завжди синхронізовані з поточним текстом.

find_symptoms() — повертає список об'єктів SymptomKeyword (не рядків!), що дозволяє далі типобезпечно працювати з результатом (наприклад, if SymptomKeyword.FEVER in note.find_symptoms()).

to_dict() / to_json() / __str__() / display() — той самий поділ відповідальностей, що й у MedicalMeasurement: структуровані дані окремо від "красивого" консольного виводу.
"""
