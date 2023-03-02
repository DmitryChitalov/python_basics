"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv


def pay(*args):
    rate = int(op_hours) * int(hour_costs)
    bonus = rate * 0.1
    return rate + bonus


script_name, op_hours, hour_costs = argv
print(pay(op_hours, hour_costs))
