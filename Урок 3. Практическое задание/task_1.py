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
def division(n1: int, n2: int):
    try:
        result = n1 / n2
        return result
    except ZeroDivisionError:
        print("Вы передали 0 в качестве 2 аргумента!")
        n3 = int(input("Введите второй аргумент:"))
        result_new = division(n1, n3)
        return result_new

num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")

print("Результат деления:", division(4, 3))