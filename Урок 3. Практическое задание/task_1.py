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


def division_numb(argument_1, argument_2):
    """Функция деления"""
    return argument_1 / argument_2


def get_numb(order_numb):
    """Функция ввода"""
    while True:
        input_numb = input(f'Введите {order_numb} число: ')
        if input_numb == '':
            break
        try:
            input_numb = float(input_numb)
        except ValueError:
            print('Ошибка преобразования введенного значения в число!')
        else:
            break
    return input_numb


while True:
    first_numb = get_numb(1)
    if first_numb == '':
        break

    second_numb = get_numb(2)
    if second_numb == '':
        break
    try:
        division_res = division_numb(first_numb, second_numb)
    except ZeroDivisionError:
        print('Ошибка деления на ноль!')
        continue
    else:
        print(f'Результат операции {first_numb} / {second_numb} = {division_res: .2f}')
print('Операция отменена!')
