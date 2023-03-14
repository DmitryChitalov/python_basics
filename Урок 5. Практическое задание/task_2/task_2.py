"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
try:
    with open("new_file.txt", 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(f'Количество строк в файле: {len(lines)}')
        word_cnt = 0
        for line in lines:
            print(f'Количество слов в строке {lines.index(line)+1}: {len(line.split())}')
            word_cnt += len(line.split())
        print(f'Количество слов в файле: {word_cnt}')
except IOError:
    print("Ошибка ввода-вывода!")
