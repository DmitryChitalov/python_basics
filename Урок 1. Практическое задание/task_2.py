"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
s = int(input('Введите время в секундах:'))
h = round(s/3600, 1)
m = round(s/60, 1)
print(f'Время в формате ч:м:с - {h} : {m} : {s}')
