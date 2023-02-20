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
def division(*args):
    try:
        args1 = int(input("Input args1: "))
        args2 = int(input("Input args2: "))
        res = args1 / args2
    except BaseException:
        return ("ERROR. EXIT.")
        exit(-1)

        return int(res)

print(division())
