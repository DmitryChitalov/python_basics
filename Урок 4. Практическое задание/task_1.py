"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
#!/usr/bin/env python3

'''
The essential difference between a salary and wages is that a salaried person is paid a fixed amount per pay period and a wage earner is paid by the hour. 
'''
from sys import argv

working_hours = int(argv[1])
hourly_wages = int(argv[2])

print(f"Вы предлагаете рассчитать з/п со следующими входными данными: {working_hours} и {hourly_wages}")
    
def wages_calculation(working_hours, hourly_wages):
    return working_hours * hourly_wages

print(f"Заработная плата сотрудника:", wages_calculation(working_hours, hourly_wages))
