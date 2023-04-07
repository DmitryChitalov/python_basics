
"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""
def int_func(*args):
    word = input("Type words: ")
    print(word.title())
    return
int_func()



def my_func(word):
    separated_word = word.split(' ')
    final = []
    for i in separated_word:
        words = str(i)
        res = words[:1].upper() + words[1:]
        final.append(res)
    return final
print(my_func("small big"))
