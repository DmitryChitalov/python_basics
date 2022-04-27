"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

input_value = input("Input integer value ")
# Проверяем что строка состоит из цифр
if str.isdigit(input_value):
    seconds_value = int(input_value)
    # Вычисляем количество полных часов
    hour = seconds_value // 3600
    # Вычисляем количество минут без учёта полных часов
    minutes = (seconds_value % 3600) // 60
    # Вычисляем количество секунд без учёта полных часов и минут
    seconds = (seconds_value % 3600) % 60
    print(f"Total time is {hour}:{minutes}:{seconds}")
    
    # Вычисляем количество часов и минут
    total_hour = seconds_value / 3600
    total_minutes = seconds_value / 60
    print(f"Total hour is {total_hour}\nTotal minutes is {total_minutes}\nTotal seconds is {seconds_value}")
else:
    print(f"Error: your value is not a integer number")