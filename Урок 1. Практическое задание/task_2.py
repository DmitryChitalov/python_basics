"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

"""ФИО Суслин Александр"""

unformatted_time = int(input("Enter time in seconds: "))

hours = unformatted_time // 3600
minutes = unformatted_time % 3600 // 60
seconds = unformatted_time % 3600 % 60

print(f"{unformatted_time} seconds it's: {hours}::{minutes}::{seconds}")
print(f"Or {unformatted_time / 3600}h : {unformatted_time / 60}m : {unformatted_time}s")
