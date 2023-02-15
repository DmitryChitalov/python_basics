"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
f2 = open('test_2.txt', 'r')
content = f2.read()
print(f'Содержимое файла: \n {content}')
f2 = open('test_2.txt', 'r')
content = f2.readlines()
print(f'Количество строк в файле - {len(content)}')
f2 = open('test_2.txt', 'r')
content = f2.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
f2 = open('test_2.txt', 'r')
content = f2.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
f2.close()