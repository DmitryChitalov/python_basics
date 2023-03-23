"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def count_info():
    try:
        with open('task2.txt', 'r', encoding="utf-8") as file:
            my_list = file.readlines()
            for i in range(len(my_list)):
                new_1 = my_list[i].split()
                print(f'В {i + 1} строке {len(new_1)} слов. Всего строк: {len(my_list)}.')
    except FileNotFoundError:
        return 'Файл не найден'

count_info()