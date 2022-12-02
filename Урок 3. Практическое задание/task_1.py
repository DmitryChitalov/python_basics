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

def my_func():
    f_dig = float(input("Укажите первое число: "))
    s_dig = float(input("Укажите второе число: "))
    try:
        div = f_dig / s_dig
        return div
    except ZeroDivisionError:
        div = "Ошибка, деление на 0"
        return div
print(my_func())
