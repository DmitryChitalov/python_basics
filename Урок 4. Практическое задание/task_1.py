"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

def calc_salary(hours, rate, bonuses):
    '''Расчет зп сотрудника'''
    return float(hours) * float(rate) + float(bonuses)

script_name, hours_val, rate_val, bonuses_val = argv
print(f'Зароботная плата сотрудника: {calc_salary(hours_val, rate_val, bonuses_val)}')
