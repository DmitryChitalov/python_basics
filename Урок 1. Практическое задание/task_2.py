"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

time_in_sec = int(input("Введите время в секундах: "))
time_in_hour = time_in_sec // 3600
time_in_min = time_in_sec // 60

# Вариант 1
print("\nВариант 1:\n")
print(
    f"Время в формате ч:м:с - {time_in_hour} : {time_in_min} : {time_in_sec}")
print("---------------------\n")

# Вариант 2
print("Вариант 2:\n")
format_sec = time_in_sec % 60
format_hour = time_in_sec // 3600
format_min = (time_in_sec - (format_hour * 3600)) // 60

print(f"Время в формате ч:м:с - {format_hour}:{format_min}:{format_sec}")
