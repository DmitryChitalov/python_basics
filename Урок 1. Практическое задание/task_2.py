"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
your_number = int(input("Time in seconds "))
a = your_number//3600
b = your_number//60
print(f"Time is hours: {a}, Time in minutes: {b}, Time in seconds: {your_number}")

