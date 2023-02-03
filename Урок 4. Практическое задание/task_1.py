"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv
prog, employee, hours, rate, bonus = argv

def salary_sum(hours, rate, bonus):
    try:
        res = (int(hours) * int(rate)) + int(bonus)
        return res
    except TypeError:
        print("Не правильно введены данные")

print(f"Зарплата сотрудника {employee} составила {salary_sum(hours, rate, bonus)} руб.")
