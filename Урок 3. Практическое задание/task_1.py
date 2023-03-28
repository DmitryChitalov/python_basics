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


def my_div(var_divd, var_divr):
    try:
        var_res = var_divd / var_divr
        return var_res
    except ZeroDivisionError:  # проверка на возникновение ошибки деления на нуль
        return "Ошибка деления на нуль"


error_check = True
var_dividend = None
var_divider = None
try:
    var_dividend = int(input("Введите первое число:"))  # переменная делимое
    var_divider = int(input("Введите второе число:"))  # переменная делитель
except ValueError:  # проверка на возникновение ошибки типов данных (введено значение отличное от целого числа)
    print("Ошибка типов введенных значений. Необходимо ввести целое число.")
    error_check = False
if error_check:
    print("Результат деления первого числа на второе: ", my_div(var_dividend, var_divider))
