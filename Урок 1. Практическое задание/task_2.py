"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

time_in_second = int(input("Введите время в секундах: "))

hour = int(time_in_second / 3600)
minute = int(time_in_second % 3600 / 60)
second = int(time_in_second % 3600 % 60)
if hour < 10:
    hour = "0"+str(hour)
if minute < 10:
    minute = "0"+str(minute)
if second < 10:
    second = "0"+str(second)
print(f"Время в формате чч:мм:сс: {hour}:{minute}:{second}")
