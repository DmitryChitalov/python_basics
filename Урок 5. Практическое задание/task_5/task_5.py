"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

with open("some_numbers.txt", "w", encoding="utf-8") as my_file:
    for i in range(10):
        my_file.write(str(random.randint(1, 100)) + " ")  # Записали 10 рандомных чисел в файл

with open("some_numbers.txt", "r", encoding="utf-8") as my_file:
    number_list = my_file.readline().split()
    print(number_list)  # В переменную number_list записали значения чисел

final_result = 0  # Сюда будем записывать суммы всех чисел
for i in number_list:
    final_result += int(i)

print(final_result)
