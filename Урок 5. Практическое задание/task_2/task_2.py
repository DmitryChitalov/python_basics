"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
my_file = open('file.txt', 'r')
content = my_file.readline()
print(len(content) - 2)

my_file.close()


my_file = open('file.txt', 'r')
content = my_file.readline()
for i in range(len(content)-2):
    print(f'{i + 1} {len(content[i])}')

my_file = open('file.txt', 'r')
content = my_file.read().split()
print(len(content))
