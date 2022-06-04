"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


from functools import reduce


with open('Урок 5. Практическое задание/task_5/task_5.txt', 'w', encoding='utf-8') as f:
    data = '10 20 55 7 9 10'
    f.write(data)

with open('Урок 5. Практическое задание/task_5/task_5.txt', 'r', encoding='utf-8') as f:
    data = f.readline().split()
    print(f'Сумма чисел: {reduce(lambda a, b: int(a) + int(b), data)}')
