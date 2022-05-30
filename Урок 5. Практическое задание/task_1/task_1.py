"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
new_list = []
while True:
    new_line = input('Enter any text to add txt: ')
    if new_line == '':
        print(new_list)
        exit()
    else:
        other_line = new_line + '\n'
        new_list.append(other_line)
    with open("text1.txt", "w") as file_obj:
        file_obj.writelines(new_list)
