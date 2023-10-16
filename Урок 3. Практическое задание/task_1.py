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


def divide_numbers(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        print(f'Вы что? Пытаетесь делить на 0?!')


print(divide_numbers(int(input('Первое число: ')), 
                     int(input('Второе число: '))))