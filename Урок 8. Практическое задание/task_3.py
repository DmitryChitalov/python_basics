"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

import re


class MyExcept(Exception):
    def __init__(self, txt):
        self.txt = txt


sp = []
while True:
    try:
        a = input('Введите числовой элемент списка (exit - выход): ')
        if a == 'exit':
            print(sp)
            exit()
        if not re.findall(r'^[-]?[0-9]*[\.]?[0-9]*$', a):
            raise MyExcept('Вы ввели не число!')
        sp.append(a)
    except MyExcept as err:
        print(err)
