"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""
def change_register(my_str):
    s = []
    for word in my_str.split(' '):
        if not word.istitle():
            word = word[0].upper() + word[1:].lower()
            s.append(word)
        else:
            s.append(word)
    return ' '.join(s)

print(change_register("проверка"))

#не успел