"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
time_in_sec = int(input('Введите время в секундах: '))
seconds = time_in_sec % 60
minutes = time_in_sec // 60 % 60
hours = time_in_sec // 60 // 60

print(f'{time_in_sec} секунд, это {hours} часов, {minutes} минут, {seconds} секунд')
print(f'Время в формате ч:м:с - {round(time_in_sec / 60 / 60, 2)} : {round(time_in_sec / 60, 2)} : {time_in_sec}')
