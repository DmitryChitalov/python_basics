"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroError(Exception):
    def __init__(self, catch_err):
        self.catch_err = catch_err


divident = float(input('Введите делимое: '))
try:
    divider = float(input('Введите делитель: '))
    if divider == 0:
        raise ZeroError('Делить на ноль нельзя!')
except ZeroError as zero_exception:
    print(zero_exception)
else:
    print(f' {round((divident / divider), 5)}')
