"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

user_number = input('Введите числа через пробел: ')
user_number = user_number.split()

with open('newfile.txt', 'w') as file:

    for i in user_number:
        file.write(f'{i} ')

count = 0

with open('newfile.txt', 'r') as file:

    date = file.readline()
    date_list = date.split()

    for i in date_list:
        i = int(i)
        count += i

print(f'Сумма числе в файле равна: {count}')
