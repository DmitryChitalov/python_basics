"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

fp = open("file.txt", "r", encoding="utf-8")

counter_lines = 0
counter_words = 0

for line in fp:
    words = len(line.split())
    counter_words += words
    counter_lines += 1
    print(f"В строке номер {counter_lines} найдено {words} слов")

print(f"Всего в файле строк {counter_lines} и {counter_words} слов.")

fp.close()
