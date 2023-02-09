"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('summary.txt', 'w+', encoding='utf-8') as file:
    numbers = input('Введите цифры через пробел ')
    file.writelines(numbers)
    result = numbers.split()
    print(sum(map(int, result)))
