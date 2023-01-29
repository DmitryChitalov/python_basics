"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

f_name, name_p, hours_p, rate_p, prize_p = argv
print(f_name)

def paycheck(hours, rate, prize):
    try:
        print(f"Сотрудник {name_p} заработал {(int(hours)*int(rate))+int(prize)}!")
    except TypeError:
        print("Неверное значение!")

print(f"Имя сотрудника: {name_p}")
print(f"Отработано часов: {hours_p}")
print(f"Ставка: {rate_p}")
print(f"Премия: {prize_p}")
paycheck(hours_p, rate_p, prize_p)

"""
В конфигураторе запуска в поле 'Parametrs' необходимо указать;
'Имя сотрудника, отработанные часы, ставку, премию' 
"""