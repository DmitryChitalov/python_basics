"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0"""
def div(*args):

    try:
        arg1 = 10
        arg2 = 0
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"

    return res
print(f'result  {div()}')
"""
Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""
def div(*args):
    try:
        arg1 = 10
        arg2 = 10
        res = arg1 / arg2
    print(f"Результат деления 10 на 10: {int(res)}")
