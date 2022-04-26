"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

f_name, w_time, salary, add_bonus = argv
try:
    w_time = int(w_time)
    salary = int(salary)
    add_bonus = int(add_bonus)
    res = w_time * salary + add_bonus
    print(f'заработная плата сотрудника --> //{res}//')
except ValueError:
    print('Not a number')

"""-------------"""

def sal():
    try:
        w_time = float(input('Выработка в часах '))
        salary = int(input('Ставка в у.е. '))
        add_bonus = int(input('Премия в у.е. '))
        res = w_time * salary + add_bonus
        print(f'заработная плата сотрудника  --> //{res}//')
    except ValueError:
        return print('Not a number')
sal()

