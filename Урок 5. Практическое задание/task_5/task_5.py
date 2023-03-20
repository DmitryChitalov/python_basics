"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

afile = open("file.txt", "w")
line_str = ""
try:
    for i in range(int(input('Сколько чисел записать в файл?: '))):
        line_str += str(random.randint(1, 100)) + " "
    afile.write(line_str.rstrip())
    print(line_str.rstrip())
except ValueError:
    print("Это не число")
afile.close()

file_ = open("file.txt")
list_of_digits = file_.readline().split()

print(f"Сумма чисел: {sum([int(digit) for digit in list_of_digits])}")

