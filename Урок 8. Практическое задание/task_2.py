"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class DivByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return divider / denominator
        except ZeroDivisionError:
            return f"Деление на ноль недопустимо"


div = DivByNull(7, 77)
print(DivByNull.divide_by_null(7, 0))
print(DivByNull.divide_by_null(7, 0.1))
print(div.divide_by_null(77, 1))