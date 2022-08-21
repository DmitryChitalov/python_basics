"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
list_numbers = [90, 150, 23, 40]
my_count = 0
out_f = open("task5.txt", "a", encoding='utf-8')
for i in list_numbers:
    out_f.write(str(i) + " ")
out_f.close()
out_f = open("task5.txt", "r", encoding='utf-8')
list_numbers_f = out_f.read()
out_f.close()
list_numbers_f = list_numbers_f.split()
for i in list_numbers_f:
    my_count = my_count + int(i)
print(f"Сумма чисел в файле: {my_count}")
