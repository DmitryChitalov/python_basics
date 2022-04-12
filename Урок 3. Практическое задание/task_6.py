"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(string):
    if False == isinstance(string, str):
        raise Exception("It should be string.")
    word = string.split()
    if 1 != len(word):
        raise Exception("It should be only one word.")
    return string.title()

string = input("Enter string: ")
new_string = ""
words = string.split()
for word in words:
    new_string += (int_func(word))
    new_string += " "

print(new_string)
