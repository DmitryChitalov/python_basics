"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


test_file = open("test_file_1.txt", "w+")
lines = []
while True:
    s = input("Введите строку: ")
    if s != '':
        lines.append(s)
    else:
        break

for _ in lines:
    test_file.write(_+'\n')
