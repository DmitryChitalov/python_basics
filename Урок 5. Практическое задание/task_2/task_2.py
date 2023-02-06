"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
line_counter = 0
word_counter = 0
with open('HW5T2.txt', 'r', encoding='utf-8') as in_file:
    i = 1
    for line in in_file:
        word_counter = len(line.split(' '))
        print(f'В строке {i} количество слов: {word_counter}')
        line_counter += 1
        i += 1
print(f'Всего строк в файле: {line_counter}')
