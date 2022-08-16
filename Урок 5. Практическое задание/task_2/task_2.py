"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
import os


cur_dir = os.path.join('Урок 5. Практическое задание', 'task_1')
file_path = os.path.join(cur_dir, 'result.txt')
with open(file_path, 'r', encoding='utf-8') as f:
    data = f.readlines()
    print(f'Количество строк: {len(data)}')
    i = 1
    for el in data:
        words = el.split(' ')
        print(f'Слов в строке {i}: {len(words)}')
        i += 1
    