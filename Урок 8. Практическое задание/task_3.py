"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NoNumberError(Exception):
    def __init__(self, message_error="Вам можно вводить только числа!"):
        self.message_error = message_error
        super().__init__(self.message_error)


def my_list():
    numbers_list = []
    while True:
        try:
            my_value = input("Введите число, или 'end' для завершения: ")
            if my_value == "end":
                break
            if not my_value.isdigit():
                raise NoNumberError
            numbers_list.append(int(my_value))
        except NoNumberError as my_error:
            print(my_error)
    return numbers_list


print(my_list())
