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
def quot_int():

    try:
        my_bool_true = True
        Message = 'Введите второе число: '
        val_1 = float(input('Введите первое число: '))
        while my_bool_true:
            val_2 = float(input(Message))
            if val_2 == 0:
                Message = 'второе число должно быть больше нуля'
                my_bool_true = True
            else:
                my_bool_true = False
                return val_1 / val_2

    except ValueError:
        return 0

print(quot_int())