user_time = input("Введите время в секундах: ")
print(f"Ваше время: {int(user_time) // 3600}:{(int(user_time) % 3600) // 60}:{(int(user_time) % 3600) % 60}")
