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
        print (f'Сотрудник {fio_sotr} заработал {(int(vir_h) * int(stav_h)) + int(prem)}')
    except TypeError:
        print ("Операция применена к объекту несоответствующего типа")
        exit()

calculate_salary (vir_h, stav_h, prem)
