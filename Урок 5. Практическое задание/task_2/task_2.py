"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("file_2.txt", "r") as my_file:
    text_file = my_file.read()
    words = len(text_file.split())
    print("Количество слов: ", words)
with open("file_2.txt", "r") as my_file:
    lines = len(my_file.readlines())
    print("Количество строк: ", lines)
