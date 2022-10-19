"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def my_capitalize_lat(word):
    """
    принимает слово из маленьких латинских букв и возвращающую его же,
    но с прописной первой буквой.
    """
    sym_list = list(word)
    code_small_a = ord('a')
    code_small_z = ord('z')
    code_big_a = ord('A')
    code_big_z = ord('Z')
    sym_shift = code_small_a - code_big_a

    for index, sym in enumerate(sym_list):
        sym_code = ord(sym)
        if sym_code < code_big_a or (code_big_z < sym_code < code_small_a) or \
                sym_code > code_small_z:
            return None
        if index == 0:
            if code_small_a <= sym_code <= code_small_z:
                sym_code -= sym_shift
        elif code_big_a <= sym_code <= code_big_z:
            sym_code += sym_shift

        sym_list[index] = chr(sym_code)

    return ''.join(sym_list)


print(my_capitalize_lat("text"))
print(my_capitalize_lat("bla1k"))

words = input("Введите слов из латинских букв в нижнем регистре через пробел: ")
for word_str in words.split(' '):
    transformed = my_capitalize_lat(word_str)
    if transformed is None:
        print(f"В слове '{word_str}' есть не латинская буква")
        break
    print(f"{transformed} ", end='')
