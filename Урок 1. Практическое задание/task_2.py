"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

enter_time = int(input('Enter time in seconds '))
hours = enter_time / 3600
minutes = enter_time / 60
seconds = enter_time
print(f'Time in h:m:s - {hours} : {minutes} : {seconds}')

"""
Другое решение

enter_time = int(input('Enter time in seconds '))
hours = enter_time // 3600
rest_time = enter_time % 3600
minutes = rest_time // 60
secs = rest_time % 60
print(f'{enter_time} sec is {hours} hours {minutes} minutes {secs} seconds')
"""
