"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

name, employee, hours, rate, premium = argv


def salary(hours_f, rate_f, premium_f):
    print(f'{employee} заработал {int(hours_f) * int(rate_f) + int(premium_f)} рублей')


salary(hours, rate, premium)
