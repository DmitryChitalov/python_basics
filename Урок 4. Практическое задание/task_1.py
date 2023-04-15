"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
спользуйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def payroll_calculation(var1, var2, var3):
    """Функция вычисляет размер зарплаты по формуле: (выработка в часах*ставка в час) + премия."""
    return (int(var1) * int(var2)) + int(var3)


script, output_in_hours, rate_per_hour, prize = argv
print(f"{payroll_calculation(output_in_hours, rate_per_hour, prize)}")
