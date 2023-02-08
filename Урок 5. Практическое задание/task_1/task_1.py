"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


my_file = open('test.txt', 'w', encoding="utf-8")
while True:
    new_line = input('Введите текст в строку: \n')
    my_file.writelines(f"{new_line}\n")
    if not new_line:
        break
my_file.close()

