"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

f = open("my_file.txt", "w")
while True:
    user_str = input("Enter new string: ")
    if 0 == len(user_str):
        break
    f.write(user_str)

f.close()
