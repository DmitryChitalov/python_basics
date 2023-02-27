"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

row_count = 0

with open('02.txt', 'r') as my_fl:
    for line in my_fl:
        row_count += 1
        word_count = len(line.strip().split())

        print(f'Строка {row_count} содержит {word_count} слова ')


print(f'Всего {row_count} строк')
