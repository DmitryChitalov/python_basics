"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

"""
Выполенине! Емельяненко А.А.
"""


class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByNull(100, 1000)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))

#Альтернативное решение

class DivisionByNull(Exception):
    def __init__(self, txt):
        self.txt = txt


def divide_by_null(divider, denominator):
    try:
        if denominator == 0:
            raise DivisionByNull("Деление на ноль недопустимо")
        print(divider / denominator)
    except DivisionByNull as err:
        print(err)


divide_by_null(100, 10)
