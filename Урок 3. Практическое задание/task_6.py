"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(str_param):
    tmp = str_param[0]
    tmp = tmp.upper()
    str_param = str_param[:0] + tmp + str_param[1:]
    return str_param


print("Первая часть задания:")
print(f"Было: word\nСтало: {int_func('word')}")

orig_string = "word and some other things"

tmp_word = ""
result_string = ""
for el in orig_string:
    if el != " ":
        tmp_word += el
    else:
        tmp_word = int_func(tmp_word)
        result_string = result_string + tmp_word + " "
        tmp_word = ""

if tmp_word != "" or tmp_word != " ":
    tmp_word = int_func(tmp_word)
    result_string = result_string + tmp_word + " "

print("\nВторая часть задания:")
print(f"Было: {orig_string}\nСтало: {result_string}")
