"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('task_2.txt', encoding='utf-8') as N:
    strings = N.readlines()
    strings = [string.split() for string in strings]


lines = len(strings)
words = sum(len(word_list) for word_list in strings)
print(f"Количество строк - {lines}, количество слов - {words}")
