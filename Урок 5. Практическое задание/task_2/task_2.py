"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

open_file = open('text2.txt', 'r')
text_file = open_file.read()
print(f'Содержимое файла:\n{text_file}')

open_file = open('text2.txt', 'r')
text_file = open_file.readlines()
print(f'Количество строк в файле: {len(text_file)}')

open_file = open('text2.txt', 'r')
text_file = open_file.read()
text_file = text_file.split()
print(f'Количество слов: {len(text_file)}')
open_file.close()

