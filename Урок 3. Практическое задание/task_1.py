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


def division_fun(arg1, arg2):
    return arg1 / arg2


arg1 = float(input("Введите первое число: "))
arg2 = float(input("Ведите второе число: "))
try:
    res = division_fun(arg1, arg2)
except ZeroDivisionError:
    print("Деление на ноль запрещено !!!")
else:
    print(f"Результат: {res}")
