"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
try:
    with open("test_file.txt", encoding="utf-8") as f_obj:
        lines_count = 0
        for line in f_obj:
            lines_count += 1
            words_count = len(line.split(" "))
            print(f"слов в строке {lines_count}: {words_count}")
        print(f"строк в файле: {lines_count}")
except IOError:
    print("Произошла ошибка ввода вывода!")
