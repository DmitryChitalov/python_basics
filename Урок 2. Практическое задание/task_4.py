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

string = input("input words through space: ").split(' ')
print(string)
for ind, el in enumerate(string, 1):
    if len(el) > 10:
        print(f"{ind}.  {el[0:10]}")
    else:
        print(f"{ind}.  {el}")
