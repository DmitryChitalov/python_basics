"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def getStringsCount(c):
    return [f'Количество слов в {c.index(el) + 1} строке - {len(el.split(" "))}' for el in c]


with open('text.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    print('Количество строк в файле:', len(content))
    for item in getStringsCount(content):
        print(item)
