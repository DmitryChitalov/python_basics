"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

import sys

f_obj, fio_sotr, vir_h, stav_h, prem = sys.argv

def calculate_salary (vir_h, stav_h, prem):
    try:
        print(f'Зарплата сотрудника {fio_sotr} составила {(int(vir_h) * int(stav_h)) + int(prem)}')
    except TypeError:
        print("Операция не применима к объекту данного типа")
        exit()

calculate_salary (vir_h, stav_h, prem)
