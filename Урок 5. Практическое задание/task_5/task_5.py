"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import numpy

with open("numbers.txt", "w", encoding="utf-8") as numb:
    list_num = numpy.random.randint(1, 100, size=10)
    print(f'В файл запишем строку {list_num}. Сумма чисел в строке: {numpy.sum(list_num)}')
    numb.write(str(list_num))
