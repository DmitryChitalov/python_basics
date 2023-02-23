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

def divide_numbers(first_object, second_object):
    try:
        return first_object/second_object
    except ZeroDivisionError:
        return "Деление на ноль невозможно"

try:
    first_numb = int(input("Введите первое число: "))
    second_numb = int(input("ведите второе число: "))
    print(divide_numbers(first_numb, second_numb))
except ValueError:
    print("Вы ввели некорректное значение. Пожалуйста, введите число")
