"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class NumErr(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        a = input("Введите значения: ")
        if a == "p":
            break
        if a.isnumeric() == True:
            my_list.append(a)
        else:
            raise NumErr("Введено не число")
        print(my_list)
    except NumErr as err:
        print(err)
