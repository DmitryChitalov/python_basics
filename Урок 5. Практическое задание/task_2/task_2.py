"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
my_f = open('text_2.txt', 'r', encoding='utf-8')
content = my_f.read()
print(f'Содержимое файла: \n {content}')

my_f = open('text_2.txt', 'r', encoding='utf-8')
content = my_f.readlines()
print(f'Кол-во строк в файле - {len(content)}')

my_f = open('text_2.txt', 'r', encoding='utf-8')
content = my_f.readlines()
for i in range(len(content)):
    print(f'Кол-во символов {i + 1}  строки {len(content[i])}')

my_f = open('text_2.txt', 'r', encoding='utf-8')
content = my_f.read()
content = content.split()
print(f'Общее кол-во слов - {len(content)}')
my_f.close()