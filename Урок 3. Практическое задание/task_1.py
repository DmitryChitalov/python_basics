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


def f_devide(a, b):
    try:
        return int(a) / int(b)
    except Exception as ex:
        print(f"Error: {ex}")  # `Error: division by zero` if devider = 0
        return "Error"


devident = input("Введите первое число: ")
devider = input("Введите второе число: ")
print(f"Result: {f_devide(devident, devider)}")
