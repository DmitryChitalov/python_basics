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


def my_division(a, b):
    """
    Функция для деления первого аргумента на второй. Результат округляется до второго знака после запятой.
    :param a: Делимое
    :param b: Делитель
    :return: Результат
    """
    res = None
    try:
        res = a / b

    except ZeroDivisionError:
        print("Вы что? Пытаетесь денить на 0!")
    return res


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if my_division(a, b) is not None:
    print(f"Результат: {my_division(a, b)}")
