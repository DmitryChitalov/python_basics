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


def division(divisible, divisor):
    try:
        return divisible / divisor
    except:
        print("Вы что? Пытаетесь делить на 0!")


divisible = int(input("Введите делимое: "))
divisor = int(input("Введите делитель: "))
print(f"Частное = ", division(divisible, divisor))