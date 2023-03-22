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


def func_division():
    try:
        first_value = int(input("Введите первое число для деления: "))
        second_value = int(input("Введите второе число для деления: "))
        result = first_value / second_value
        print(result)
    except ZeroDivisionError:
        print("Нельзя делить на 0!")
    except ValueError:
        print("Вам нужно вводить числа!")


func_division()
