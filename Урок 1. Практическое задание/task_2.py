
__author__ = 'Юлия Павлова'
__group__ = 2547

"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

time_sec = float(input('Введите время в секундах'))
hour = time_sec / 3600
min = time_sec / 60
print(f'Время в формате ч:м:с - {hour} : {min} : {time_sec}')
