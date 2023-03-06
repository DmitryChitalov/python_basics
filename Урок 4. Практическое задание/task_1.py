"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv


def get_arg(args, index):
    try:
        return int(args[index])
    except:
        return 0


salary, time, bonus = get_arg(argv, 1), get_arg(argv, 2), get_arg(argv, 3)

print(f'Salary = {time * salary + bonus}')
