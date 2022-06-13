"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivideByZero(Exception):
    pass


try:
    number_1 = int(input('Введите делимое число: '))
    number_2 = int(input('Введите число делитель: '))
    if number_2 == 0:
        raise DivideByZero('Вы пытаетесь разделить на ноль!')
    result = number_1 / number_2
except ValueError:
    print('Вы ввели не число')
except DivideByZero as err:
    print(err)
else:
    print(f'{number_1} / {number_2} = {round(result, 2)}')
