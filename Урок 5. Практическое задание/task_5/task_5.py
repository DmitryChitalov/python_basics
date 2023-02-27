"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint
i = 0
my_line = ""
while i <= 100:
    if i < 100:
        my_line += f"{randint(100, 500)} "
    else:
        my_line += f"{randint(100, 500)}"

    i += 1

    my_file = open("05.txt", "w")
    my_file.write(my_line)
    my_file.close()

with open("05.txt", "r") as my_fl:
    new_list = [int(item) for item in my_fl.read().split(' ')]
    print(f"Сумма числе в файле равна: {sum(new_list)}")
