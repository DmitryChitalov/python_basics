"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
#Выполнение первого задания
from sys import argv


def pay():
    try:
        name, hours, pays, bonus = argv
        res = (float(hours) * int(pays)) + int(bonus)
        return print(f'Выработка в часах {hours} * ставка в час {pays} + {bonus} = заработная плата сотрудника {res} ')
    except ValueError:
        return print('Некорректное значение')


pay()