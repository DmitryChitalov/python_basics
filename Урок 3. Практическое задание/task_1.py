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
def separator(num_divisible, num_divider):
    try:
        return num_divisible / num_divider
    except ZeroDivisionError:
        return 'Вы что? Пытаетесь делить на 0!'


divisible = int(input('Введите первое число :'))
divider = int(input('Введите второе число :'))

print(separator(divisible, divider))

print(separator(10, 20))

print(separator(10, 0))