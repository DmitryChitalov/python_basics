"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

if len(argv) > 1:
    name_script, times, rate, premiums = argv
    times = int(times)
    rate = float(rate)
    premiums = float(premiums)
    print((times * rate) + premiums)
else:
    times = int(input("Отработанные часы: "))
    rate = float(input("Ставка в час: "))
    premiums = float(input("Премия: "))
    summ = ((times * rate) + premiums)
    print(f'Размер заработной платы составил: {summ}')

