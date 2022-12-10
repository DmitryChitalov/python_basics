"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv


def my_salary(*args):
    salary = (hours * rate) + bonus
    return salary


if len(argv) > 1:
    script_name, hours, rate, bonus = argv
    hours = int(hours)
    rate = int(rate)
    bonus = int(bonus)
    print(my_salary(argv))
else:
    hours = int(input("Input amount of work hours: "))
    rate = int(input("Input rate: "))
    bonus = int(input("Input bonus: "))
    print(my_salary(hours, rate, bonus))
