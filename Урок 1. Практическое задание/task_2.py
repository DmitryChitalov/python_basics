"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

user_input = int(input("Please enter time in seconds:"))
hours = 00
minutes = 00
seconds = 00

if user_input < 0:
    print("Very funny -_-")
    exit()

hours = user_input // 3600
remainder = user_input - hours * 3600
minutes = remainder // 60
seconds = remainder % 60

print(f"{hours}:{minutes}:{seconds}")