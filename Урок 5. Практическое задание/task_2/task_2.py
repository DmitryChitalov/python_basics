"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('task_2.txt', 'r', encoding='utf-8') as perf:
    res = [f'{line}. {count.strip()} - {len(count.split())} words'
           for line, count in enumerate(perf, 1)]
    print(*res, f'Strings - {len(res)}.', sep='\n')
