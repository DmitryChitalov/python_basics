"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class MyIntOnlyFilter(Exception):
    def __init__(self, txt):
        self.txt = txt


def fill_list():
    my_list = []
    print(f'Для завершения программы введите \'^\'')

    while True:
        el = input("Введите число: ")
        if el == "^":
            break
        try:
            if not el.isnumeric():
                raise MyIntOnlyFilter(f"'{el}' - не является числом!")
            my_list.append(el)
        except MyIntOnlyFilter as error:
            print(error)
    print(f'Результат: {my_list}')


fill_list()
