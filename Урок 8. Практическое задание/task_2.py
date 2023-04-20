"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


def division():
    try:
        divisible = float(input("Введите делимое: "))
        divisor = float(input("Введите делитель: "))
        if divisor == 0:
            raise DivisionByZeroError("Делить на ноль нельзя!")
        else:
            print(f"{divisible}/{divisor}={divisible / divisor}")
    except DivisionByZeroError as e:
        print(e)
        division()


division()
