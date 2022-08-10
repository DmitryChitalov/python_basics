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

# Выводим название программы
print(f'Программа вывода каждого эмента на новую строку')

# Запрашиваем набор слов
words = input('Введине несколько слов: ').split()

# выводим каждое слово в отдельную строчку
index_word = 1
for word_from_list in words:
    print(f'{index_word}.{word_from_list[:10]}')
    index_word += 1
