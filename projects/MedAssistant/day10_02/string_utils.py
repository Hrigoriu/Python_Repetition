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