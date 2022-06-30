"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randrange

random_numbers = [randrange(1, 13) for _ in range(8)]

with open('task5.txt', 'w') as f:
    f.write(" ".join(map(str, random_numbers)))

with open('task5.txt') as fi:
    numbers = fi.read().split()

    print(sum(int(x) for x in numbers))
