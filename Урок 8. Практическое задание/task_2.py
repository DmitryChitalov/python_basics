"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class ZeroDivision:
    def __init__(self, divider, divisible):
        self.divider = divider
        self.divisible = divisible

    @staticmethod
    def zero_division(divider, divisible):
        try:
            return (divisible / divider)
        
        except:
            return 'Ошибка деления на ноль'


number = ZeroDivision(100, 10)
print(ZeroDivision.zero_division(0, 10))
print(ZeroDivision.zero_division(0.1, 10))
print(number.zero_division(0, 100))
