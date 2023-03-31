"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
#!/usr/bin/env python3
import os
os.getcwd()
print("Уточняю расположение файла вывода функцией os.getcwd():", os.getcwd())

user_input = " "
output_file = open("./output_file.txt", "w", encoding='utf-8')

while user_input != "":
    user_input = input("Пожалуйста, введите строку для записи в файл. Для окончания ввода Питон ждет пустую строку: ")
    output_file.write(user_input + "\n")

output_file.close()
