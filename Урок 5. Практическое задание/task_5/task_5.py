"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random
with open('test.txt', 'w', encoding='UTF-8') as test:
    glue = ''
    for _ in range(5):
        test.write(glue + str(random.randint(0, 10)))
        glue = ' '
with open('test.txt', 'r', encoding='UTF-8') as test:
    numbers_str = test.read()
    numbers_lst = numbers_str.split(' ')
    print(f"Содержимое файла:\n{numbers_str}")
    print(f"Сумма чисел:\n{sum([int(i) for i in numbers_lst])}")