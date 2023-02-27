"""
1) Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

my_f = open("Task1.txt", "w", encoding='utf-8')
str_list = input("")
while str_list != "":
    str_list = input("")
    if str_list == "":
        break
    else:
        my_f.writelines(str_list)