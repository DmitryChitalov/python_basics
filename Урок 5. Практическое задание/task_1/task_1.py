"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open("task1.txt", "w", encoding = "utf-8") as file:
    while True:
        input_str = input()
        if input_str != "":
            file.write(f"{input_str}\n")
        else:
            break
