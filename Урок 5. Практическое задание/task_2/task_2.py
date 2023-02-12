"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('my_file.txt', 'r', encoding='utf-8') as my_file:
    f_string = 0
    for line in my_file:
        f_string += 1
        words = len(line.split(' '))
        print(f'В строке = {words} слов')

print(f'Строк в файле = {f_string}')
