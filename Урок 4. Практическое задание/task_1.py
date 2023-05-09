"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, production, rate_in_hours, bonus = argv


def salary(a, b, c):
    try:
        print('Выработка в часах: ', a)
        print('Ставка в час: ', b)
        print("Премия: ", c)
        print((float(a)*float(b))+float(c))
    except TypeError:
        print('Ошибка ввода параметров')


salary(production, rate_in_hours, bonus)
