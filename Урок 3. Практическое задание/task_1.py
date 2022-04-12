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

def division(int_1, int_2):
    try:
        return int_1 / int_2
    except:
        print("Error, division by zero")

int_1 = int(input("Enter first integer: "))
int_2 = int(input("Enter second integer: "))
res = division(int_1, int_2)

print(f"Result (int_1 / int_2): {res}")
