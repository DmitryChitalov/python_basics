"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, rate, sallary_hours_emp = argv

# sallary_hours_emp - выработка в часах
# rate - ставка в час
# bonus - премия

bonus_rate = 1.5

def salary(sallary_hours_emp, rate):
    try:
        salary_emp = int(sallary_hours_emp) * int(rate)
        total_bonus = bonus_rate * salary_emp
        print(f'Сотрудник заработал {salary_emp + total_bonus}')
        print("Расшифровка")
        print(f"Зарплата: {salary_emp}")
        print(f"Премия: {total_bonus}")
    except ValueError:
        print('Нужно передать цифры!')


salary(sallary_hours_emp, rate)



