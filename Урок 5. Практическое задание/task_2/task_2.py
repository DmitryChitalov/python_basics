"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

"""
Выполенине! Емельяненко А.А.
"""


def count_info():
    try:
        with open('file.txt', 'r', encoding="utf-8") as file:
            my_list1 = file.readlines()
            for a in range(len(my_list1)):
                new_list1 = my_list1[a].split()
                print(f'Количество строк в файле {len(my_list1)}. В {a + 1}-ой строке {len(new_list1)} слов(а)')
    except FileNotFoundError:
        return 'Файл не найден.'


count_info()
