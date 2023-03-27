"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class ValueError(Exception):
    def __init__(self, msg):
        self.msg = msg


l = []
while True:
    i = input('Введите число: ')
    if i != '':
        try:
            if not i.isnumeric():
                raise ValueError('Вы ввели не число!')
        except ValueError as err:
            print(err)
        else:
            l.append(i)
    else:
        break

print(l)