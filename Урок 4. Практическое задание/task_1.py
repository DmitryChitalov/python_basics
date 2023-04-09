"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv


def wg(prod, rph, bon):
    return round(float(prod) * float(rph) + float(bon), 2)


try:
    file, salary, rate_per_hour, bonus = argv
except ValueError:
    print("Неверно введены параметры скрипта")
    exit()
wage = wg(salary, rate_per_hour, bonus)

print(f"Заработная плата = {wage}")
