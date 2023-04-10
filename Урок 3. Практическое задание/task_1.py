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

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    div_result = a / b
except ValueError:
    print("Необходимо вводить только числа")
except ZeroDivisionError:
    print('На ноль делить нельзя!')
else:
    def division_func(arg_1, arg_2):
        return arg_1 / arg_2

    print(f"Результат деления первого числа на второе: {division_func(a, b)}")
