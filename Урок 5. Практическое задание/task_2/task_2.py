"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
#!/usr/bin/env python3
import os
os.getcwd()
print("Уточняю расположение файла вывода функцией os.getcwd():", os.getcwd())


input_data = open("./input_file2.txt", "r")
lines_in_file = 0
words_in_line = 0
counting_lines = {}

for i in input_data:
    lines_in_file +=1


print(f"{lines_in_file} и {words_in_line}.")

input_file.close()
