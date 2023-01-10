# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами

import sys

salary, rate, hours, bonus = sys.argv



def salary_caclulation(rate, hours, bonus):
    print(f"зп+премия: {int(rate) * int(hours) + int(bonus)}")


salary_caclulation(rate, hours, bonus)
