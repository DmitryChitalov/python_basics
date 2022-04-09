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

import string_extension

def number_division(dividend, divider):
    try:
        return dividend / divider
    except:
        print("Error: cannot be divided by 0")


input_dividend = input("Please, input your dividend: ")
input_divider = input("Please, input your divider: ")
if string_extension.is_float(input_dividend) and string_extension.is_float(input_divider):
    dividend = float(input_dividend)
    divider = float(input_divider)
    print(f"Division result: {number_division(dividend, divider)}")
else:
    print("Error: your input values is not a number")