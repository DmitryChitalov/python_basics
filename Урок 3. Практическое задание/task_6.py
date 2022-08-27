"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться
с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


# Тело функции int_func()
def int_func(one_word):
    one_word = one_word.capitalize()
    return one_word


u_quit = 0
new_str = []
while u_quit != "**":
    u_word_list = input("\nВведите латинские слова через пробел: ").split()
    for el in u_word_list:
        if el.isalpha() is True:
            el = el.lower()
            el = int_func(el)
        new_str.append(el)
    print(f"Введенная  строка: {u_word_list}")
    print(f"Полученная строка: {new_str}")
    u_quit = input("Continue - any, Quit - **: ")
