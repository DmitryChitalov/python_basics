"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
file_1 = open('file_1.txt', 'r')
content = file_1.read()
print(f'Содержимое файла: \n {content}')
file_1 = open('file_1.txt', 'r')
content = file_1.readlines()
print(f'Количество строк в файле - {len(content)}')
file_1 = open('file_1.txt', 'r')
content = file_1.readlines()
for i in range(len(content)):
    print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
file_1 = open('file_1.txt', 'r')
content = file_1.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
file_1.close()
