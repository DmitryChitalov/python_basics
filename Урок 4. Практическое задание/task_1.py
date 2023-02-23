"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, hours, cost_per_hour, bonus = argv

def payroll(hours, cost_per_hour, bonus):
    """
    Функция подсчёта ЗП
    :param hours: количество отработаных часов
    :param cost_per_hour: стоимость часа работы
    :param bonus: премия
    :return:
    """
    print(int(hours) * int(cost_per_hour) + int(bonus))

payroll(hours, cost_per_hour, bonus)
