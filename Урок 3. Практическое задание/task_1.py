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


def divide(arg1, arg2):
    if arg2 == 0:
        print("На ноль делить нельзя!")
        exit(1)
    return arg1 / arg2


first = int(input("Введите первое число:"))
second = int(input("Введите второе число:"))

print("Результат деления чисел:", divide(first, second))
