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

def division_numbers (arg_1,arg_2):
    """
    Функция деления
    :param arg_1: Делимое
    :param arg_2: Делитель
    :return: Частное
    """
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        return 'Вы что? Пытаетесь делить на 0!'

try:
    arg_1 = float(input("Введите первое число: "))
    arg_2 = float(input("Введите второе число: "))
except ValueError:
    print("Ошибочный ввод!")
else:
    print(division_numbers(arg_1,arg_2))
