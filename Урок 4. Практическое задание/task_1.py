from sys import argv
if len(argv) > 1:
    name_script, work_hours, hour_rate, bonus = argv
    work_hours = int(hour_rate)
    hour_rate = int(hour_rate)
    bonus = int(bonus)
    print((work_hours * hour_rate) + bonus)
else:
    work_hours = int(input("Выработка в часах: "))
    hour_rate = int(input("Ставка в час: "))
    bonus = int(input("Премия: "))
    print((work_hours * hour_rate) + bonus)
    