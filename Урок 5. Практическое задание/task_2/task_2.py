"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('Dz_2.txt', 'r', encoding='utf-8') as Dz:
    # Построчное чтение файла Dz
    tex_t = Dz.readlines()
    line = len(tex_t)
    print(f'Общее количество строк: {line}')

    for ele in tex_t:
        elem = ele.split()
        elem_count = len(elem)
        print(f'Количество слов в данной строке "{ele.strip()}": {elem_count}')

