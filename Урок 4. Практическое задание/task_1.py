"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv


def income_calc(arg_work_hours=0, arg_hour_payment=0, arg_bonus=0):
    return print(f"Заработано: {(arg_work_hours * arg_hour_payment) + arg_bonus}")


#    return kwargs.get('bonus')


script_name, work_hours, hour_payment, bonus = argv

print("Имя скрипта: ", script_name)
print("Часов отработано: ", work_hours)
print("Ставка (час): ", hour_payment)
print("Премия: ", bonus)

income_calc(arg_bonus=float(bonus), arg_work_hours=float(work_hours), arg_hour_payment=float(hour_payment))
"""
python.exe "D:/GeekBrains/python/python_basics/Урок 4. Практическое задание/task_1.py" 8.5 10 100 
Имя скрипта:  D:/GeekBrains/python/python_basics/Урок 4. Практическое задание/task_1.py
Часов отработано:  8.5
Ставка (час):  10
Премия:  100
Заработано: 185.0
"""
