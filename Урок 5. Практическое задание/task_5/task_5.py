"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

randomlist = random.sample(range(10, 1000), 5)

with open('file.txt', 'w') as file:
    for number in randomlist:
        file.write(str(number) + ' ')

with open('file.txt', 'r') as file:
    content = file.read()
    content = content.split()

result = 0
for number in content:
    result += int(number)
print(result)