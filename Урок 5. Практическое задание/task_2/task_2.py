"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('task2.txt', 'r', encoding='utf-8') as f_obj:
    lines = f_obj.readlines()
    print(f"Количество строк: {len(lines)}")
    for el in range(len(lines)):
        words = lines[el].split()
        print(f"Количество слов в строке {el + 1}: {len(words)}")
