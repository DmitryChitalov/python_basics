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


def s_calc(r_val, h_val):
    try:
        return r_val / h_val
    except ZeroDivisionError:
        return "What are you? Trying to divide by 0! "


r_val = float(input("Enter the number: "))
h_val = float(input("Enter the number: "))
print(s_calc(r_val, h_val))
