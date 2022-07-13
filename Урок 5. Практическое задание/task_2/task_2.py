"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('task_2.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(f'Количество строк в файле: {len(lines)}')
    line_count = 1
    for line in lines:
        words = len(line.split(" "))
        print(f'В строке {line_count} найдено {words} слов')
        line_count += 1

file.close()
