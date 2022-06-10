"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

import traceback


class MyZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


if __name__ == '__main__':

    def incorrect(a, b):
        if b == 0:
            raise MyZeroDivision('The second parameter is zero!')
        else:
            return a / b

    try:
        res = incorrect(5, 0)
    except ZeroDivisionError as e:
        print('Error:\n', traceback.format_exc())
    except MyZeroDivision as e:
        print('Error with my handler:\n', traceback.format_exc())
