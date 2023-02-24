"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

def salary(production, rate, premium):
    return production * rate + premium


print(salary(production=float(argv[1]), rate=int(argv[2]), premium=int(argv[3])))