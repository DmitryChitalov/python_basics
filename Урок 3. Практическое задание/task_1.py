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

def devison(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Вы что? Пытаетесь делить на 0!"
    return result

try:
    first_num = int(input("Введите первое число: "))
    second_num = int(input("Введите второе число: "))
    print(devison(first_num, second_num))
except ValueError:
    print("it's not an int")

