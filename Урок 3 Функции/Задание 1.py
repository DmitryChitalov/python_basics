"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

integers = input('Input two integers with a space: ').split()


def divide(int_1, int_2):
    """
    Функция для деления чисел

    Принимает два параметра:
    int_1 - делимое
    int_2 - делитель
    (number, number) -> number

    #>>> print(divide(integers[0], integers[1]))
    Input two integers with a space: 4 5
    0.8
    """

    try:
        return int(int_1) / int(int_2)
    except ZeroDivisionError:
        print('Error! Zero division')
        return ''


print(divide(integers[0], integers[1]))
