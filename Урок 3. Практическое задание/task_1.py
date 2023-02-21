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
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

def division_func(first, second):
    try:
        first / second
    except ZeroDivisionError:
        return 'Вы что? Пытаетесь делить на 0!'
    return float(first / second)
print(division_func(first_number, second_number))