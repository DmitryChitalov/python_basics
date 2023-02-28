"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def count_data():
    try:
        with open('Test.txt', 'r', encoding="utf-8") as file:
            my_list = file.readlines()
            for i in range(len(my_list)):
                new_list = my_list[i].split()
                print(f'Количество слов в строке №{i + 1}: {len(new_list)}')
            print(f'Общее количество строк: {len(my_list)} ')
    except FileNotFoundError:
        return 'Файл отсутствует.'


count_data()
