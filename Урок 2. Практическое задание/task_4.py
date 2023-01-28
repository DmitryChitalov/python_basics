"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
 Вывести каждое слово с новой строки.
 Строки нужно пронумеровать.
 Если слово длинное, выводить только первые 10 букв в слове.
"""
string_from_user = input("Введите строку из нескольких слов, разделённых пробелами : ")
list_of_words = string_from_user.split(sep=None, maxsplit=-1)
print(string_from_user)
print(list_of_words)
for index in range(len(list_of_words)):
    if len(list_of_words[index]) > 10:
        print(f"{index + 1}. {list_of_words[index][:10]}")
    else:
        print(f"{index + 1}. {list_of_words[index]}")
