"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(input_text):
    """
    Возвращает введенное слово с заглавной буквы
    :param input_text: введенное слово - латинский
    :return: Слово с заглавной буквой
    """
    try:
        return input_text.capitalize()

    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")


print(int_func("text"))
print(int_func("future"))


def text_title(input_string):
    """
    Возвращает слова строки с заглавной буквы
    :param input_string: строка текста
    :return: строка текста, где каждое слово выводится с заглавной буквы
    """
    out_string = ""
    try:
        for el in input_string.split(" "):
            out_string += " " + int_func(el)
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
    return out_string


q = input("Введите слова, разделенные пробелом: ")
print(text_title(q))
