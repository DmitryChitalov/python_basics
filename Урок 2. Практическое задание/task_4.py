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
my_list = list(input("Введите несколько слов через пробел: ").split())
counter = 1
for el in my_list:
    print(f"{counter}. {my_list[counter - 1][:10]}")
    counter += 1
