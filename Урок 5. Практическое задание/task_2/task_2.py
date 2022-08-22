"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_file = open("text4.txt", "r", encoding="utf-8")

number_of_text = []

while True:
    line = my_file.readline()
    if not line:
        break
    number_of_text.append(len(line.split()))
my_file.close()

print(f"Всего строк в файле {len(number_of_text)}")
for i, value in enumerate(number_of_text):
    print(f"Строка {i + 1} слов {value}")
