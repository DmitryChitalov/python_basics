from sys import argv

script_name, time, cash, bonus = argv

rez = (int(time) * int(cash)) + int(bonus)
print(f"Выплата составляет -  {rez}")
