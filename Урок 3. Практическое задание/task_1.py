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


def division_numbers(x1, x2):
    try:
        result = x1 / x2
    except ZeroDivisionError:
        print("Вы что? Пытаетесь делить на 0!")
        return
    return result


while True:
    var_a = input("Введите первое число: ")
    try:
        var_a = int(var_a)
        break
    except ValueError:
        print("Введите целое число")
        continue

while True:
    var_b = input("Введите второе число: ")
    try:
        var_b = int(var_b)
        break
    except ValueError:
        print("Введите целое число")
        continue

print(f"Результат: {division_numbers(var_a, var_b)}")
