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
user_string = input('Введите слова через пробел: ')
words_in_List = user_string.split(" ")
counter = 1
for word in words_in_List:
    print(f'{counter}. {word[:10]}')
    counter += 1

