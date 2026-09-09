from patient_utils import is_adult, normalize_name

name = normalize_name("  ivan  ")

def main():
    print("Application started")


if __name__ == "__main__":
    main()
    print(name)
    print(is_adult(42))