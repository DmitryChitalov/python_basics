"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

numbers = [random.randint(-50, 100) for _ in range(20)]
print(numbers)
with open('file_5.txt', 'w', encoding='utf-8') as file:
    file.writelines(f'{" ".join(map(str, numbers))} ')

with open('file_5.txt', 'r', encoding='utf-8') as file:
    numbers = map(int, [i for i in file.read().split() if i])

print(f'Sum of the generated numbers: {sum(numbers)}')
