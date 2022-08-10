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
def func(num_1, num_2):
    try:
        res = num_1 / num_2
        print(res)
    except ZeroDivisionError:
        print('Деление на 0!')


first_num = float(input('введите первое число '))
sec_num = float(input('введите второе число '))
func(first_num, sec_num)
