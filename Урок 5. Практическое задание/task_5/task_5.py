"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('numbers.txt', 'w', encoding='utf-8') as f_num:
    f_num.write('1 2 3 4 5 6 7 8 9 10')

with open('numbers.txt', encoding='utf-8') as f_num:
    f = f_num.read().split()
    result = sum(map(int, f))
    print(f'Сумма чисел в файле {f_num.name} - {result}')
