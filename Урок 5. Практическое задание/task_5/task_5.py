"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

c = 0

f_obj = open("HW5_task5.txt", "w", encoding='utf-8')
my_str = input("Введите целые числа через пробел: ")
f_obj.write(my_str)
a = list(my_str.split(' '))
for el in a:
    c += int(el)
print(c)

f_obj.close()