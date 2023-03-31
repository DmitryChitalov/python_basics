"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
total_line = 0
try:
    with open("test_file.txt") as f_obj:

        for line in f_obj:
            total_line += 1
            print(f"в строке № {total_line} слов: {len(line.split(' '))}")

        print(f"строк в файле: {total_line}")
except IOError:
    print("проблема с открытием файла. возможно его нет")


