"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def count_words(some_str):
    words_count = 0
    for el in some_str:
        if el == " ":
            words_count += 1
    if some_str[len(some_str) - 1] != " ":
        words_count += 1
    return words_count


my_file = open('textfile.txt', 'r')

counter = 1
for line in my_file:
    print(f"в {counter}-ой строке {count_words(line)} слов")

my_file.close()