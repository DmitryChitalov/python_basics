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


def my_func(var1, var2):

    try:
        result = var1 / var2

    except ZeroDivisionError:
        print("Вы что? Пытаетесь делить на 0!")

    else:
        print(result)


user_var_1 = float(input("Введите первое число: "))
user_var_2 = float(input("Введите второе число: "))

my_func(user_var_1, user_var_2)
