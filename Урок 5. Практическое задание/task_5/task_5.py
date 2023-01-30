"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('test.txt', 'w+', encoding='utf-8') as f:
    numbers = input('Введите цифры через пробел ')
    f.writelines(numbers)
    result = numbers.split()
    print(sum(map(int, result)))
