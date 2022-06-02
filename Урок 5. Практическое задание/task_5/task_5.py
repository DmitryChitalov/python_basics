"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from functools import reduce

with open('text_fi.txt', 'w', encoding='utf-8') as file:
    print('2 3 4 553 34324 2343 43', file=file)

with open('text_fi.txt', 'r', encoding='utf-8') as file:
    stri = file.readline()
    li = [int(i) for i in stri.split()]
    print(reduce(lambda a,b : a + b, li))