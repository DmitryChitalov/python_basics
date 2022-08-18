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


######
# from sys import argv
# print(argv)
# def my_func(arg1, arg2):
#    return arg1 + arg2
# a = my_func(80, 30)
# print(a)

def my_func1(a1, a2):
    try:
        return a1/a2
    except  ZeroDivisionError:
        return "Попытка деления на 0 !"
try:
    a1 = int(input("Введите первое число: "))
    a2 = int(input("Введите второе число: "))
    print(my_func1(a1, a2))
except ValueError:
    print("Ошибка! Нужно вводить только числа")
