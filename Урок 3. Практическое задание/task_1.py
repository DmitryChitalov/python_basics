"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""

arg_1 = int(input('Число 1: '))
arg_2 = int(input('Число 2: '))


def my_func():
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        return 'На 0 делить нельзя!'


print(my_func())
