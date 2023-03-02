"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, production, bet_in_hour, prize = argv

print("Имя скрипта:", script_name)
print("Выработка в часах:", production)
print("Ставка в час:", bet_in_hour)
print("Премия:", prize)


def salary(prod, bet, priz):
    a = int(prod)
    b = int(bet)
    c = int(priz)
    result = a * b + c
    return result


print(f"Зарплата составит: {salary(production, bet_in_hour, prize)} руб.")
