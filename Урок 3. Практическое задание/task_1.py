"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division_function(arg1, arg2):
    """
    Функция реализует деление двух принимаемых чисел.
    """
    try:
        return arg1 / arg2
    except ZeroDivisionError:
        return "Деление на ноль запрещено"


divisible_var = int(input("Введите делимое: "))
divider_var = int(input("Введите делитель: "))
print(f"{division_function(divisible_var, divider_var)}")
