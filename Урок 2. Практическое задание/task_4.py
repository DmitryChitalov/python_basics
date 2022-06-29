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
words = words.split(" ")
line_number = 0

for word in words:
    line_number += 1
    res = word[0:10] if len(word) > 10 else word
    print(f'{line_number}. {res}')



