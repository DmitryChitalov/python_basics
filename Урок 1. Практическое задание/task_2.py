"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
seconds = None
while not (isinstance(seconds, str) and seconds.isdigit()):
    seconds = input('Введите время в секундах: ')
seconds = int(seconds)

m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print('{:d}:{:02d}:{:02d}'.format(h, m, s))