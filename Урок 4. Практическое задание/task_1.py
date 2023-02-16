"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

# pylint: disable=unbalanced-tuple-unpacking

import sys

file, p, r, b = sys.argv

try:
    productivity: int = int(p)
    rate: int = int(r)
    bonus: int = int(b)
    result: int = productivity * rate + bonus
    print(f"Заработная плата сотрудника  {result}")
except ValueError:
    exit('Параметр должен быть числом')
