"""
4. Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.

Пример:
Введите слова через пробел: раз два три
1. раз
2. два
3. три

Введите слова через пробел: раз перерефрижерированность
1. раз
2. перерефриж
"""
words = input("Введите слова через пробел: ")
list_of_words = words.split(' ')
# dict_of_words = [print(f"{i + 1}. " + list_of_words[i][0:9]) for i in range(0, len(list_of_words))]

for ind, el in enumerate(list_of_words, 1):
    print(f"{ind}.", el)
