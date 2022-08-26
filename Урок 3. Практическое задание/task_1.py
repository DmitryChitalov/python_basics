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


def divider(a, b):
    is_complete = False
    result_div = 0
    while not is_complete:
        try:
            result_div = a / b
            is_complete = True
        except ZeroDivisionError:
            print("Вы что? Пытаетесь делить на 0! НИЗЗЯ)) ")
            b = int(input("Укажите делитель еще раз: "))
    return result_div


x = int(input("Введите делимое число: "))
y = int(input("Введите делитель числа: "))
result = divider(x, y)
print(f"Ответ: ", result)
