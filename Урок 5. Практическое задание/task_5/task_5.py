"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

def generate_file(file_name, count):
    with open(file_name, 'w', encoding='utf-8') as out_file:
        for i in range(0, count):
            number = random.randrange(100)
            out_file.write(f'{number} ')

generate_file("input.txt", 50)

sum = 0
with open("input.txt", "r", encoding="utf-8") as in_file:
    for num_str in in_file.readline().split(" "):
        if (num_str != ''):
            sum += int(num_str)

print("sum=", sum)