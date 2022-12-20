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
#

def my_func(user_inp_num, user_inp_den):
    try:
        return round((int(user_inp_num)/int(user_inp_den)), 2)
    except ZeroDivisionError:
        print('Вы что? Пытаетесь делить на 0!')
    except ValueError:
        print('Нужно ввести цифры!')


numerator = input('Введите первое число: ')
denumerator = input('Введите второе число: ')

result = my_func(numerator, denumerator)

print(result)

