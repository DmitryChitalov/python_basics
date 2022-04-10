"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv


def my_salary():
    try:
        my_name_script, my_name, my_hour, my_money, my_bonus = argv
        return print(f'Заработная плата {my_name} составила {float(my_hour) * int(my_money) + int(my_bonus)}')
    except ValueError:
        print(f'Ошибка ввода данных')


my_salary()
