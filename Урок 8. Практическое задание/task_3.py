"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать
у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NonNumber(Exception):
    """info"""


def append_number(number_list: list):
    """info"""
    value = input("Введите число >>> ")

    try:
        number_list.append(float(value))
    except ValueError as error:
        raise NonNumber(f"Вы ввели '{value}' вместо числа") from error


numbers = []

while True:
    try:
        append_number(numbers)
    except NonNumber as exception:
        print(exception)
    except KeyboardInterrupt:
        print(f"\nСписок чисел = {numbers}")
        break
