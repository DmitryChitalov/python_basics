"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class OwnZeroDivisionError(Exception):

    def __str__(self):
        return 'Вы пытаетесь поделить на ноль'

while True:
    num_1 = int(input('Введите делимое ==>'))
    num_2 = int(input('Введите делитель ==>'))
    try:
        if num_2 == 0:
            raise OwnZeroDivisionError()
        print('Результат деления -', num_1 / num_2)
    except OwnZeroDivisionError as err:
        print(err)
    