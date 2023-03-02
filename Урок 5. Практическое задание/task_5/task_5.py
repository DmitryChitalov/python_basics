"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

numbers = [1, 2, 3, 4, 5]

with open('numbers.txt', 'w') as file:
    for number in numbers:
        file.write(str(number) + ' ')

with open('numbers.txt', 'r') as file:
    numbers = [int(number) for number in file.read().split()]

sum_of_numbers = sum(numbers)
print('Сумма чисел:', sum_of_numbers)
