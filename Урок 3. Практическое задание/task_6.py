"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""
def int_func(word: str):
    first_char = word[:1]
    big_first_char = first_char.upper()
    tail = word[1:]
    return big_first_char + tail


def int_func_ext(row: str):
    result = []
    words = row.split(' ')
    for item in words:
        result.append(int_func(item))
    return ' '.join(result)


s = input("Введите строку для преобразования:\n")
print(int_func_ext(s))
