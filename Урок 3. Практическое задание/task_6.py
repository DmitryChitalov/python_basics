"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

def my_func(text):
    word = text.split()
    total = []
    for i in word:
        string_el = str(i)
        first_letter = string_el[:1].upper()
        word = first_letter + string_el[1:]
        total.append(word)
    return total

print(my_func('hjdndn jkdjhx jjdnnd')) 
