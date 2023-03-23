"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random
from functools import reduce

def list_summ(summ, next_val):
    return summ + next_val

with open('task5.txt', 'w') as num_data_file:
    for i in range(100):
        num_data_file.write(str(random.randint(0, 999)) + ' ')

with open('task5.txt', 'r') as num_data_file:
    num_list = num_data_file.readline().strip().split(' ')
    print(num_list)

    # Преобразование элементов списка из str в int
    for i, el in enumerate(num_list):
        num_list[i] = int(el)
    print(num_list)

    total = reduce(list_summ, num_list)

print('Сумма случайных чисел:', total)