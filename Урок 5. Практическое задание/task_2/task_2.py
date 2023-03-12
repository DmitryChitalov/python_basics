"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

from collections import Counter

def read_file(file_name):
    file = open(file_name, "r", encoding="utf-8")
    return file.readlines()

def word_stat(line):
    words = line.split()
    return len(words)

lines = read_file("input.txt")
length = len(lines)
print("Total lines of file:", length)
for i in range(0, length):
    line = lines[i].replace('\n', '')
    print(f"{i + 1}: '{line}': {word_stat(lines[i])}")