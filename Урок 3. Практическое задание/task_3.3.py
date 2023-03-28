"""Реализовать функцию my_func(),
которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов."""

def my_func(*args):
    arg_1 = float(input("Введите первое число: "))
    arg_2 = float(input("Введите второе число: "))
    arg_3 = float(input("Введите третье число: "))

    if (arg_1 > arg_2 or arg_2 > arg_1) and arg_1 > arg_3 and arg_2 > arg_3:
        return arg_1 + arg_2

    elif arg_1 > arg_2 and (arg_1 > arg_3 or arg_3 > arg_1) and arg_3 > arg_2:
        return arg_1 + arg_3

    elif arg_2 > arg_1 and (arg_2 > arg_3 or arg_3 > arg_2) and arg_3 > arg_1:
        return arg_2 + arg_3

print(my_func())
