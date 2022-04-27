"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from functools import reduce
import random

def get_ints(lst):
    for el in lst:
        if str.isdigit(el):
            yield int(el)

with open("task5.txt", "w", encoding = "utf-8") as file:
    count_elements = random.randint(1, 40)
    for el in range(count_elements):
        file.write(f"{random.randint(1, 100)} ")

with open("task5.txt", "r", encoding = "utf-8") as file:
    line_numbers = file.readline()
    file_numbers = get_ints(line_numbers.split(" "))
    
    print(f"Result = {reduce(lambda a, b: a + b, file_numbers)}")