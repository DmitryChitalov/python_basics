"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, w_hours, wh_rate, bonus = argv

def salary_calc(w_hours, wh_rate, bonus):
    salary = (int(w_hours) * int(wh_rate)) + int(bonus)
    return salary

print(salary_calc(w_hours, wh_rate, bonus))
