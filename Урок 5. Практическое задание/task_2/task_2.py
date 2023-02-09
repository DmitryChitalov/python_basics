"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
first_f = open("first_file.txt", "r", encoding='utf-8')
lines = first_f.readlines()
count = 0
for line in lines:
    count += 1
    print(f"Line: {count} count: {len(line.split())}")
print(f"Total lines: {count}")
