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
my_str1 = input("Введите строку из нескольких слов через пробел: ")
my_str1 = my_str1.split()
for ind, el in enumerate(my_str1, 1):
    print(ind, el[0:10])
    
