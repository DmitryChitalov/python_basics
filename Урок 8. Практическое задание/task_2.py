"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ExampleError(Exception):
    def __init__(self, txt):
        self.txt = txt


f_num = int(input('Введите первое число: '))
s_num = int(input('Введите второе число: '))

try:
    if s_num == 0:
        raise ExampleError('Вы ввели число 0')
    else:
        result = f_num / s_num
except ExampleError as err:
    print(err)
else:
    print(f'Ответ = {result}')
