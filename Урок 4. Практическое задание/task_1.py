"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""


def calc_salary(hours, salary, additional_money):
    print(f"Итоговая зп: {hours * salary * additional_money}")


worker_hours = float(input("Введите часы "))
worker_salary = float(input("Введите зп за час "))
worker_additional_money = float(input("Введите множитель премии "))

calc_salary(worker_hours, worker_salary, worker_additional_money)