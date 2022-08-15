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
    if a2 != 0:
        return round(a1 / a2, 1)
    else:
        print(f"Деление на 0, так нельзя")
        return None

a1 = int(input("Введите первое число: "))
a2 = int(input("Введите второе число: "))
print(type(my_func1(a1,a2)))
if type(my_func1(a1, a2)) != "None":
    print(my_func1(a1, a2))
