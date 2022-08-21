"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

"""from sys import argv
script_name, salary, bet, prize = argv

def func_pay(a, b, c):
    return int(a) * int(b) + int(c)

print(func_pay(salary, bet, prize))

Спрва сделал выше, потом ниже, удалять не стал))"""

from sys import argv
script_name, salary, bet, prize = argv

def func_pay(var):
    return int(var[1]) * int(var[2]) + int(var[3])

print(func_pay(argv))



