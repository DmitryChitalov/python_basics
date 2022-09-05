"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

f_obj = open('file.txt', 'w', encoding='utf8')
strings = []
while True:
    string = input('Введите текст или нажмите Enter: ')
    if string != '':
        strings.append(string + '\n')
    else:
        break
f_obj.writelines(strings)
f_obj.close()

with open('file.txt', 'r', encoding='utf8') as my_file:
    for line in my_file:
        print(line)