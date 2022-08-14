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


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Вы что? Пытаетесь делить на 0!')
        raise ZeroDivisionError

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(divide(a, b))
