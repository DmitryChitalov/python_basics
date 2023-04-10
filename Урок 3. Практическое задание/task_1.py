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


def div_number(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print('Вы что? Пытаетесь делить на 0!')


first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))
rezult = div_number(first_number, second_number)
if rezult is not None:
    print(rezult)
