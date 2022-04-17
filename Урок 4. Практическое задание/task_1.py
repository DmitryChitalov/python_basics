"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, hours, perhour, prize = argv


def salary(hours, perhour, prize):
    try:
        print(f'{(int(hours) * int(perhour)) + int(prize)}')
    except ValueError:
        print("Некорректные данные")

salary(hours, perhour, prize)
