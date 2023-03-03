"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
try:
    with open('nums.txt', 'w') as num:
        num.write(input('Введите числа через пробел: '))
    with open('nums.txt', 'r') as num:
        line = num.read()
        numbs = map(int, line.split())
        print(sum(numbs))
except FileNotFoundError:
    print('Файл не найден.')