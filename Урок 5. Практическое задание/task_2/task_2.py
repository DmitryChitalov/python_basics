"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


with open("random_text.txt", 'r', encoding='utf_8') as f:
    my_lines = f.readlines()
print(f'Количество строк в файле: {len(my_lines)}')
count = 0
for line in my_lines:
    count += 1
    res = line.split()
    print(f'В строке №{count} всего {len(res)} слов(-а)')

