"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open("m_file.txt", "w", encoding='utf-8') as f_obj:
    lin_dan = []
    while True:
        str_line = input("Новые данные или ENTER: ")
        if str_line != '':
            lin_dan.append(str_line + "\n")
        else:
            break
    f_obj.writelines(lin_dan)
