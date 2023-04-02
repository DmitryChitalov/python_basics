"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
#!/usr/bin/env python3
import os
import random

print("Внимание, текущая папка:", os.getcwd())

with open("./output_file5.txt", "a") as output_file:
    random_numbers = random.sample(range(100, 1000), 10)
    print(*random_numbers, sep=" ")

    for i in random_numbers:
        output_file.write(str(i) + " ")

print(f"Сумма чисел в файле: {sum(random_numbers)}")
