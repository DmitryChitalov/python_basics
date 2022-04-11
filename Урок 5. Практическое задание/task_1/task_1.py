"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

my_file1 = open("text1.txt", "w", encoding="utf-8")
str = input("Введите текст:" + '\n')
while str:
    my_file1.writelines(str)
    str = input("Введите текст:" + '\n')
    if not str:
        break
my_file1.close()
