"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

import re

try:
    with open("t2.txt", "r", encoding="utf-8") as t_obj:
        print(t_obj.read())
        print('')
    with open("t2.txt", "r", encoding="utf-8") as t_obj:
        cont = t_obj.readlines()
        print(f"Количество строк в файле: {len(cont)}")
        res = [print("В", i + 1, "строке", len(re.findall(r"\w+", cont[i])),
                     "слов(а).") for i in range(len(cont))]
except FileNotFoundError:
    print("Файл не найден!")