"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
my_var = 0
with open('test.txt', 'w', encoding='utf-8') as my_f:
    my_f.writelines(input('Введите числа через пробел: '))

with open('test.txt', 'r', encoding='utf-8') as my_f:
    content = my_f.read().split()

for i in content:
    my_var += int(i)

print(my_var)


