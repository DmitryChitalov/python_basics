"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

f_obj, name_v, rate_v, hours_v = argv
print(f_obj)


def calc_salary(rate, hours):
    try:
        print(f'Сотрудник {name_v} заработал {int(rate) * int(hours) * 1.25}')
    except TypeError:
        print('Ошибка типа')
        exit()


calc_salary(rate_v, hours_v)
