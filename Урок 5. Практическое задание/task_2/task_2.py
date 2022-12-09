"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

file_in = 'my_text.txt'

with open(file_in, 'r', encoding="UTF-8") as fl:
    more_lines = fl.readlines()

print(f"Всего строк в документе - {len(more_lines)}")
for line in more_lines:
    if len(line.split(' ')) == 1:
        print(f"{len(line.split(' '))} - слово в этой строке")
    else:
        print(f"{len(line.split(' '))} - слов(а) в этой строке")
