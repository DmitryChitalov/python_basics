"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_divident = float(input('Введите делимое: '))
inp_divisor = float(input('Введите делитель: '))

try:
    if inp_divisor == 0:
        raise OwnError("Делитель на ноль нельзя!")
    result = inp_divident/inp_divisor
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Результат деления: {result}")
