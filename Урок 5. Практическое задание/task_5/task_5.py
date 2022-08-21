"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from itertools import count

my_file = open("c:\Python38\\text6.txt", "w", encoding="utf-8")
for i in count(30):
    if i > 100:
        break
    my_file.write(str(i) + " ")
my_file.close()
print("Данные сохранены в c:\Python38\\text6.txt")

my_file = open("c:\Python38\\text6.txt", "r", encoding="utf-8")
my_list = my_file.read().split()
result = 0
for i in my_list:
    try:
        result_i = float(i)
    except ValueError:
        result_i = 0
    result += result_i
my_file.close()
print(f"Итог последовательности: {result}")
