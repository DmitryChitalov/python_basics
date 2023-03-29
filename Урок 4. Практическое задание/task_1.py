"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

# параметры скрипта: имя скрипта, выработка в часах, почасовая ставка, премия
script_name, production_hrs, rate_per_hour, premium = argv


def func_salary(prod, rate, prem):
    return prod * rate + prem


print("Заработная плата: ", func_salary(int(production_hrs), int(rate_per_hour), int(premium)))
