"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, first_param, second_param, third_param = argv

print("Имя скрипта: ", script_name)
print("Кол-во часов: ", first_param)
print("Ставка в час: ", second_param)
print("Премия: ", third_param)
salary = int(first_param) * int(second_param) + int(third_param)
print(f"Зарплата составляет: {salary}")
