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
num = 1
my_list = []
str = input('Введите слова через пробел')
for i in range(str.count(' ') + 1):
    my_list = str.split( )
    if len(my_list[i]) <=10:
        print(f'{num}. {my_list[i]}')
        num+=1
    else:
        print(f'{num}. {my_list[i][:10]}')
        num += 1






