"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

count = 0
with open('file_2.txt', 'r') as f:
    line = f.readlines()

    for el in line:
        if len(el) > 1:
            count += 1
            ls = el.split()
            if len(ls) == 1:
                print(f'Word  count is: {len(ls)} in line № {count}')  # if 1 word
            else:
                print(f'Words count is: {len(ls)} in line № {count}')  # > 1 words in line
    print(f'Total count of lines is: {count}')

"""
file_2.txt

Word verb dict
Planet space
"""
