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

def my_div(first_obj, second_obj):
    try:
        return first_obj/second_obj
    except ZeroDivisionError:
        return f'Деление на {second_obj} запрещено !'


first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
print(my_div(first_num, second_num))



