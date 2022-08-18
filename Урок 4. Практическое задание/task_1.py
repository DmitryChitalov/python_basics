"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

"""
В скрипт передаются аргументы: 
1: выработка в часах;
2: ставка в час, руб.;
3: размер премии, руб.
"""

from sys import argv

result_hours = int(argv[1])
hourly_payment = int(argv[2])
bonus = int(argv[3])

print(f"Выработка сотрудника: {result_hours} часов. Ставка в час: {hourly_payment} руб. Премия: {bonus} руб.")
print(f"Заработная плата сотрудника: {result_hours * hourly_payment + bonus} руб.")
