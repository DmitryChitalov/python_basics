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
def calculate(x, y):
    try:
        solution = x / y
        print(f"Formula: ({x}/{y}) = {solution}")

    except ZeroDivisionError:
        y = int(input("Вы что пытаетесь делить на 0? Пожалуйста введите другое значение: "))
        calculate(x, y)

try:
    user_input = (input("Введите два числа через пробел: ")).split()

    while len(user_input) != 2:
        print("Введите только два числа! ")
        user_input = (input("Введите два числа через пробел: ")).split()

    x = int(user_input[0])
    y = int(user_input[1])

    calculate(x, y)

except ValueError:
    print(user_input," is not valid input.")