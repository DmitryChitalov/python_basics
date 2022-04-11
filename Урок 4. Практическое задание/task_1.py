"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

f_name, w_time, salary, add_bonus = argv
try:
    w_time = int(w_time)
    salary = int(salary)
    add_bonus = int(add_bonus)
    result = w_time * salary + add_bonus
    print(f"Заработная плата работника составила: {result} у.е.")
except ValueError:
    print("Вводить нужно только числа!")


######
def sal():
    try:
        hour = float(input("Выработка в часах: "))
        bet = int(input("Ставка за час (у.е.): "))
        premium = int(input("Премия (у.е.): "))
        calculation = hour * bet + premium
        print(f"Заработная плата работника составила: {calculation} у.е.")
    except ValueError:
        return print("Вводить нужно только числа!")


sal()
