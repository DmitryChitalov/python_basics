"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

name_employee, hours, cost_for_hour, bonus = argv


def employee_salary(hours, cost_for_hour, bonus):
    salary = float(hours) * float(cost_for_hour) + float(bonus)
    return salary


print(f"Зарплата сотрудника: {employee_salary(hours, cost_for_hour, bonus)}")
