"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(my_str):
    return my_str.title()


print(int_func('lorem'))


def text_int_func(my_txt):
    list_words = []
    lst = my_txt.split()
    for i in lst:
        list_words.append(int_func(i))
    print(*list_words)


text_int_func('lorem ipsum is simply dummy text of the printing and typesetting industry')
