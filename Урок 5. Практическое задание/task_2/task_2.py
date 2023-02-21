"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("less5_t2_block.txt", "r", encoding='utf-8') as txt:
     l_strings = [line.split() for line in txt.readlines()]  
     print(f'В файле {len(l_strings)} строк(и)')

for string, words in enumerate(l_strings):
     print(f'В строке {string + 1} - {len(words)} слов(а)'
