"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv
script_name, production_inhour, bet_inhour, prize = argv
salary = int(production_inhour) * int(bet_inhour) + int(prize)
print(f"Выработка в часах: {production_inhour}")
print(f"Ставка в часах: {bet_inhour}")
print(f"Премия: {prize}")
print(f"Заработная плата сотрудника: {salary}")