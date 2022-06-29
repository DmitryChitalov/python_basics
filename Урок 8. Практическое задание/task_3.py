"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NumberError(ValueError):
    def __init__(self, message="Символ не число"):
        self.message = message
        super().__init__(self.message)


def number_filter(symbol):
    try:
        if symbol.isdigit():
            return symbol
        else:
            raise NumberError()
    except NumberError as err:
        print(err)


input_txt = ''
numbers_list = []

print("Вводите числа по одному. Для выхода введите 'stop'")

while input_txt != 'stop':
    input_txt = input()
    numbers_list.append(number_filter(input_txt))

print(f"Result list:\n{numbers_list}")
