"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('test2.txt', 'r', encoding='utf-8') as my_file:
    test = my_file.readlines()
    line = len(test)
    print(f'Кол-во строк: {line}')

    for ele in test:
        elem = ele.split()
        elem_count = len(elem)
        print(f'Количество слов в строке {elem_count}')