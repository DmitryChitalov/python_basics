"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""


from sys import argv

salary_calc, hours, pay_per_hour, bonus = argv

def calc(hours_, pay_per_hour_, bonus_):
    try:
        result = (int(hours_) * float(pay_per_hour_)) + float(bonus_)
    except ValueError:
        return
    return result


print(f"{calc(hours, pay_per_hour, bonus)}")
