"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionZero:
    def __init__(self, divisible, divisor):
        self.divisible = divisible
        self.divisor = divisor

    @staticmethod
    def division(divisible, divisor):
        try:
            return (divisible / divisor)
        except:
            return ("Вы что?! Пытаетесь делить на ноль?")


divisible = int(input("Введите делимое: "))
divisor = int(input("Введите делитель: "))
print(f"Частное = {DivisionZero.division(divisible, divisor)}")
