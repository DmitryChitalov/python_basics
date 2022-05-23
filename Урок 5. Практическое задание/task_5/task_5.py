"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

some_file = open('somefile.txt', 'w')

for i in range(0, 10):
    some_file.write(f"{i}\n")

some_file = open('somefile.txt', 'r')
sum = 0
for line in some_file:
    sum += float(line)

print(sum)
some_file.close()