"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('new_file.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    line = len(lines)
    print(f'Количество строк: {len(lines)}')
    for key, el in enumerate(lines):
        words = el.split('')
        ptint(f'Количество слов в строке {key + 1}: {len(words)}')

