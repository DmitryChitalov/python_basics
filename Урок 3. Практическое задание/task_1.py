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


def func_division(first_value, second_value):
    result = first_value / second_value
    return result


try:
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    print(func_division(first_number, second_number))
except ZeroDivisionError:
    print("Нельзя делить на 0!")
except ValueError:
    print("Вам нужно вводить числа!")
