"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
lines = 0
with open("vv_file.txt", "r", encoding='utf-8') as file:
    for line in file:
        lines += 1
        words = len(line.split())
        print(f"Количество слов в строке {lines}: {words}")
    print(f"Строк в файле: {lines}")
