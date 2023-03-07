"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


number = int(input("Введите число: "))
divider = int(input("Введите делитель: "))
try:
    if divider == 0:
        raise MyZeroDivisionError('На 0 делить нельзя!')
    print(number/divider)
except MyZeroDivisionError as err:
    print(err)
