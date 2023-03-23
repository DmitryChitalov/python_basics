"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
def count_info():
    try:
        with open('test.txt', 'r', encoding="utf-8") as file:
            test = file.readlines()
            for i in range(len(test)):
                new_l = test[i].split()
                print(f'Количество строк в файле {len(test)}. В {i + 1}-ой строке {len(test)} слов(а)')
    except FileNotFoundError:
        return 'Файл не найден...'
