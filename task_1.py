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


def my_func(var_1, var_2):
    try:
        var_1 / var_2
    except ZeroDivisionError:
        print('Введено значение 0. Ошибка ввода')
        return
    my_res = var_1 / var_2
    return my_res


print(my_func(float(input('Введите числитель: ')), float(input('Введите '
                                                               'знаменатель:'
                                                               ' '))))
