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
def my_div(a, b):
    try:
        c = a / b
    except ZeroDivisionError:       # ошибка деления на ноль
        return print(f'Делить на 0 нельзя!')
    return c

try:
    n1 = int(input(f'Введите первое число: '))
    n2 = int(input(f'Введите второе число: '))
except ValueError:
    print(f'Введите числа')
else:
    print(my_div(n1, n2))
