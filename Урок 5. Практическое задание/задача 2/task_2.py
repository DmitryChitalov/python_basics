"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
my_file = open("mtsuri.txt", "rt")
line_number = 0
for read_line in my_file.readlines():
    if read_line != "\n":
        word_count = len(read_line.split(" "))
        line_number += 1
        print(f"Строка № {line_number}, в ней всего слов: {word_count}")
print(f"Всего строк: {line_number}")
my_file.close()
