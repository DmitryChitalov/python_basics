"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
python task_1.py "Федя" 16 1000 2000
"""

import sys

def calc_salary(work_hours, salary_per_hour, bonus):
    return work_hours * salary_per_hour + bonus

f_name, name_v, work_hours_v, salary_per_hour_v, bonus_v = sys.argv

salary = calc_salary(int(work_hours_v), int(salary_per_hour_v), int(bonus_v))
print(f'Сотрудник {name_v} заработал {salary} рублей')