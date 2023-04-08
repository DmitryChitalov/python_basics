"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
import sys


def salary(hours, price, bonus):
    return hours * price + bonus


h, p, b = (0, 0, 0)

try:
    h = int(sys.argv[1])
except ValueError:
    print("Hours should be integer")
try:
    p = int(sys.argv[2])
except ValueError:
    print("Price should be integer")
try:
    b = int(sys.argv[3])
except ValueError:
    print("Bonus should be integer")

print(salary(h, p, b))
