"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('les5_task2_text.txt', 'r', encoding='utf-8') as txt:
    list_of_strings = [line.split() for line in txt.readlines()]  # создание вложенного списка слов в списке строк

print(f'Всего в файле {len(list_of_strings)} строк')
for string, words in enumerate(list_of_strings):
    print(f'В строке {string + 1} - {len(words)} слов')
