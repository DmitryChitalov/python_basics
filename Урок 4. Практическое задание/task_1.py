"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

script, work_hours, pay_per_hour, bonus = argv


def calc_salary(work_hours, pay_per_hour, bonus):
    result = (int(work_hours) * int(pay_per_hour)) + int(bonus)
    return result


print(f"Результат: {calc_salary(work_hours, pay_per_hour, bonus)}")
