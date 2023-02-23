"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""


from sys import argv

script_name, hours, hourcost, bonus = argv


def payment(hours, hourcost, bonus):
    try:
        print(f'{(int(hours) * int(hourcost)) + int(bonus)}')
    except ValueError:
        print("Параметр должен быть числом")

payment(hours, hourcost, bonus)