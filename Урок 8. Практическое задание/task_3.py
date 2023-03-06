"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

# pylint: disable=missing-class-docstring, singleton-comparison


class MyHandler(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        a = input("Введите значения: ")
        if a == "q":
            break
        if a.isnumeric() == True:
            my_list.append(a)
        else:
            raise MyHandler("Введено не число")
        print(my_list)
    except MyHandler as err:
        print(err)
