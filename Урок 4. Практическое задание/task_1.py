"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

try:
    script_name, hh_count, hour_rate, bonus = argv
except ValueError:
    print('\nВведено недостаточное количество параметров!\n')
else:
    try:
        salary = (float(hh_count) * float(hour_rate)) + float(bonus)
    except ValueError:
        print('\nОшибка преобразования введенных параметров!\n')
    else:
        print(f'\nКоличество часов {hh_count} * Ставка в час, ₽ {hour_rate} + Премия, ₽ {bonus} = {salary} ₽ \n')