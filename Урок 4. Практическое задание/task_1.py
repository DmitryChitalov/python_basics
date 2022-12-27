"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, hours_worked, rate_per_hour, prize = argv

print("Имя скрипта: ", script_name)
print("\n'Программа рассчета заработной платы сотрудника'")
print("Выработка в часах: ", hours_worked)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", prize)
print("Зарплата сотрудника: ", (float(hours_worked) * float(rate_per_hour)) + float(prize))

# PS C:\Users\son2001\PycharmProjects\pythonProject> python 1.py 8 2 200
