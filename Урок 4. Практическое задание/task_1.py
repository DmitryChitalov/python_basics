"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_param_name, output_in_hours_param, ratу_per_hours_param, prize_param = argv
print("Имя скрипта: ", script_param_name)
print("Выработка в часах: ", output_in_hours_param)
print("Ставка в час: ", ratу_per_hours_param)
print("Премия: ", prize_param)


def s_pay(a, b, c):
    return a * b + c


print(f"Заработная плата {s_pay(int(output_in_hours_param), int(ratу_per_hours_param), int(prize_param))}")
