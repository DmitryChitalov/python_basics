"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

integers = input('Input two integers with a space: ').split()


def div(int_1, int_2):
    try:
        return int(int_1) / int(int_2)
    except ZeroDivisionError:
        print('Error! Zero division')
        return ''


print(div(integers[0], integers[1]))
