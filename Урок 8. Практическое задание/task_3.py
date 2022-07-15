"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NumbersOnly(Exception):
    pass


numbers = []


def append_number(number_list: list):
    value = input("Input number: ")

    try:
        number_list.append(float(value))
    except ValueError:
        raise NumbersOnly(f"error '{value}' input")


while True:
    try:
        append_number(numbers)
    except NumbersOnly as exception:
        print(exception)
    except KeyboardInterrupt:
        print(f"\nList number = {numbers}")
        break
