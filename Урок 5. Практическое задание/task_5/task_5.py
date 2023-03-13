"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

rnd_numb = [random.randint(1, 100) for i in range(1, 30)]

with open('random_num_sum.txt', 'w+', encoding='utf-8') as file:
    file.writelines('%s ' % line for line in rnd_numb)

with open('random_num_sum.txt', 'r', encoding='utf-8') as file:
    result = 0
    for el in file.read().split():
        result += int(el)
print(result)