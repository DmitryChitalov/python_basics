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


def dev(a, b):
    try:
        return a / b
    except ZeroDivisionError:
       return "Не дели на ноль!"
try:
    a = int(input("введи 1 число"))
    b = int(input("введи 2 число"))
    print(dev(a, b))
except ValueError:
    print("Только число")
