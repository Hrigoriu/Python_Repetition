def normalize_name(name: str) -> str:
    return name.strip().title()


def is_adult(age: int) -> bool:
    return age >= 18

print("Loading patient module...")