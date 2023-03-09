"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
"""Открывается созданный заранее файл на чтение"""


def counting_string():
    try:
        with open('file2.txt', 'r') as file:
            text = file.readlines()
            """Считывается количество слов в строке"""
            for i in range(len(text)):
                string = text[i].split()
                print(f"Файл содержит {len(text)} строк. "
                      f"{i + 1}-ая/ья строка содержит {len(string)} слов(а) \n")
    except FileNotFoundError:
        return 'Файл не найден.'


counting_string()
