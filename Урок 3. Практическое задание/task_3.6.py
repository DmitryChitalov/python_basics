"""Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text."""

def int_func():
    a = input("Введите любые слова через пробел: ")
    a = a.title()
    return a
print(int_func())