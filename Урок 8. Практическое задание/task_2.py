"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class Division:
    def __init__(self, divisible, divider):
        self.divisible = divisible
        self.divider = divider

    @staticmethod
    def divbyz(divisible, divider):
        try:
            return (divisible / divider)
        except:
            return "Делить на ноль, нельзя."


dd = Division
print(Division.divbyz(2, 0.2))
print(Division.divbyz(20, 0))
