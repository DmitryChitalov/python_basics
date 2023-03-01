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

def division(a, b):
    """
    Возвращает результат деления числа a на число b
    (number, number) -> number
    >>> division(10, 2)
    5
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Вы что? Пытаетесь делить на 0!"

print(division(11, 0))
