"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("file_1.txt", "r", encoding="utf-8") as f_obj:
    content = f_obj.read()
    content_lst = content.split("\n")

    print(f"Всего строк: {len(content_lst)}")
    for i in content_lst:
        print(f"Строка {content_lst.index(i) + 1} -> Количество слов:{len(i.split())} --> {i}")
