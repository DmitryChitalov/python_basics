"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import numpy as np

base_list = np.random.randint(10, 100, 5)
line = ' '.join(str(x) for x in base_list)
fw = open("numbers.txt", "w")
fw.write(line)
fw.close()

fr = open("numbers.txt", "r")
line = fr.read()
fr.close()
print("Summ: " + str(sum(list(int(x) for x in line.split()))))
