"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

new_txt = open('file_text.txt', 'r', encoding='utf-8')

text = new_txt.readlines()
print(f'Количество строк в файле - {len(text)}')

for i in range(len(text)):
    print(f'Кол-во символов {i + 1}-ой строки {len(text[i])}')
    print(f'Общее количество слов - {len(text[i].split())}')

new_txt.close()