"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
my_file = open('Text.txt', 'r')
content = my_file.read()
print(f'Файл содержит следующий текст: \n {content}')
my_file = open('Text.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле = {len(content)}')
my_file = open('Text.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов в(о) {i + 1} - строки {len(content[i])}')
my_file = open('Text.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()