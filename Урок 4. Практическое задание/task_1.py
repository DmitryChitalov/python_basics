"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv


# расчёт зарплаты
def pay_for_work(work_time, cost_hour, prize):
    res = float(work_time) * float(cost_hour) + float(prize)
    return res


# получаем параметры
script_name, first_param, second_param, third_param = argv

print(f"Заработная плата сотрудника = {pay_for_work(first_param, second_param, third_param)}")
