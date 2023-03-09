"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class NewDivisionByNull(Exception):
    def __init__(self, message):
        self.txt = message


class Calc:
    def divide(self, number, desired):
        if desired == 0:
            raise NewDivisionByNull("На ноль делить нельзя!")
        return number / desired


calculator = Calc()

try:
    number = float(input("Введите число: "))
    desired = float(input("Введите делитель: "))
    result = calculator.divide(number, desired)
    print("Результат:", result)
except NewDivisionByNull as alarm:
    print("Внимание:", alarm)
