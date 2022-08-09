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

dividend = int(input("Please enter the number to be divided:"))
divisor = int(input("Please enter the number to be the divisor:"))

def divide_numbers (a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("You can't divide by zero")
        exit(0) 

print(divide_numbers(dividend,divisor))