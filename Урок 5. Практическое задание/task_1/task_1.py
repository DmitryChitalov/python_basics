"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

import fileinput

print("Введите данные:")
for user_input in fileinput.input():
    if '' == user_input.rstrip():
        break
    with open('user_input.txt', 'a') as file:
        file.write(user_input)
print(f"Ваши данные записаны в файл {file.name}")
