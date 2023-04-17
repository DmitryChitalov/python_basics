"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

file1 = open('filo1.txt', 'r')
print(f'Количество строк в файле - {len(file1.readlines())}')
file1.close()
file1 = open('filo1.txt', 'r')
content = file1.read()
with open('filo1.txt') as f:
    lines = f.readlines()
print(lines)
print(len(lines))
for i in range(len(lines)):
    print(f"количество слов в строке {i + 1} равно {len(lines[i].split(' '))}")

