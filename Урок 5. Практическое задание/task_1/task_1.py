"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open(r"my_random_text_file.txt", "w") as f_obj:
    while True:
        in_text = input()
        f_obj.write(in_text + '\n')
        if in_text == "":
            break
