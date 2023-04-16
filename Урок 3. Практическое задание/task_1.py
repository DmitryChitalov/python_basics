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

def div(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        return 'Так нельзя!'
    return result
try:
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))
    print(div(num1, num2))
except ValueError:
    print('Введите только числа!')