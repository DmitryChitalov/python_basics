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
word_list = words.split()
for i, word in enumerate(word_list):
    if len(word) > 10:
        word = word[:10]
    print(f"{i+1}. {word}")
