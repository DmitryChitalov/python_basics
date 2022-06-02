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


def div(num, den):
    try:
        return num / den
    except ZeroDivisionError:
        return 'Вы что? Пытаетесь делить на 0!'


try:
    input_num = int(input('Введите первое число: '))
    input_den = int(input('Введите второе число: '))
    print(div(input_num, input_den))
except ValueError:
    print('Пожалуйста, введите числа!')
