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


def division(dividend, divider):
    try:
        result = dividend / divider
        return result
    except ZeroDivisionError:
        print("Вы что? Пытаетесь делить на 0!")


num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
res = division(num_1, num_2)
print(res)
