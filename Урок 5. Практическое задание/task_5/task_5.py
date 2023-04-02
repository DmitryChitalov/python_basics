"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random
with open("text4.txt", "w+") as txt_file:
    for i in range(random.randint(1,10)):
        txt_file.write(str(random.randint(1,100)) + " ")
n = 0
with open("text4.txt") as txt_file:
    for i in txt_file.read().split():
        n += int(i)
print(n)