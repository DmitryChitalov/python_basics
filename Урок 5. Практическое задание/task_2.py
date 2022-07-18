"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
lines = 0
words = 0
with open("file2.txt", "r", encoding='utf-8') as my_f:
    print("Количество слов в каждой строке:")
    for line in my_f:
        lines += 1
        words += len(line.split())
        print(f"Строка {lines} содержит: {words} слов")
        words = 0
print(f"Всего строк в файле: {lines}")

