"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

import sys


def employee(hours, cost_per_hour, prem):
    return round(float(hours) * float(cost_per_hour) + float(prem), 2)


try:
    _, hours, cost_per_hour, prem = sys.argv
except ValueError:
    print("Параметры скрипта введены не верно")
    exit()
wage = employee(hours, cost_per_hour, prem)

print(f"Заработная плата сотрудника = {wage}")
