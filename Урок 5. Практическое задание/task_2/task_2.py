"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
lines = 0
try:
    with open('test.txt', 'r') as my_file:
        for line in my_file:
            lines += 1
    print(f'Кол-во всех строк {lines}')
except FileNotFoundError:
    print(f"FileNot Found")
