"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from functools import reduce
file_name_and_path = '/Users/aleksandr_bolokhov/Desktop/GeekBrains/DevOps/Python/homeworks/python_basics/Урок 5. Практическое задание/task_5/data.txt'

with open(file_name_and_path, 'w', encoding='utf-8') as file:
    my_data = [str(i) for i in range(1, 30, 2)]
    file.write(' '.join(my_data))
            

with open(file_name_and_path, 'r', encoding='utf-8') as file:
    sum_my_data  = file.read()
    print(f'Сумма всех числе: {reduce(lambda el_1, el_2: int(el_1) + int(el_2), sum_my_data.split())}')
    
