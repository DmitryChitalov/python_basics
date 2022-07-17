"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_file = open('my_file.txt', 'r', encoding='utf-8')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('my_file.txt', 'r', encoding='utf-8')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов в {i + 1} строке {len(content[i])}')
my_file.close()