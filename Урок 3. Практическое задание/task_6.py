"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def uc_first(word):
    """
    Returns the word with the first letter capitalized
    :param str word: word
    :return: Word
    """
    return str(word).title()


def uc_words(func):
    """
    Uppercase the first character of each word in a string
    :param func: uc_first(word)
    :return: string
    :rtype: str
    """
    lst = input('Введите слова через пробел: ').strip().split(' ')
    s = ''
    for i in lst:
        if i != '':
            s += f"{func(i)} "
    print(s)


uc_words(uc_first)
