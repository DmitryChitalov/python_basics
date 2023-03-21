"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ExDivideByZero(Exception):
    pass


try:
    number = int(input('Введите число: '))
    divider = int(input('Введите делитель: '))
    if divider == 0:
        raise ExDivideByZero('На ноль делить нельзя!')
    result = number / divider
except ValueError:
    print('Вы ввели не число')
except ExDivideByZero as error:
    print(error)
else:
    print(f'{number} / {divider} = {round(result, 2)}')
