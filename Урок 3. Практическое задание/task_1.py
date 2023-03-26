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


def division(first_digit, second_digit):
    try:
        print(int(first_digit) / int(second_digit))
    except ZeroDivisionError:
        print("Вы что? Пытаетесь делить на 0!")
    except TypeError:
        print("Невреный формат данных!")
    except ValueError:
        print("Неверный формат данных!")


division(first_digit=input("Введите первое число: "), second_digit=input("Введите второе число: "))
