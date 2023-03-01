"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

afile = open("file.txt", "w")

try:
    for i in range(int(input('Сколько чисел записать в файл?: '))):
        line = str(random.randint(1, 100)) + " "
        afile.write(line)
        print(line)
except ValueError:
    print("Это не число")

print(f"Сумма чисел: {afile}")
afile.close()

