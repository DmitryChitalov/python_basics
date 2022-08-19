"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, h_working = argv
# На ввод принимаю один параметр, остальные будут фиксированные
val = int(h_working)


def salary(work):
    rate = 500
    bonus = 250
    try:
        res = work * rate + bonus
        return res
    except ValueError:
        print("Введите число")


salary(val)
print(f"Зарплата сотрудника: {salary(val)}")
