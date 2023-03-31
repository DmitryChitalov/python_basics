"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random
list_numbers = [random.randint(0, 30) for i in range(random.randint(5, 10))]

with open("file.txt", "w") as f_obj:
    print(' '.join(str(el) for el in list_numbers), file=f_obj)
file = open("file.txt", "r")
content = file.read()
file.close()
sum_fom_file = 0
for el in content.split():
    sum_fom_file += int(el)
print("сумму чисел в файле = ", sum_fom_file )
