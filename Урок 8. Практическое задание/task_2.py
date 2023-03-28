"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class MyErrDivision(Exception):
    def __init__(self):
        self.txt = 'My division by zero'


def division():
    try:
        a = float(input('Dividend: '))
        b = float(input('Divisor: '))
        if b == 0:
            raise MyErrDivision
        print(f'a / b = {a / b: .4f}')
    except MyErrDivision as err:
        print(err.txt)


division()
