"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('result.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    print(f'Количество строк: {len(data)}')
    i = 1
    for el in data:
        words = el.split(' ')
        print(f'Слов в строке {i}: {len(words)}')
        i += 1
    