"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

strings = 0
words = 0
with open('my_file.txt', encoding='utf-8') as f_obj:
    for line in f_obj:
        strings += 1
        words = len(line.split())
        print(line)
        print(f'Слов в строке: {words}')
print(f'Строк: {strings}')
