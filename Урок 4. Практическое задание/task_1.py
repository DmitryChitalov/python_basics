"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv
script_name, job_hour, hours_rate, bonus = argv

print("Скрипт: ", script_name)
print("Рабочего времени в часах: ", job_hour)
print("Cтавка за час: ", hours_rate)
print("Премия : ", bonus)

calculation = (int(job_hour) * int(hours_rate) + int(bonus))
print(f"Your salary is {calculation}")
