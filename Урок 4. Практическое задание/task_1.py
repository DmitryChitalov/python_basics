"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

obj, name, time, stavka, bonus = argv


def zp(name_1, time_1, stavka_1, bonus_1):
    total = 0
    total = int(time_1) * int(stavka_1) + int(bonus_1)
    print(f"{name} заработная плата  - {total}")


zp(name, time, stavka, bonus)
