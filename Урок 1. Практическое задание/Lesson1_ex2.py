user_time=input("Введите время в секундах: ")
if user_time.isdigit():
    print(f"Ваше время: {int(user_time)//3600}:{(int(user_time)%3600)//60}:{(int(user_time)%3600)%60}")
else: print("Ошибка ввода")

