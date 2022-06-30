"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_file = open('test_2.txt', 'r', encoding="utf-8")
file_cont = my_file.readlines()

for i in range(len(file_cont)):
    file_words = file_cont[i].split()
    print(f'В строке {i + 1} слов - {len(file_words)}')

print(f'Количество строк - {len(file_cont)}')
