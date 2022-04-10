"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

def info():
    try:
        with open('test.txt', 'r', encoding="utf-8") as file:
            sp = file.readlines()
            for i in range(len(sp)):
                nl = sp[i].split()
                print(f'В {i + 1}-ой строке {len(nl)} слов(а)')
            print(f'Количество строк в файле: {len(sp)}')
    except FileNotFoundError:
        return 'Файл не найден'
info()
