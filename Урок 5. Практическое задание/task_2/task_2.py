"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
#!/usr/bin/env python3
import os
os.getcwd()
print("Уточняю расположение файла функцией os.getcwd():", os.getcwd())

lines_in_file = 0
words_in_line = 0
counting_lines = {}

with open("input_file2.txt", "r") as file:
    file_data = file.readlines()
    
    for i in file_data:
        words_in_line = len(file_data[lines_in_file].split(" "))
        counting_lines.update({lines_in_file: words_in_line})
        lines_in_file += 1
        print(f"В строке {lines_in_file} Питон прочел {words_in_line} сл.")
