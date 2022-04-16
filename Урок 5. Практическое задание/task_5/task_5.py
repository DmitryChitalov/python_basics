"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('test.txt', 'w+') as my_file:
    my_input = input('введите число через пробел ')
    my_file.writelines(my_input)
with open('test.txt', 'r') as my_file:
    content = my_file.read()
    content = content.split()
    print(sum(map(int, content)))
