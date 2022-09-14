"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, worker_name, worker_rate, work_hours = argv
def calculate_salary(worker_rate, work_hours):
    try:
        print(f'Сотрудник {worker_name} заработал '
              f'{int(work_hours) * int(worker_rate) + 500}')
    except:
        print("Ошибка")

calculate_salary(worker_rate, work_hours)
