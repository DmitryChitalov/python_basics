"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
def count_data():
    try:
        with open('test.txt', 'r', encoding="utf-8") as file:
            my_list = file.readlines()
            for i in range(len(my_list)):
                new_list = my_list[i].split()
                print(f'Количество слов в {i + 1} строке: {len(new_list)}')
            print(f'Общее количество строк: {len(my_list)} ')
    except FileNotFoundError:
        return 'Файл отсутствует.'


count_data()