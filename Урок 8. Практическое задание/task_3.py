"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class NumberValidationError(Exception):
    def __init__(self, value):
        self.message = f"{value} is not a number"
        super().__init__(self.message)


# data = input("Input numbers, separated by space: ")
list = []


def check(value):
    try:
        val = int(value)
    except ValueError:
        raise NumberValidationError(value)

    return val


while True:
    data = input("Input value. Leave empty to finish: ")
    if data == '':
        break

    try:
        list.append(check(data))
    except NumberValidationError:
        pass

print(f"Result list of numbers: {list}")
