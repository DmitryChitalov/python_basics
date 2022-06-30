"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('task2.txt') as f:
    strings = f.readlines()
    expanded_strings = [string.split() for string in strings]

strings_count, words_count = len(strings), sum([len(word_list) for word_list in expanded_strings])

print(f"Количество строк - {strings_count}, количество слов - {words_count}")
