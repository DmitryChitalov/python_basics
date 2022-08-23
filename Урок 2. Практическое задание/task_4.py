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
words_list = input("Введите слова через пробел: ").split()
seq_num = 1
for elem in words_list:
    if len(elem) > 10:
        print(f"{seq_num}. {elem[:10]}")
    else:
        print(f"{seq_num}. {elem}")
    seq_num += 1
