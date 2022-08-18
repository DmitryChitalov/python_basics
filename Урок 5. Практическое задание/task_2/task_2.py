"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("my_file.txt", 'r', encoding='utf-8') as f_obj:
    content = f_obj.readlines()
    print(f"Количество строк: {len(content)}")
    for i, line in enumerate(content):
        print(f"Строка {i + 1} содержит {len(line.split())} слов")
