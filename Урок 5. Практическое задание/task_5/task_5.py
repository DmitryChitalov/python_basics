"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

str_obj = "1 2 3 4 5"
res = 0

with open("output_file.txt", "w", encoding='utf-8') as f_obj:
    f_obj.write(str_obj)

with open("output_file.txt", encoding='utf-8') as f_obj:
    content = f_obj.read().split(" ")
    for n in content:
        res = res + int(n)
    print(f"Сумма чисел = {res}")
