"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, hours_worked, money, bonus = argv

print('Имя скрипта:', script_name)
print('Выроботка в часах:', hours_worked)
print('Ставка в час:', money)
print('Премия:', bonus)


def calculation(hours_worked, money, bonus):
    salary = float(hours_worked) * float(money) + float(bonus)
    return salary


print(f'Зарплата сотрудника = {calculation(hours_worked, money, bonus)} рублей!')
