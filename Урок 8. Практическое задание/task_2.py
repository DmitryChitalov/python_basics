"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


def smart_divider(a, b):
    if b == 0:
        raise DivisionByZeroError(f'{a} / {b} = Деление на ноль!')
    return a / b


try:
    smart_divider(6, 0)
except DivisionByZeroError as e:
    print(e)

print(f'45 / 5 = {smart_divider(45, 5)}')
