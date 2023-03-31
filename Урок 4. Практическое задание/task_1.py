"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

def res(prod, wagerate, bon):
    return round(float(prod) * float(wagerate) + float(bon), 2)


try:
    file, salary, wagerate_per_hour, bonus = argv
except ValueError:
    print("Ошибка в данных!")
    exit()
resoult_wage = res(salary, wagerate_per_hour, bonus)

print(f"Выплата составляет {resoult_wage}")

