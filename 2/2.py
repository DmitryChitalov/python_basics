"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('file_for_task.txt', 'r', encoding='utf-8') as f_obj:
    count_dict = {}

    for idx, line in enumerate(f_obj, 1):
        count_dict[idx] = len(line.split())

for key, val in count_dict.items():
    print(f'В строке {key} количество cлов {val}')
