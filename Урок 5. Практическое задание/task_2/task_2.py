"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
f = open('task_2.txt', 'r', encoding="utf-8")
line_num = 0
words_count = 0
total_words = 0
for line in f:
    line = line.strip("\n")
    words_count = len(line.split())
    line_num += 1
    total_words += words_count
    print(f'Line num: {line_num}; words count: {words_count}; line = {line}')
f.close()
print(f'Total lines: {line_num}; Total words: {total_words}')