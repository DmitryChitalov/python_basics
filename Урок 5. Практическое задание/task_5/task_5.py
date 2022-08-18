"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open("sum.txt", 'w', encoding='utf-8') as f_obj:
    f_obj.write("12 2 333 4 5222 6453 73 825 9")

with open("sum.txt", 'r', encoding='utf-8') as f_obj:
    print(sum(int(number) for number in f_obj.readline().split()))
