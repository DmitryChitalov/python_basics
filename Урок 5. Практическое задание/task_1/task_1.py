"""
Задание 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def bub_values():
    try:
        number_one = int(input('Введите первое число: '))
        number_two = int(input('Введите второе число: '))
        return number_one, number_two
    except ValueError:
        print("Ошибка ввода чисел. Попробуйте снова ! ")
        return bub_values()


def func_operation():
    addition = '+'
    subtraction = '-'
    multiplication = '*'
    division = '/'
    stop_pogramm = '0'

    input_operation = input(
        'Введите операцию (+, -, *, /) или введите 0 для завершения : ')

    if input_operation.find(stop_pogramm) != -1:
        return print('Программа завершена, оплата на кассе !')
    elif input_operation.find(addition) != -1:
        number_one, number_two = bub_values()
        print(f'Результат сложения = {number_one + number_two}')
        return func_operation()
    elif input_operation.find(subtraction) != -1:
        number_one, number_two = bub_values()
        print(f'Результат вычитания = {number_one - number_two}')
        return func_operation()
    elif input_operation.find(multiplication) != -1:
        number_one, number_two = bub_values()
        print(f'Результат умножения = {number_one * number_two}')
        return func_operation()
    elif input_operation.find(division) != -1:
        number_one, number_two = bub_values()
        try:
            print(f'Результат деления = {number_one / number_two}')
            return func_operation()
        except ZeroDivisionError:
            print(f'Деление на 0, странная затея')
            return func_operation()
    else:
        print('Ошибка, выбирите операцию')
        return func_operation()


operation = func_operation()
