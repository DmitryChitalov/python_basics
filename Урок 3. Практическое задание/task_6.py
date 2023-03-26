"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

except_mark = False


def int_func(user_input):
    global except_mark
    while not except_mark:
        try:
            if not user_input.islower():
                except_mark = True
            else:
                return user_input.title()
        except TypeError:
            print("Слова должны содержать только маленькие буквы")
            break


txt_str = ''

user_str = input("Введите для преобразования исходный текст маленькими латинскими буквами через пробел: ").split()

for i in range(len(user_str)):
    while not except_mark:
        try:
            txt_str = txt_str + int_func(user_str[i]) + ' '
            break
        except TypeError:
            print("Слова должны содержать только маленькие буквы")
            break
print(txt_str)
