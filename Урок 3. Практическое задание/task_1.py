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

def division(arg):
    try:
        dividend, divider = [int(_) for _ in arg]
        return f'{dividend / divider:.2f}'
    except ZeroDivisionError:
        print('Вы что? Пытаетесь делить на 0!')
    except ValueError:
        print('Не хватает значения')


print(division(input('Введите делимое и делитель: ').split()))