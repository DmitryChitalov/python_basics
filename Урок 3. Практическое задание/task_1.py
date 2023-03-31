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
    try:
        return a / b
    except ZeroDivisionError:
        return "Делить на 0 нельзя"

    try:
        a_numb = int(input("Первое число"))
        b_numb = int(input("Второе число"))
        print(division(a_numb, b_numb))
    except ValueError:
        print("нужны числа!")

