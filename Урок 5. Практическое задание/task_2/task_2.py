"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('text_file_2.txt', encoding='utf-8') as my_f:
    x = 0
    for line in my_f:
        x += 1
        my_list = line.split(' ')
        y = len(my_list)
        print(f"{line} Количество слов в строке: {y}\n")
    print(f"Количество строк: {x}")
my_f.close()
