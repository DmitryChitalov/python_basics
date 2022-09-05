"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('file.txt', 'w', encoding='utf-8') as my_file:
    ls = list(range(20))
    for i in ls:
        ls[i] = str(ls[i])
    st = ' '.join(ls)
    my_file.write(st)

with open('file.txt', 'r', encoding='utf-8') as r_file:
    for line in r_file:
        ls = line.split()
        ls = [int(i) for i in ls]
        print(f'Сумма чисел в строке {sum(ls)} ')