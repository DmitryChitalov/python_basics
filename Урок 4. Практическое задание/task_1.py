"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv


def payroll_calculation(production, rate_per_hour, bonus):
    return production * rate_per_hour + bonus


if len(argv) == 4:
    try:
        print(f'{payroll_calculation(float(argv[1]), float(argv[2]), float(argv[3])):.2f}')
    except ValueError:
        print("Ошибка: не верно указаны значения параметров")
else:
    print("Ошибка: не верное количество параметров.")
