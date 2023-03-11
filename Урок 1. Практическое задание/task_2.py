"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
seconds_per_minute = 60
minutes_per_hour = 60
seconds_per_hour = minutes_per_hour * seconds_per_minute

seconds = int(input("Введите время в секундах: "))

hours = seconds // seconds_per_hour
minutes = seconds // seconds_per_minute

print(f"Время в формате ч: м: с - {hours} : {minutes} : {seconds}")
