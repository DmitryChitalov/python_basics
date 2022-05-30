"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('file_2.txt', 'r', encoding='utf-8') as file:
    total_words, lines = 0, 0
    line = file.readline()
    while line:
        print(f'Content: {line}', end='')
        words_in_line = len(line.split(" "))
        print(f'Number of words: {words_in_line}')
        total_words += words_in_line
        lines += 1
        line = file.readline()
    print(f'Number of lines: {lines}, Total number of words: {total_words}')
