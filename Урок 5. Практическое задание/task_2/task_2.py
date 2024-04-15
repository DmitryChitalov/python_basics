"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
my_f = open("task2_lesson5.txt", "r")
print(my_f.read())

my_f = open("task2_lesson5.txt", "r")
lines = 0
words = 0
numb = 1

for line in my_f:
    print(f'{numb}-я строка содержит слов - {len(line.split())}')
    words += len(line.split())
    lines += 1
    numb += 1

print(f"Количество строк в файле - {lines}")
print(f"Общее количество слов в файле - {words}")

my_f.close()


