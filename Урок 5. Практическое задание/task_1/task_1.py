"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

my_file = open("c:\Python38\\text1.txt", "w", encoding="utf-8")
print("Введите данные в файл (пустая строка - окончание ввода)")
while True:
    text_str = input(">")
    if text_str == "":
        break
    my_file.write(text_str + "\n")
my_file.close()
print("Данные сохранены в c:\Python38\\text1.txt")
