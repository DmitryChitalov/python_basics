"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("text.txt", "r") as usr_file:
    print(f'Количество строк в файле: {len(usr_file.readlines())}')

count = 1
with open("text.txt", "r") as usr_file:
    for line in usr_file:
        print(f'Количество слов строке {count}: {len(line.split())}')
        count += 1