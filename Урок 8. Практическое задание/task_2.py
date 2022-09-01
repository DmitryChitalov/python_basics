"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DevByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        divisible = int(input('Введите делимое: '))
        divider = int(input('Введите делитель: '))
        if divider == 0:
            raise DevByZero("Делить на ноль нельзя!")
        else:
            result = divisible / divider
            return f'{result:.2f}'
    except DevByZero as error:
        return error


print(div())
