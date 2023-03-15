"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
line = input('Введите текст: ')

with open('new_file.txt', 'w') as new_file:
    print(line, file=new_file)

new_file = open('new_file.txt', 'r', encoding='utf-8')
content = new_file.read()
print(f'Содержимое файла: {content}')

new_file = open('new_file.txt', 'r')
content = new_file.readlines()
print(f'Количество строк в файле {len(content)}')

new_file = open('new_file.txt', 'r')
content = new_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')

new_file = open('new_file.txt', 'r')
content = new_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')

new_file.close()