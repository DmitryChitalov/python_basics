"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, production_hour, bid_hour, award = argv

print("Выработка в часах: ", production_hour)
print("Ставка в час: ", bid_hour)
print("Премия: ", award)

production_hour = int(production_hour)
bid_hour = int(bid_hour)
award = int(award)

result = (production_hour * bid_hour) + award
print("Заработная плата сотрудника равна: ", result)
