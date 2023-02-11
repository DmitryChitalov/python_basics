"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
# решение через построчное чтение
with open('lesson5_task2_text.txt', 'r', encoding='utf-8') as txt:
    current_line = 0  # начальное значения счетчика строк
    for line in txt:  # перебор строк в файле
        current_line += 1
        numbers_of_words = len(line.split())  # подчет числа слов в строке
        print(f'В строке {current_line} - {numbers_of_words} слов')
    print(f'Всего в файле {current_line} строк')

print()  # пустая строка для отделения решений

# решение через readlines
with open('lesson5_task2_text.txt', 'r', encoding='utf-8') as txt:
    list_of_strings = [line.split() for line in txt.readlines()]  # создание вложенного списка слов в списке строк

print(f'Всего в файле {len(list_of_strings)} строк')
for string, words in enumerate(list_of_strings):
    print(f'В строке {string + 1} - {len(words)} слов')
