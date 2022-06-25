"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class ListCheckError(Exception):

    def __str__(self):
        return 'Элемент не является числом'

lst = []

while True:
    num = input('Введите число ==>')
    try:
        if num.isdigit():
            lst.append(num)
            print(lst)
        else:
            raise ListCheckError()
    except ListCheckError as err:
        print(err)
    