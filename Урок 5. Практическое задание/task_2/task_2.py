"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
counter = 0
with open('text_file.txt', 'r') as file:
    for line in file:
        line_splitted = line.split()
        print(f'In line {counter} {len(line_splitted)} words')
        counter += 1
print(f'Total number of rows {counter}')
