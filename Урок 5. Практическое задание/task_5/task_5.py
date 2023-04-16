"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

line_num = []
for i in range(random.randint(10, 100)):
    line_num.append(random.randint(1, 100))

# отладочный вывод
#print(' '.join(map(str, line_num)))

with open('test.txt', 'w') as fp:
    fp.write(" ".join(str(el) for el in line_num))

with open('test.txt', 'r') as fp:
    my_numb = fp.read().split()

print(sum(map(int, my_numb)))
