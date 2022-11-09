"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyError(Exception):
    def __init__(self, data):
        self.data = data

number_1 = input('введите первое число:')
number_2 = input('введите второе число:')

try:
    number_1 = int(number_1)
    number_2 = int(number_2)
    if number_2 == 0:
        raise MyError("На ноль делить нельзя")
    result_n = number_1/number_2
except MyError as err:
    print(err)
else:
    print(f'Результат операции :{result_n}')

