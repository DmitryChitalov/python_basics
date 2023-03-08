"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    def __init__(self, message):
        self.txt = message


class Calculator:
    def divide(self, numerator, denominator):
        if denominator == 0:
            raise MyZeroDivisionError("Нельзя делить на ноль")
        return numerator / denominator


calculator = Calculator()

try:
    numerator = float(input("Введите делимое: "))
    denominator = float(input("Введите делитель: "))
    result = calculator.divide(numerator, denominator)
    print("Результат:", result)
except MyZeroDivisionError as error:
    print("Ошибка:", error)
