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


# Функция деления двух чисел с проверкой деления на ноль.
def divided_func(first_num, sec_num):
    try:
        equl_div = first_num // sec_num
    except ZeroDivisionError:
        return print("Делить на ноль нельзя!")
    return equl_div


while True:
    first_var = int(input("Введите делимое: "))
    sec_var = int(input("Введите делитель: "))
    print("Частное от деления:", divided_func(first_var, sec_var))
    q = input("Выход - 1 ")
    if q == '1':
        print("bye bye!")
        break
