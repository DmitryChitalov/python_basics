"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


out_f = open("out_file.txt", "w")
out_f.write("String string string")
out_f.close()
print(out_f)
