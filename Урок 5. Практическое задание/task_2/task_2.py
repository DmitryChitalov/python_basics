"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

lines = 0
words = 0
with open('text2.txt') as f:
    for line in f:
        lines += 1
        words += len(line.split())
print("Lines:", lines)
print("Words:", words)