"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("user_text.txt", "r") as usr_file:
    print(f'Количество строк в файле: {len(usr_file.readlines())}')

with open("user_text.txt", "r") as usr_file:
    for line in usr_file:
        print(f'Количество слов в этой строке: {len(line.split())}')