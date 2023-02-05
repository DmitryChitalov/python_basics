"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
time_seconds = int(input("enter seconds: "))
hours = time_seconds // 3600
minutes = time_seconds // 60 - hours * 60
seconds = time_seconds - hours * 3600 - minutes * 60
if hours >= 10:
    if minutes >= 10:
        if seconds >= 10:
            print(f'Время: {hours}:{minutes}:{seconds}')
        else:
            print(f'Время: {hours}:{minutes}:{0}{seconds}')
    if minutes < 10:
        if seconds >= 10:
            print(f'Время: {hours}:{0}{minutes}:{seconds}')
        else:
            print(f'Время: {hours}:{0}{minutes}:{0}{seconds}')
if hours < 10:
    if minutes >= 10:
        if seconds >= 10:
            print(f'Время: {0}{hours}:{minutes}:{seconds}')
        else:
            print(f'Время: {0}{hours}:{minutes}:{0}{seconds}')
    if minutes < 10:
        if seconds >= 10:
            print(f'Время: {0}{hours}:{0}{minutes}:{seconds}')
        else:
            print(f'Время: {0}{hours}:{0}{minutes}:{0}{seconds}')
