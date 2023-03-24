"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivisionError(Exception):
    def __init__(self, msg):
        self.msg = msg


try:
    dividend = int(input("Введите делимое: "))
    divisor = int(input("Введите делитель: "))
    if divisor == 0:
        raise ZeroDivisionError("Делите на ноль нельзя!")
except ZeroDivisionError as err:
    print(err)
else:
    print(f"Все хорошо. Ваш результат: {round(dividend / divisor, 2)}")