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


def s_calc():
    try:
        r_val = float(input("Введите число: "))
        h_val = float(input("Введите число: "))
        if h_val == 0:
            print(f"Вы что? Пытаетесь делить на 0!")
            return
        elif r_val == 0:
            print(f"Вы что? Пытаетесь делить на 0!")
            return

    except ValueError:
        return
    s_side = r_val / h_val
    return s_side


s_side_val = s_calc()
print(f"Ответ - {s_side_val}")
