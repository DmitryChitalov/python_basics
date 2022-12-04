from sys import argv

script_name, time_work, wage_rate, bonus = argv
print("Имя скрипта: ", script_name)
print("Выработка в часах: ", time_work)
print("Cтавка в час: ", wage_rate)
print("Премия: ", bonus)
print("Заработная плата сотрудника: ", float(time_work) * float(wage_rate) + float(bonus))
