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
    return int_var_1 / int_var_2


var_1 = input(f'Введите первое число: ')
var_2 = input(f'Введите второе число: ')
int_var_1 = int(var_1)
int_var_2 = int(var_2)

if int_var_2 == 0:
    print(f'На ноль делить нельзя')
else:
    answer = my_func(var_1, var_2)
    print(answer)
