"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(var_str):
    if len(var_str) == 0:
        return ""
    var_str_0 = var_str[0].upper()
    return var_str_0 + var_str[1:]
    # return var_str.title()


print(int_func("first word"))
var_str = "second word"
lst = var_str.split()
res_str = ""
for i in lst:
    separator = " " if res_str != "" else ""
    res_str = res_str + separator + int_func(i)
print(res_str)
