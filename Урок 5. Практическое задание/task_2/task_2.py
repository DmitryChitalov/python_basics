"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

lines = 0
words = 0
symbols = 0
with open("file2.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        lines += 1
        words += len(line.split())

print(f"Lines: {lines}")
print(f"Words: {words}")
