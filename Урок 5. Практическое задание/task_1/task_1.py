"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
my_fl = open("01.txt", "w")

my_text = input('enter your text or press enter for exit: ')
my_fl.write(f"{my_text}\n")

while my_text != "":
    my_text = input('enter your text or press enter for exit: ')
    my_fl.write(f"{my_text}\n")

my_fl.close()
