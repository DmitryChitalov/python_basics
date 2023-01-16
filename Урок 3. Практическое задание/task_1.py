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


def divide(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        return False


def less1():
    num_1, num_2 = map(int, input("Введите два числа через пробел: ").split())
    res = divide(num_1, num_2)
    if not res:
        print("Error! Зафиксирована попытка деления на 0!")
    else:
        print(f"Результат деления {num_1} на {num_2}:   {res:0.3f}")


if __name__ == '__main__':
    less1()

