"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("lesson5-2.txt", "r", encoding="utf-8") as f_obj:
    lines = 0
    words = 0
    n = 0
    for line in f_obj:
        lines = lines + line.count("\n")
        n = n + 1
        words = len(line.split(" "))
        print(f"Количество слов в {n} строке = {words}")
    print(f"Строк в тексте - {lines}")