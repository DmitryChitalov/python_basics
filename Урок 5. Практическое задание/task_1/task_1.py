"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
the_line = str(print("Начнем"))

out_f = open(r"D:\DevOps\Python\Урок5\test2.txt", "w+")
while the_line[0] != "":
    try:
        the_line = str(input("Введите данные или ничего для выхода: "))
        out_f.write(str({the_line}))
    except IndexError:
        print("the end")
out_f.close()