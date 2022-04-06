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

str = input("Введите несколько слов через пробел: ")
words: list = []
substr = ""
i = 1

for el in str:
    if el != " ":
        substr += el
    elif substr != " " or substr != "" or el == "\n":
        words.append(substr)
        substr = ""

if substr != " " or substr != "":
    words.append(substr)

for word in words:
    print(f"{i}. {word[:10]}")
    i += 1

