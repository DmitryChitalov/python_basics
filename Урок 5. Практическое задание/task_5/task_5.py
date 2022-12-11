"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

my_file = open("calc_sum.txt", "w")
my_file.write("3 25 532 123 342 45")
my_file.close()

res_file = open("calc_sum.txt", "r")
read_file = res_file.read()
total = 0
for el in read_file.split(" "):
    total += int(el)
res_file.close()
print("Сумма всех чисел равна: ", total)