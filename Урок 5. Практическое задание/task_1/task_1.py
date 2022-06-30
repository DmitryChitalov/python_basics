"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

new_file = []
while True:
    line = input("Введите произвольный текст, для выхода введите Q >> ")
    if line == 'Q':
        print(new_file)
        exit()
    else:
        newline = line + '\n'
        new_file.append(newline)

    with open("test.txt", "w") as file_obj:
        file_obj.writelines(new_file)
