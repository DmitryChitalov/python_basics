"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
my_file = open("../task_2/my_first_file.txt", "a")

text_line = None
i = 1
while text_line != "":
    text_line = input(f"{i}. ")
    i += 1
    my_file.write(text_line + "\n")
my_file.close()
