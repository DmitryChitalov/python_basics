"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
my_dict = {"15", "16", "17", "18",
           "19", "16", "21", "23", "25", "12", "90"}
s1 = 0
with open("file_1.txt", "w") as out_file:
    for x in my_dict:
        out_file.writelines(x)
        out_file.writelines(' ')

with open("file_1.txt", "r") as my_file:
    text_file2 = my_file.readlines()
for el in text_file2:
    words = el.split()
    for i in range(len(words)):
        s1 += int(words[i])

print("Сумма чисел", s1)
