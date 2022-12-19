"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
f_obj = open("file.txt", 'w', encoding='utf-8')
lines = []
while True:
    line = input("Enter smth: ")
    if line != "":
        lines.append(line + "\n")
    else:
        break
f_obj.writelines(lines)
