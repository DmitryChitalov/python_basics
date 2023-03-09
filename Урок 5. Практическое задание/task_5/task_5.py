"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

try:
    with open('n_file.txt', 'w') as n_file:
        n_file.write(input('Введите числа через пробел: '))
    with open('n_file.txt', 'r') as n_file:
        line = n_file.read()
        nums = map(int, line.split())
        print(sum(nums))
except FileNotFoundError:
    print('Файл не найден.')
