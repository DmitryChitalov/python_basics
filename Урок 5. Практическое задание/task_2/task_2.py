"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('test.txt', 'r') as fp:
    content = fp.readlines()
    print(f'Количество строк в файле - {len(content)}')
    for i in range(len(content)):
        print(f'Окличество слов {i + 1}-ой строки: {len(content[i].split())}')
