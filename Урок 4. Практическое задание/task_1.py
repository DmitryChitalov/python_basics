"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
import sys

employee_obj, name_employee, rate_employee, hours_employee = sys.argv
print(employee_obj)

def calculate_salary(rate, hours):
    try:
        print(f'Сотрудник {name_employee} заработал {int(rate) * int(hours) * 1.5}')
    except TypeError:
        print("Объект не соотвествует данному типу")
        exit()
calculate_salary(rate_employee, hours_employee)
