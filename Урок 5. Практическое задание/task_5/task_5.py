"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open("text_file5.txt", "r", encoding='utf-8') as f_obj:
    file_summ = 0
    for line in f_obj:
        str_sum = sum(float(x) for x in line.split())
        file_summ += str_sum
print(file_summ)
