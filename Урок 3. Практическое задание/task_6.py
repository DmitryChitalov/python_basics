"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


# Вариант 1
def upper_words(some_string):
    words = some_string.split()
    upper_words = [word.capitalize() for word in words]
    return " ".join(upper_words)


some_string = input("Введите строку из слов на латинице, разделенных пробелом: ")
final_string = upper_words(some_string)
print(final_string)

# Вариант 2
'''
def upper_words(some_string):
    return some_string.title()
some_string = input("Введите строку из слов на латинице, разделенных пробелом: ")
final_string = upper_words(some_string)
print(final_string)
'''
