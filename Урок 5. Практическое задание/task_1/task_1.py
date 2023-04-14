"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


my_file = open("text.txt", "w+")
user_text = 1
while user_text != "":
    user_text = input()
    my_file.write(user_text)
    my_file.write("\n")
my_file.close()
