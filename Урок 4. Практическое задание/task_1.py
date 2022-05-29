"""

1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

name, first, second, third = argv
#print(argv, type(argv))
def my_func(*args):
    first, second, third = args
    #print(args)
    res = int(first) * int(second) + int(third)
    return res

print(my_func(first, second, third))

