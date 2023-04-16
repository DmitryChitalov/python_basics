"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, hour, rate_per_hour, awards = argv
def wage(hours, rate_p_hour, award):
    print(f'Заработная плата равна: {float(hours) * float(rate_p_hour) + float(award)}')

wage(hour, rate_per_hour, awards)