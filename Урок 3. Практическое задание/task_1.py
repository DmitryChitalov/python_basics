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
def div_func(arg_int, arg_int2):
    return arg_int / arg_int2
while True:
    user_input = input('Введите первое число, для выхода введите q: ')
    user_input_2 = input('Введите второе число, для выхода введите q: ')
    if (user_input or user_input_2) == 'q':
        break
    try:
        div_result = div_func(int(user_input), int(user_input_2))
    except ZeroDivisionError:
        print(f'На ноль делить нельзя!')
    except ValueError:
        print(f'Недопустимое значение. Введите число!')
    else:
        print(f'Результат деления этих чисел = {div_result}')
        
