"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint
with open('random.txt', 'w') as f_obj:
    random_list = [randint(0, 100) for i in range(10)]
    random_string = (' '.join(str(i) for i in random_list))
    f_obj.write(random_string)
print(f'Сумма чисел: {sum(random_list)}')
