"""
5)	Создать (программно) текстовый файл, записать в него программно набор
чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел
в файле и выводить ее на экран.
"""

from random import randint

with open("text_file_5.txt", "w") as my_f1:
    for i in range(10):
        my_f1.write(str(randint(0, 10000)))
        my_f1.write(" ")

total_sum = 0
with open("text_file_5.txt", "r") as my_f2:
    line = my_f2.readline()
    for integer in line.split():
        total_sum += int(integer)
print(f"Сумма чисел в файле: {total_sum}")
