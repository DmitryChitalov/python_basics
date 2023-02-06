"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv
if len(argv) > 1:
    name_script, time_work, rate, prize = argv
    time_work = int(time_work)
    rate = int(rate)
    prize = int(prize)
    print((time_work * rate) + prize)
else:
    time_work = int(input("Выработка в часах: "))
    rate = int(input("Ставка: "))
    prize = int(input("Премия: "))
    print((time_work * rate) + prize)
    
