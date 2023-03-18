a = open("file1.txt", "r", encoding="utf-8")
b = a.readlines()
print(b)
print(f"Колличество строк {len(b)}")
d = 1
for el, el2 in enumerate(b):
    list1 = el2.split()
    c = 0
    for el in enumerate(list1):
        c += 1
    print(f"Слов в {d}-ой строке - {c}")
    d += 1
a.close()

# Не получается посчитать колличество слов(

"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
