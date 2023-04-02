"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
#!/usr/bin/env python3
import os
import random

print("Внимание, текущая папка:", os.getcwd())

output_file = open("./output_file5.txt", "w")
random_numbers = random.sample(range(100, 1000), 10)
print(*random_numbers, sep=" ")
line_to_write = " ".join(str(random_numbers))
print(type(line_to_write), line_to_write)
output_file.write(line_to_write)
output_file.close()
print(f"Сумма чисел в файле: {sum(random_numbers)}")
