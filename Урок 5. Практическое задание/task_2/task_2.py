"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
from itertools import count

with open("text.txt", "r") as f_obj:
    counter = 0
    counter_split = 1
    while True:
        content = f_obj.readline()
        if content == "":
            break
        content_split = content.split(" ")
        print(f"Кол-во слов в строке {counter_split}: {len(content_split)}")
        counter += 1
        counter_split += 1
    print(f"Кол-во строк: {counter}")


