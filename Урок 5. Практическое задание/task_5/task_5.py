"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


import random
 
count = int(input("введите количество числ"))
index = 0
file_text=""
while index<count-1:
    index += 1
    file_text += str(random.randint(1, 100)) + " "
file_text += str(random.randint(1, 100))

print("File Content is {}".format(file_text))

file1 = open('numbers.txt', 'w')
file1.write(file_text)
file1.close()

with open('numbers.txt', 'r') as file:
	data = file.read().replace('\n', '')

#data = file_text

list_numbers = data.split()

sum=0
for number in list_numbers:
	sum+=int(number)
print("Average Numbers is {}".format(sum/len(list_numbers)))
