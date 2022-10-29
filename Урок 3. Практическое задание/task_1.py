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


def division(var_1, var_2):
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        return 'Вы что? Пытаетесь делить на 0!'


try:
    print(division(int(input('Введите первое число: ')), int(input('Введите второе число: '))))
except ValueError:
    print('Вы ввели не число!')
