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
my_string = str(input("Введите слова через пробел: "))
my_string_list = list(my_string.split(" "))

for i, el in enumerate(my_string_list):
    print(f"{i + 1}. {el[0:10]}")
