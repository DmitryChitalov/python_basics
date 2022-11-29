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

def division_num(arg_1, arg_2):
    """ Функция деления чисел """
    if arg_1 == str(arg_1) or arg_2 == str(arg_2):
        return "Что-то из аргументов не является числом"
    else:
        try:
            return arg_1 / arg_2
        except ZeroDivisionError:
            return "Вы что? Пытаетесь делить на 0!"


print(division_num(5, 10))
