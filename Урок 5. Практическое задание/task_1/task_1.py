"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

my_file = open("task1_file.txt", "w", encoding='utf-8')
text_in = None
i = 1
while text_in != "":
    text_in = input(f"{i}. ")
    i += 1
    my_file.write(text_in + "\n")
my_file.close()