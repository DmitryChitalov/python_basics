user_data=input("Введите число: ")
if user_data.isdigit():
    print(f"Ваше результат: {int(user_data)+int(user_data)*int(user_data)+int(user_data)*int(user_data)*int(user_data)}")
else: print("Ошибка ввода")