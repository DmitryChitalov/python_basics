"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('my_file.txt', 'w', encoding='utf-8') as my_file:
    line = (input('Введите числа через пробел: '))
    my_file.writelines(line)
    content = line.split()

print(sum(map(int, content)))