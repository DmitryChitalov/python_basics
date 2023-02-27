"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

from os.path import join, abspath

file_name = join('.', '1', '2', 'xxx.py')
try:
    print(file_name)
    print(abspath(file_name))

    file_py = open(file_name, 'r')

    line_count = 0
    word_count = 0
    line_word_count = 0
    for line_str in file_py:
        line_count += 1
        line_word_count = len(line_str.split())
        word_count += line_word_count
        print(f'Строка # {line_count: 03}: {line_str.strip()}. \t Количество слов в строке: {line_word_count}')

    print()
    print('Всего строк в файле:', line_count)
    print('Всего слов в файле:', word_count)
except:
    print('Ошибка при открытии файла!')
finally:
    file_py.close()