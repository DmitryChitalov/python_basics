"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('file.txt', encoding='utf-8') as file:
    files = file.readlines()  # Создает список из строк
    length_str = len(files)  # Записывает кол-во элементов списка

print(f'В файле file.txt {length_str} строк')
for i in range(length_str):
    print(f'В строке {i+1} = {len(files[i])-1} cимволов.')
