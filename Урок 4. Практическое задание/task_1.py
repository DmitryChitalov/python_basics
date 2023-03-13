"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
import sys

def calc_salary(name, rate, hours, bonus=0):
    try:
        salary = int(rate) * int(hours) + int(bonus)
        print(f'Сотрудник {name} заработал {salary}')
    except TypeError:
        print("Операция применена к объкту несоответствующего типа")
        exit()

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Недостаточно аргументов")
        exit()
    elif len(sys.argv) == 4:
        _, name, rate, hours = sys.argv
        calc_salary(name, rate, hours)
    else:
        _, name, rate, hours, bonus = sys.argv
        calc_salary(name, rate, hours, bonus)