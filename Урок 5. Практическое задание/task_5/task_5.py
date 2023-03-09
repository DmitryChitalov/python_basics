"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

rnd_int = [str(randint(1, 100)) for el in range(15)]

with open('numbers.txt', 'w') as f:
    f.write(' '.join(rnd_int))

with open('numbers.txt', 'r') as f:
    s = f.read()


out_f = [int(el) for el in s.split()]
print(sum(out_f))
