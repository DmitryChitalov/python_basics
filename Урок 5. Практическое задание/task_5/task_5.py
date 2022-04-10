"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

i = 0
my_string = ""

while i <= 100:
    if i < 100:
        my_string += f"{randint(0, 1000)} "
    else:
        my_string += f"{randint(0, 1000)}"

    i += 1

my_file = open("my_file05_05.txt", "w")
my_file.write(my_string)
my_file.close()

with open("my_file05_05.txt", "r") as my_file_for_read:
    new_list = [int(item) for item in my_file_for_read.read().split(' ')]
    print(f"Сумма числе в файле равна: {sum(new_list)}")
