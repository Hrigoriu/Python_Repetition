# 📊 Фірмовий вивід у рамці (Система пошуку):
# 💻 Інтерактивний код:
    
patients = ["Ivan", "Olena", "Petro", "Hanna"]
WIDTH = 44 

print("👋 Вітаємо в системі пошуку! (Натисніть Enter без вводу, щоб вийти)\n")

while True:
    # Запитуємо ввід користувача та очищаємо від зайвих пробілів
    search_name = input("Введіть ім'я пацієнта: ").strip()
    
    # Умова виходу: якщо нічого не ввели (просто натиснули Enter)
    if not search_name:
        print("Вихід із системи. Гарного дня! 🏥")
        break

    # 1. Логіка пошуку (наш for...else)
    for patient in patients:
        # Для зручності можна додати .lower() до обох змінних, щоб пошук не залежав від регістру:
        if patient.lower() == search_name.lower():
        #if patient == search_name:
            status_msg = "✅ Patient found"
            break
    else:
        status_msg = "❌ Patient not found"

    # 2. Формування та вивід рамки
    print("┌" + "─" * WIDTH + "┐")
    print("│" + "ПОШУК В БАЗІ ПАЦІЄНТІВ".center(WIDTH) + "│")
    print("├" + "─" * WIDTH + "┤")
    
    # Готуємо рядки з відступами зліва
    query_line = f"  Запит: {search_name}"
    status_line = f"  Статус: {status_msg}"
    
    # Виводимо їх, доповнюючи пробілами до потрібної ширини (ljust)
    print("│" + query_line.ljust(WIDTH) + "│")
    print("│" + status_line.ljust(WIDTH) + "│")
    
    print("└" + "─" * WIDTH + "┘\n")