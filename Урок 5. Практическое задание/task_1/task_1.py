"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
xt_file = open("text.txt", "w+")
user_text = 1
while user_text != "":
    user_text = input()
    txt_file.write(user_text)
    txt_file.write("\n")
txt_file.close()