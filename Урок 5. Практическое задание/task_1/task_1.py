"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

sp = []
while True:
    line = input("Введите что-нибудь или нажмите 'Enter': ")
    if line == '':
        print(sp)
        exit()
    else:
        newline = line + '\n'
        sp.append(newline)

    with open("test.txt", "w") as file_obj:
        file_obj.writelines(sp)
