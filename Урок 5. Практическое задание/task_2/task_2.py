"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

word_count = 0

with open("example.txt", "r") as file:

    for i in file:
        date = i.rstrip('\n').split()
        count_list = len(date)
        word_count += 1

        print(f'{word_count} строка содержит {count_list} слов')

print(f'Общее количество строк: {word_count}')
