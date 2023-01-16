"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
my_file = open("test.txt", 'w', encoding='utf-8')
str_list = []

while True:
    user_input = input('Введите текст: ')
    if user_input != '':
        str_list.append(user_input +'\n')
    else:
        break
my_file.writelines(str_list)




