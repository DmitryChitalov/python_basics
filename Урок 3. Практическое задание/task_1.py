a = float(input("Введите делимое"))
b = float(input("Введите делитель"))

if a == 0:
    print("Вы что? Пытаетесь делить на 0!")
elif b == 0:
    print("Вы что? Пытаетесь делить на 0!")
else:
    def Division(a, b):
        return a // b


    d = Division(a, b)
    """Делит a на b, выводит значение d"""

    print(d)

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
