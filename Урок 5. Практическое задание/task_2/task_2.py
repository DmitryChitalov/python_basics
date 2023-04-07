"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
line = 0
with open('new_file.txt', 'r', encoding='utf-8') as my_file:
    for i in my_file:
        if i != '\n':
            line += 1
            word = i.split()
            count = len(word)
            print(f'Слов в строке {line}: {count}')
    print(f'Строк в файле: {line}')
    my_file.close()