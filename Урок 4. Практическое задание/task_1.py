"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
import sys
from sys import argv

try:
    pay, work, rate, premium = argv
    pay_result = int(work) * int(rate) + int(premium)
    print(pay_result)
except Exception as e:
    print(e)
