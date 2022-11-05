"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


with open("text.txt", "r", encoding="utf-8") as my_file:
    some_lines = my_file.readlines()

print(some_lines)

i = 0
words = 0
for line in some_lines:
    i += 1
    words += len(line.split())
    print(f"Кол-во слов в строке {i} - {len(line.split())}")
print(f"Всего строк = {i}")
print(f"Всего слов = {words}")
