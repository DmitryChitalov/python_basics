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


def divide(num, denum):
    """
    Результат деления первого числа на второе
    :param num: Первое число, т.е числитель
    :param denum: Второе число, т.е знаменатель
    :return: Возвращает результат деления первого числа на второе
    """
    return num / denum


while True:
    try:
        numerator = int(input('Введите первое число: '))
        denominator = int(input('Введите второе число: '))
        if denominator == 0:
            raise ZeroDivisionError
    except ValueError:
        print('Ошибка ввода данных. Попробуйте еще раз.\n')
    except ZeroDivisionError:
        print('Делить на 0 запрещено! Попробуйте еще раз.\n')
    else:
        print(divide(numerator, denominator))
        break
