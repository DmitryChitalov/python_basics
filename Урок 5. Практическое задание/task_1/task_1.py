"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
s = input('Введите текст. Для окончания введите пустую строку: ')
with open("output.txt", "w", encoding='utf-8') as file:
    file.write(s + '\n')
while s:
    s = input()
    with open("output.txt", "a", encoding='utf-8') as file:
        file.write(s + '\n')
