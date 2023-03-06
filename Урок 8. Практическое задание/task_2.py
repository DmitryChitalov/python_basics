"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

# pylint: disable=missing-class-docstring


class MyHandler(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input("Введите числитель: "))
b = int(input("Введите знаменатель: "))

try:
    if b == 0:
        raise MyHandler("Нельзя делить на 0")
except MyHandler as err:
    print(err)
else:
    print(a / b)
