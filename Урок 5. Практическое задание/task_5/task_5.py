"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random


def writeToFile():
    with open('numbers.txt', 'a', encoding='utf-8') as f_num:
        for num in range(10):
            number = random.randint(0, 10)
            f_num.write(f'{number} ')


writeToFile()
with open('numbers.txt', 'r', encoding='utf-8') as file:
    content = file.readline()
    numbers = content.split()

print(sum(map(int, numbers)))
