"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""
#task 1
def int_func(usr_inp):
    return usr_inp.title()

#task 2
def text_func(usr_inp_str):
    my_data = []
    my_list = usr_inp_str.split()
    for i in my_list:
        my_data.append(int_func(i))
    return my_data


example_word = 'привет'
example_text = 'с наступающим новым годом!'
#user_input = input('Введите слово: ')

#task 1
print(int_func(example_word))
#task 2
print(*text_func(example_text))







#text_func(example_text)
#print(text_func(*example_text))
#print(int_func(user_input))