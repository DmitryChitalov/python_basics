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


def func_division(arg_1, arg_2):
    try:
        results_func_d = arg_1 / arg_2
    except ZeroDivisionError:
        return print("Вы пытаетесь делить на 0")
    results_func_d = arg_1 / arg_2
    return results_func_d


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(func_division(a, b))
