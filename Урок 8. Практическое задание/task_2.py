"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivideByZeroException(Exception):
    def __init__(self, divided):
        self.divided = divided

    def __str__(self):
        return f'Attempt to divide {self.divided} to \'0\''


class DivisionByZero:
    @staticmethod
    def divide_by_null(divided, divider):
        try:
            return divided / divider
        except ZeroDivisionError:
            raise DivideByZeroException(divided)


try:
    print(DivisionByZero.divide_by_null(10, 0.1))
    print(DivisionByZero.divide_by_null(10, 0))
except DivideByZeroException as error:
    print(f"Unexpected {error=}, {type(error)=}, message: {error}")
