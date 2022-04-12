"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv
import string_extension

script_name, work_hour, val_per_hour, bonus = argv
if string_extension.is_int(work_hour) and string_extension.is_int(val_per_hour) and string_extension.is_int(bonus):
    print(f"{int(work_hour) *  int(val_per_hour) + int(bonus)}")
else:
    print("Error: params is not an integer values")