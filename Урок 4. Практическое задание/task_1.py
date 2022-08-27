"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""


from sys import argv


def payroll(prod_in_hours, rate_per_h, prem):
    return prod_in_hours * rate_per_h + prem


script_name, production_in_hours, rate_per_hour, premium = argv

print(f'Заработная плата = {production_in_hours} * {rate_per_hour} + {premium} = '
      f'{payroll(int(production_in_hours), int(rate_per_hour), int(premium))}')
