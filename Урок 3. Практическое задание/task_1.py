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


def my_div(arg1, arg2):
    try:
        return print(arg1 / arg2)
    except ZeroDivisionError:
        return "Вы что? Пытаетесь делить на 0!"


try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print(my_div(num1, num2))

except ValueError:
    print("Вводите только числа!")
