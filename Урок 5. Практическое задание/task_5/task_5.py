"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
file_u = open("number_sum.txt", "w")
summa = 0
x = input("введите несколько чисел через пробел, я запишу их в файл и рассчитаю сумму на экране ")
file_u.write(x)
file_u.close()
file_u = open("number_sum.txt", "r")
line = file_u.read()
num = line.split()
for i in range(0, len(num)):
    y = int(num[i])
    summa = summa + y
print(summa)
file_u.close()