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


def div_two(divisible, divisor):
    """ Возвращает частное от деления двух чисел """
    if divisor == 0:
        print("Division by zero!")
        return None
    return divisible / divisor


first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))

quotient = div_two(first_num, second_num)
if quotient is not None:
    print(div_two(first_num, second_num))
