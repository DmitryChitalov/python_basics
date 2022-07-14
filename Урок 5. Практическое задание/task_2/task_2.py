"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

count, words = 0, []
with open('input.txt') as f:
    for line in f:
        words.append(len(line.split()))
        count += 1
print(f'Строк: {count}')
print(f'Слов: {words}')
