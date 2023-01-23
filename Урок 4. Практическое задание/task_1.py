"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

import sys


f_obj, global_name, global_rate, global_hours = sys.argv


def less1(rate, hours):
    try:
        print(f"Сотрудник {global_name} получил {int(rate) * int(hours) * 1.25}")
    except TypeError:
        print("Неправильный тип объекта")
        exit()


if __name__ == '__main__':
    less1(global_rate, global_hours)

