"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
from AppData.Local.Programs.Python.Python310.Lib.datetime import datetime

sec = 3754
seconds = sec % 60
hour = sec // 3600 % 24
minutes = sec // 60 % 60
print(f"{hour}:{minutes}:{seconds}")
