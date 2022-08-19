"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
платы сотрудника.
"""
+ from sys import argv
+
+
+ def salary(hours, base, bonus):
+       """ Salary """
+ return int(hours) * int(base) + int(bonus)
+
+
+ print(salary(argv[1], argv[2], argv[3]))
