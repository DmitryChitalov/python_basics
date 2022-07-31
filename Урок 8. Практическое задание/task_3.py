"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class ListExcept(Exception):
    def __init__(self, txt):
        self.txt = txt


numb_lst = []
while True:
    try:
        numbs = input("Введите число или '~' для выхода: ")
        if numbs == '~':
            break
        elif numbs.isdigit():
            numb_lst.append(int(numbs))
        else:
            raise ListExcept("Введите число!")
    except ListExcept as err:
        print(err.txt)

print(numb_lst)
