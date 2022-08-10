"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
7. Продолжить работу над заданием. В программу должна попадать строка
из слов, разделённых пробелом. Каждое слово состоит из латинских букв
в нижнем регистре. Нужно сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().
"""


def int_func(text):
    """Изменение первой буквы в слове"""
    return text.capitalize()


def text_cap(text):
    """Функция перебора каждого слова и преобразования первой буквы слова"""
    word_list = text.split(' ')
    for i, j in enumerate(word_list):
        word_list[i] = int_func(j)

    return ' '.join(word_list)




def title_func():
    """Второй вариант решения задачи 6 и 7"""
    text_list = input("Введите слово или текст: ")
    return text_list.title()


second_text = input("Введите слово: ")
print(f'Вывод функции int_func: {int_func(second_text)}')
next_text = input("Введите текст: ")
print(f'Вывод функции int_func: {text_cap(next_text)}')
print(title_func())
