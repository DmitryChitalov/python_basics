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
my_list = input("Введите слова через пробел: ").split(' ')
a = 1
for el in my_list:
    if len(el) > 10:
        print(f'{a}. {el[:10]}')
    else:
        print(f'{a}. {el}')
    a += 1