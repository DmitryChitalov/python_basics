"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
sec = int(input('Enter time amount in secons ==>'))
print(f'Время в формате ч:м:с - {sec / 3600} : {sec / 60} : {sec}')

msg = '''

P.S.
Сначала я думал, что решение этой задачи должно конвертировать число секунд в указанный формат и выглядеть так:

'''
from datetime import timedelta
print(msg)
sec = int(input('Enter time amount in secons again ==>'))
time_delta = timedelta(seconds=sec)
print(f'Время в формате ч:м:с - {time_delta}')
