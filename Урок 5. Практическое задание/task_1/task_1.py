from func import write_file

"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


while True:
    my_text = input("Введите строку текста: ")
    if len(my_text) < 1:
        break
    else:
        write_file("my_file.txt", my_text + "\n")



