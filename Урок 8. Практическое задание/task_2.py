"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDevisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


divider = int(input('Введите делимое: '))
divisor = int(input('Введите делитель: '))


def MyDevide(divider, divisor):
    try:
        if divisor == 0:
            raise MyZeroDevisionError("На ноль делить нельзя!")
        else:
            res = divider / divisor
            return res
    except MyZeroDevisionError as err:
        return err


print(MyDevide(divider, divisor))
