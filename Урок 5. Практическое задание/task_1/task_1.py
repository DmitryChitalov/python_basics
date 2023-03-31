"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
out_file = open("out_file.txt", "w")

inp_str = " "
while inp_str != "":
    inp_str = input("Введите строку для записи в файл: ")
    if inp_str == "":
        break
    else:
        out_file.write(inp_str)
        out_file.write("\n")
out_file.close()
