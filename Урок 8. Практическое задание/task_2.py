"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""




class ZeroDivisionError(Exception):
    def __init__(self, text):
        self.text = text
def divider(x, y):
    if y == 0:
        raise ZeroDivisionError(f"{x} / {y} : Делить на ноль нельзя")
    return x / y
try:
    divider(15, 0)
except ZeroDivisionError as c:
    print(c)

