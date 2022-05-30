"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

with open("text5.txt", "w") as f1:
    for i in range(10):
        f1.write(str(randint(0, 10000)))
        f1.write(" ")

total = 0
with open("text5.txt", "r") as f2:
    line = f2.readline()
    for integer in line.split():
        total += int(integer)

print(f"Total: {total}")