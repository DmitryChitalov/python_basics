"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
sum_1 = 0
with open('test.txt', 'w') as num_file:
    nums = input('Введите числа через пробел: ')
    num_file.write(nums)
with open('test.txt') as num_file:
    for i in num_file.read().split():
        sum_1 += int(i)
    print(sum_1)