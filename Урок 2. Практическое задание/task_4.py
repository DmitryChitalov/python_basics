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
i = 0
list = input().split()
for word in list:
    i += 1
    if len(str(word)) > 10:
        print("<", i, "строка >", str(word)[0:10])
    else:
        print("<", i, "строка >", word)