"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

source_file = open("file1.txt", "w", encoding='utf-8')
change_file = input("Введите текст")
while change_file:
    source_file.writelines(change_file + "\n")
    change_file = input("Введите текст")
    if change_file == "":
        break

source_file.close()
