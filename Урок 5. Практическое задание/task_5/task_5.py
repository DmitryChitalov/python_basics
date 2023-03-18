a = open("file+.txt", "w", encoding='utf-8')
list1 = "1 2 3 4 5 6 7"
a.writelines(list1)
a.close()
a = open("file+.txt", "r", encoding='utf-8')
b = a.read()
list1 = b.split()
a.close()
c = 0
for el, el2 in enumerate(list1):
    c += int(el2)
print(c)

"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
