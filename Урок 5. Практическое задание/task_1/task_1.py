"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
str_list = []
while True:
    new_str = input("Введите строку (Enter для выхода):")
    if new_str != '':
        str_list.append(new_str + "\n")
    else:
        break
first_f = open("first_file.txt", "w", encoding='utf-8')
first_f.writelines(str_list)
first_f.close()
