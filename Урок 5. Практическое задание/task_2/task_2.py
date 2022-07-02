"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


file_lines = 0
file_words = 0

with open('file.txt', 'r', encoding='utf-8') as my_f:
    for line in my_f:
        words = line.split()
        file_lines += 1
        file_words += len(words)

print(f"Количество строк - {file_lines}, количество слов - {file_words}")
