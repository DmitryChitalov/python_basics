"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

import os

with open("task2.txt", "r", encoding = "utf-8") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")
    for i, line in enumerate(lines):
        words = line.split(" ")
        print(f"Line {i + 1} has {len(words)} words")