"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def string(text_input):
    str2 = str(text_input)
    total = ""
    while str2 != "":
        total = f'{total}{str2}\n'
        str2 = input()
    my_file = open("task1_leeson5.txt", "a")
    my_file.write(total)
    my_file.close()
    return total

print(string(input()))


