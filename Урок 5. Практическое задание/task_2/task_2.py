"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
f = open('task_2_text.txt', 'r', encoding='utf-8')
text_lines = 0
text_words = 0
for line in f:
    line = line.strip('/n')
    text_words = len(line.split())
    text_lines += 1
    print(f'Number of line: {text_lines}, words in line: {text_words}')
f.close()
