"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

import os

path = os.path.dirname(__file__)

lines = 0

try:
    with open((os.path.join(path, 'file.txt')), "r") as text_file:
        for line in text_file:
            lines += 1
            word = line.split()
            print(f"В {lines} строке {len(word)} слов")
    print(f"Всего в файле {lines} строк")
except:
    print("Файла не существует")
