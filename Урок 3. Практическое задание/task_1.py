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

first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))


def func(first_number, second_number):
    try:
        result = first_number / second_number
        return result
    except ZeroDivisionError:
        return 'You can not divide by 0'


print(func(first_number, second_number))
