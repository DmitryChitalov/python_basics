"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

file_task2 = open('text2.txt', 'r')
mean = file_task2.readlines()
print(f'Number of lines in file - {len(mean)}')
file_task2 = open('text2.txt', 'r')
mean = file_task2.readlines()
for k in range(len(mean)):
    print(f'Line {k + 1} characters - {len(mean[k])}')
file_task2 = open('text2.txt', 'r')
mean = file_task2.read()
mean = mean.split()
print(f'Total number of words - {len(mean)}')
file_task2.close()
