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


def my_div(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        print("Вы что? Пытаетесь делить на 0!")
    except ValueError:
        print("Нужны числа а не буквы")


first_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")

my_div(first_number, second_number)
