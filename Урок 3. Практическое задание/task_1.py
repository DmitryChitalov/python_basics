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

def my_func(*args):

    try:
        arg1 = int(input('Введите первое число: '))
        arg2 = int(input('Введите второе число: '))
        res = arg1 / arg2
    except ValueError:
        return 'Неверное значение'
    except ZeroDivisionError:
        return 'Вы что? Пытаетесь делить на 0!'

    return res

print(f'result  {my_func()}')
