"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("test.txt") as f_obj:
    num_str = 0
    for line in f_obj:
        num_str += 1
        num_words = line.count(" ") + 1
        print(f"Строка № {num_str}: {line} - {num_words} слов.")

print(f"Итого строк в файле: {num_str}")


