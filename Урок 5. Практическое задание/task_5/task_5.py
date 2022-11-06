"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


with open('out.txt', 'w', encoding='utf-8') as my_file:
    my_list = input('Введите набор чисел, разделенных пробелами, нажмите enter для окончания ввода:\n')
    my_file.write(my_list)

with open('out.txt', 'r', encoding='utf-8') as my_file:
    my_sum = my_file.read().split(' ')
    result = list(map(int, my_sum))
    print(f'Сумма чисел в файле: {sum(result)}')
