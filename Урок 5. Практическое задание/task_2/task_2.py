"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('example.txt', 'r') as file:
    content = file.readlines()

    num_lines = len(content)
    print(f'Количество строк: {num_lines}')

    for line in content:
        words = line.split()
        num_words = len(words)
        print(f'Количество слов в строке "{line.strip()}": {num_words}')
