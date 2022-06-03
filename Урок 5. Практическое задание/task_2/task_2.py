"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

lines = 0
words = 0

with open('lorem.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        print(line.replace('\n', ''))
        for i in line:
            if i == ' ':
                words += 1
        lines += 1
        print(f'Количество слов в строке {lines} = {words} \n')
        words = 1
    print(f'В файле {f_obj.name} {lines} строк(и)')
