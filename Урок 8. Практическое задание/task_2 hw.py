__author__ = 'AndreiM'
__version__ = "1.0 25.04.2023"
print("\n task_2 \n -------- \n")

class DivisionByNull:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    @staticmethod
    def divide_by_null(num, denom):
        try:
            return (num / denom)
        except ZeroDivisionError:
            return (f'Деление на нуль запрещено')


div = DivisionByNull(19, 100)
print('19 / 0   ', DivisionByNull.divide_by_null(19, 0))
print('19 / 0.1 ',DivisionByNull.divide_by_null(19, 0.1))
print('190 / 0  ', div.divide_by_null(190, 0))
print('0 / 190  ', div.divide_by_null(0, 190))


"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

