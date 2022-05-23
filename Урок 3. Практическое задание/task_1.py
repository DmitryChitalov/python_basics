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


def divide_two_numbers(first_number, second_number):
    try:
        print(f'Результат: {round(first_number / second_number, 3)}')
    except ZeroDivisionError:
        print("Вы что? Пытаетесь делить на 0!")
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")


first_numb = int(input("Введите первое число: "))
second_numb = int(input("Введите второе число: "))
divide_two_numbers(first_numb, second_numb)
