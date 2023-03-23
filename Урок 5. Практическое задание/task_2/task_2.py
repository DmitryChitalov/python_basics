"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

test2 = open('test2.txt', 'r')
content = test2.read()
print(f'Содержимое файла: \n {content}')
test2 = open('test2.txt', 'r')
content = test2.readlines()
print(f'Количество строк в файле - {len(content)}')
test2 = open('test2.txt', 'r')
content = test2.readlines()
for i in range(len(content)):
    print(f'Кол-во символов {i + 1} - ой строки {len(content[i])}')
test2 = open('test2.txt', 'r')
content = test2.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()
