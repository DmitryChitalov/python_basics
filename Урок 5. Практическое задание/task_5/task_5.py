"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import csv

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]
with open('file.txt', 'w', encoding='utf8') as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerow(a)

summ = 0
with open('file.txt', 'r', encoding='utf8') as f:
    reader = csv.reader(f, delimiter=' ')
    for el in reader:
        for i in el:
            summ += int(i)
print(summ)
