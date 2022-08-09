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

first_number = int(input("Please enter the number to be divided:"))
second_number = int(input("Please enter the number to be the divisor:"))


def divide_numbers(dividend, divisor):
    """
    Returns value dividend divided by divisor
    :param dividend: Dividend
    :param divisor: Divisor
    :return: Result dividend divided by divisor
    """
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return "You can't divide by zero"


print(divide_numbers(first_number, second_number))
