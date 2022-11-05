"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, production_h, bet_h, prize = argv


def salary_func(production, bet, bonus):
    try:
        print(f"Заработная плата сотрудника: {float(production_h) * float(bet_h) + float(prize)}")
    except ValueError:
        print("Убедитесь, что в параметрах переданы числа!")
        exit()


salary_func(production_h, bet_h, prize)
