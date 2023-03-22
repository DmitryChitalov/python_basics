"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('ex2.txt', 'r', encoding='utf-8') as text:
    content = text.readlines()

    lines_count = len(content)
    print(f'Количество строк: {lines_count}')

    for item in content:
        words = item.split()
        words_count = len(words)
        print(f'Количество слов в строке "{item.strip()}": {words_count}')
