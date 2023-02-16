"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
user_list = list(input('Введите целые числа через пробел : ').split(' '))

with open('DZ_tast_5.txt', 'w', encoding='utf-8') as out_f:
    out_f.writelines(' '.join(user_list))

with open('DZ_tast_5.txt', 'r', encoding='utf-8') as my_file:
    my_list = my_file.readline().split(" ")

summ = 0

for line in my_list:
    summ += float(line)

print(f'Сумма чисел в файле = {summ}')
