------
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия. 
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
------


from sys import argv

script_name, hours_production, rate_per_hour, bonus = argv

print("Имя скрипта: ", script_name)
print("\n<< Программа рассчета заработной платы сотрудника >>")
print("Выработка в часах: ", hours_production)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", bonus)
print("Зарплата сотрудника: ", (float(hours_production) * float(rate_per_hour)) + float(bonus))