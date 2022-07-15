"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("file_2.txt") as file_obj:
    LINES = 0
    WORDS = 0
    for line in file_obj:
        LINES += line.count("\n")
        WORDS = len(line.split())
        print(f"Количаство слов в строке номер {LINES} равно {WORDS}")
    print(f"Количество строк в файле - {LINES}")
