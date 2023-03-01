"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("my_file_t2.txt", 'r', encoding='utf-8') as my_file:
    string_counter = 0
    for i in my_file:
        string_counter += 1
        print(f'в строке {string_counter} - {len(i.split())} элементов')
    print(f'Всего в файле {string_counter} строк')
