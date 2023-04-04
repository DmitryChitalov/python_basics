"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
out_file = open("task_file1.txt", "w", encoding="utf8")

inp_str = " "
while inp_str != "":
    inp_str = input("Введите строку с данными: ")
    if inp_str == "":
        break
    else:
        out_file.write(inp_str)
        out_file.write("\n")
out_file.close()