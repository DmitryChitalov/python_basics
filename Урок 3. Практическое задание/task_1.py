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

a = int(input("input first num: "))
b = int(input("input second num: "))


def my_div(p1, p2):
    return p1 / p2


try:
    print(f"{a} / {b} = {my_div(a, b)}")
except ZeroDivisionError:
    print("[!] - division by zero")
