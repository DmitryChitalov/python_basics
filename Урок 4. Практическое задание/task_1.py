"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, production_v, rate_v, award_v = argv


def salary(production, rate, award):
    print(f"Заработная плата составляет: {int(production) * int(rate) * int(award)}")


salary(production_v, rate_v, award_v)
