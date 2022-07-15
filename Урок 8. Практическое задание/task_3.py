"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NotNumbersOwn(Exception):
    def __init__(self, text):
        self.text = text


my_list = []

while True:
    line = input("Введите число: ")
    if line == "stop":
        break
    else:
        try:
            if line.isnumeric():
                my_list.append(int(line))
            else:
                raise NotNumbersOwn("Переданное значение не является числом")
        except NotNumbersOwn as e:
            print(e)

if len(my_list) > 0:
    print(my_list)
