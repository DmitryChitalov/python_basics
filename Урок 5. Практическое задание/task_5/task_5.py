"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

str_obj = '1 2 3 4 5'
res = 0

with open('numbers.txt', 'w', encoding='utf-8') as f_obj:
    f_obj.write(str_obj)

with open('numbers.txt', 'r', encoding='utf-8') as f_obj:
    cont = f_obj.read().split(' ')
    for i in cont:
        res = res + int(i)
    print(f'Сумма чисел в файле {f_obj.name} = {res}')
