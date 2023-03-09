"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

try:
    with open('new_file.txt', 'r', encoding="utf-8") as file:
        my_list = file.readlines()
        print(f'Количество строк в файле {len(my_list)}.')
        for i in range(len(my_list)):
            new_l = my_list[i].split()
            print(f'В {i + 1}-ой строке {len(new_l)} слов(а)')
except FileNotFoundError:
    print('Файл не найден.')
