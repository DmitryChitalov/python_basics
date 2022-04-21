"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NoDigitError(ValueError):
    def __init__(self, txt):
        self.txt = txt


my_list = []
next_element = ""

while next_element != "q":
    next_element = input("Введите следующий элемент списка (или \'q\'для выхода): ")
    try:
        if next_element.isdigit():
            next_element = int(next_element)
        else:
            if next_element != "q":
                raise NoDigitError("Элемент не является числом")

    except NoDigitError as err:
        print(err)
    else:
        if next_element != "q":
            my_list.append(next_element)


print(my_list)