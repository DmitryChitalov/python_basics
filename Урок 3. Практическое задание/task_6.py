"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

# часть 1
def int_func(string):
    return string.title()

def title_func(string):
    list_text = list(text)
    list_text[0] = list_text[0].upper()
    return ''.join(list_text)

data = []

for word in input('Введите слова которые разделены пробелами: ').split(' '):
    data.append(int_func(word))

print(f'Вывод: {" ".join(data)}')
