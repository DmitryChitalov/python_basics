"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


lines = 0
words = 0
lines_words = {}
with open("text.txt") as my_file:
    for i in my_file:
        if i != '\n':
            lines += 1
            words = len(i.split())
            lines_words["Cтрока_" + str(lines)] = words
print(f"Количество строк: {lines}")
print(f"Количество слов в строке: {lines_words}")
