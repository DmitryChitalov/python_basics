"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
new_line = 1
str_list = []
while new_line != '':
    new_line = input('Введите данные для записи или оставьте поле пустым, чтобы закончить: ')
    if new_line != '':
        str_list.append(new_line+'\n')
with open('text_file.txt', 'a') as file:
    file.writelines(str_list)


