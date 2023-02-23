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
numb_1 = float(input('enter any number: '))
numb_2 = float(input('enter any number: '))
def _my_division_(arg_1, arg_2):
    try:
        result = round(arg_1 / arg_2, 3)
    except ZeroDivisionError:
        print('делить на ноль нельзя')
        exit()
    return result
print(
    f'Результат деления {numb_1} на {numb_2} с точностью до трех знаков '
    f'равен: {_my_division_(numb_1, numb_2)}')
