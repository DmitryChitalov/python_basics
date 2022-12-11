"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_file = open("../task_1/task1_file.txt", "rt")
line_num = 0
for read_line in my_file.readlines():
    if read_line != "\n":
        word_count = len(read_line.split(" "))
        line_num += 1
        print(f"Строка № {line_num}, всего слов: {word_count}")
print(f"Всего строк: {line_num}")
my_file.close()