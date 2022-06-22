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


def numbers_division(number_from, number_to):
    """
    :param number_from: первый аргумент функции - что делим
    :param number_to: второй аргумент функции - на что делим
    :return: <number_from> / <number_to>
    """"""
    Возращает результат деления первого целочисленного аргумента на второй
    Если второй аргумент = 0, выводится соответствующее предупреждение
    my_result = numbers_division (10, 5) -> 2
    """
    try:
        return round((number_from / number_to), 1)
    except ZeroDivisionError:
        return "Вы что? Пытаетесь делить на 0!"


try:
    number_1 = int(input("Введите первое число: "))
    number_2 = int(input("Введите второе число: "))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")

print(numbers_division(number_1, number_2))
