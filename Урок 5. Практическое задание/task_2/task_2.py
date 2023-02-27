"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
num_words = 0
num_lines = 1
with open("file.txt", 'r') as f:
    for line in f:
        num_lines += 1
        num_words += len(line.split())
print(f"Строк в файле: {num_lines}")
print(f"Слов в файле: {num_words}")