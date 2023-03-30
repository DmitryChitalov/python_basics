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
        arg1 = float(input("Введите первое число: "))
        arg2 = float(input("Введите второе число: "))
        result = arg1 / arg2
    except ZeroDivisionError:
        return "Вы что? Пытаетесь делить на 0!"
    return result

print(f"{my_func()}")