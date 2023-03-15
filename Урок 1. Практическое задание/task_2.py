"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

user_num = int(input('Введите время в секундах: '))

minutes = user_num / 60
hours = minutes / 60

hours_correct = round(float(hours), 1)
minutes_correct = round(float(minutes), 1)

print(f'Время в формате ч:м:с - {hours_correct} : {minutes_correct} : {user_num}')
