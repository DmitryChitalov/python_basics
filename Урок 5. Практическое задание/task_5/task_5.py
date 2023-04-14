"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random
with open("text.txt", "w+") as my_file:
    for i in range(random.randint(1, 10)):
        my_file.write(str(random.randint(1, 100)) + " ")
num = 0
with open("text.txt") as my_file:
    for i in my_file.read().split():
        num += int(i)
print(f"Сумма чисел в файле: {num}")
