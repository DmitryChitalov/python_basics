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


def division(first, second):
    res = first / second
    return res


a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))

try:
    print(division(a, b))
except ZeroDivisionError:
    print("Вы что? Пытаетесь делить на 0!")
