"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByZeroException(Exception):
    def __init__(self, message="Деление на 0 невозможно"):
        self.message = message
        super().__init__(self.message)


def divide_by_zero(div, den):
    try:
        if den == 0:
            raise DivisionByZeroException()
        print(div / den)
    except DivisionByZeroException as err:
        print(err)


print(divide_by_zero(25, 0))
