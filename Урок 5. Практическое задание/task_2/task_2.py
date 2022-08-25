"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('test.txt', "w", encoding="utf-8") as f_obj:
    str_list = ['stroka_1 stroka_1''\n', 'stroka_2 stroka_2 stroka_2''\n',
                'stroka_3']
    f_obj.writelines(str_list)

with open('test.txt', 'r', encoding="utf-8") as f_obj:
    content = f_obj.read()
content = content.split('\n')
for i in range(len(content)):
    new_list = content[i].split()
    print(f'В файле {len(content)} строк(и). '
          f'В {i + 1} строке {len(new_list)} слов(а)')







