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

def calc (figure_1, figure_2):
    try:
        return figure_1 / figure_2
    except ZeroDivisionError:
        return "Делить на 0 нельзя!!!"
try:
    number_1 = int(input("Введите число: "))
    number_2 = int(input("Введите еще число: "))
    print(calc(number_1,number_2))
except ValueError:
    print("Вводите правильные числа")
