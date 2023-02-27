"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

test_text = open('test_text.txt', 'r', encoding='utf-8')
counter = 0
word_counter = 0
for line in test_text:
    counter += 1
    word_count = len(line.split())
    word_counter += word_count
    print(f'Слов в строке №{counter} - {word_count}.')
print(f'Всего в тексте {counter} строк и {word_counter} слов.')
