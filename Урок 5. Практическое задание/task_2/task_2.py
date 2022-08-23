"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('task_2.txt', 'r', encoding="utf-8") as my_file:
    list_1 = my_file.readlines()
    for i in range(len(list_1)):
        list_2 = list_1[i].split()
        print(f'Строк в файле {len(list_1)}. {i + 1}-я строка, Кол-во слов: {len(list_2)}')
