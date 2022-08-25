"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
file = open('test.txt', 'r', encoding='utf-8').read().splitlines()
lines_count = 0
for i in file:
    lines_count += 1
    words_count = len(i.split(' '))
    print(f'line:{lines_count} [{i}] word count: {words_count}')
print(f'total lines count: {lines_count}')
