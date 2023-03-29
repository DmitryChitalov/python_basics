"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('some_text.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    line = len(lines)
    print(f'Количество строк: {line}')
    for elem in lines:
        words = elem.split()
        words_count = len(words)
        print(f'Количество слов в строке: "{elem.strip()}": {words_count}')
