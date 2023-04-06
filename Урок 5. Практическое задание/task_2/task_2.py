"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
line = 0
words = 0
lines_words = {}
with open("text1.txt") as txt_file:
    for i in txt_file:
        if i != '\n':
            line += 1
            words = len(i.split())
            lines_words['строка_' + str(line)] = words
print("всего строк:", line)
print(lines_words)