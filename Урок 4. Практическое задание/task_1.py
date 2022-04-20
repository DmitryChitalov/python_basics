"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

import sys

script_name, numb_hours, sal_per_hour, prem = sys.argv


def sal_staff(numb_hours, sal_per_hour, prem):
    sal = int(numb_hours) * int(sal_per_hour) + int(prem)
    return sal


print(sal_staff(numb_hours, sal_per_hour, prem))
