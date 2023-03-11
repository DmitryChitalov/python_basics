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
def my_division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
        return

a = int(input("Введите первое число (a): "))
b = int(input("Введите второе число (b): "))
res = my_division(a, b)
if res is not None:
    print(f"Результат деления a/b: {res}")
