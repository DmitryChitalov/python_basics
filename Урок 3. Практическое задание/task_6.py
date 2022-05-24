"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word_in_lower_case):
    return word_in_lower_case.capitalize()


def int_func_part2(words_in_lower_case):
    result_str = " "
    words_arr = words_in_lower_case.split()
    for i in range(len(words_arr)):
        words_arr[i] = int_func(words_arr[i])
    return result_str.join(words_arr)


word = input("Введите слово строчными буквами: ")
print(f"Result: {int_func(word)}")

words = input("Введите несколько слов строчными буквами: ")
print(f"Result: {int_func_part2(words)}")
