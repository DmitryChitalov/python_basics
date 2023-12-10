"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv
(script_name, work_hours, hourly_rate, perm) = argv
def staf_pay():
    print("Выработка в часах: ", work_hours)
    print("Ставка в час: ", hourly_rate)
    print("Премия: ", perm)
    return int(work_hours) * int(hourly_rate) + int(work_hours) * int(hourly_rate) / 100 * int(perm)
print(staf_pay())


