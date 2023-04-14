"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, first_param, second_param, third_param = argv


def salary(work_hours, cost_hour, bonus):
    result = float(work_hours) * float(cost_hour) + float(bonus)
    return result


print(f"Заработная плата сотрудника = {salary(first_param, second_param, third_param)}")
