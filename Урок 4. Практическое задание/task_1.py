"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

script, first_param, second_param, third_param = argv
""" 
first_param = выработка в часах
second_param = ставка в час
third_param = премия 
"""


def my_func(var_time, var_cost, var_add):
    return float(var_time) * float(var_cost) + float(var_add)


print(my_func(first_param, second_param, third_param))
