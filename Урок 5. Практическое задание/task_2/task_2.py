"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
from re import findall

# Подсчет количества строк_1
with open('task_2.txt', encoding='utf-8') as f_obj:
    count_line = f_obj.readlines()
    print(f'Количество строк в файле {f_obj.name} - {len(count_line)}')

# Подсчет количества строк_2
lines = 0
with open('task_2.txt', encoding='utf-8') as f_obj:
    for line in f_obj:
        lines += 1
    print(f'Количество строк в файле {f_obj.name} - {lines}')

# Подсчет количества слов в каждой строке
t = 0
with open('task_2.txt', encoding='utf-8') as f_obj:
    for line in f_obj:
        t += 1
        result = len(findall(r'\w+', line))
        print(f'В строке {t} - {result} слов(а)')
