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
my_lst = input('Укажите слова через пробел: ').split()
n = 1
for el in my_lst:
    if len(el) > 10:
        print(f'{n}. {el[:10]}')
    else:
        print(f'{n}. {el}')
    n += 1
print()
