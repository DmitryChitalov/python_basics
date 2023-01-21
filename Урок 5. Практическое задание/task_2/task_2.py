"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

count_lines = 0
count_words = 1

with open ('test.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        print('\n' + line)
        for i in line:
            if i == ' ':
                count_words += 1
        count_lines += 1
        print(f'Количество слов в строке {count_lines} = {count_words}')
        count_words = 1


