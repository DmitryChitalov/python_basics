"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
s = input('Введите текст. Для окончания введите пустую строку: ')
with open("out_file.txt", "w", encoding='utf-8') as file:
    file.write(s + '\n')
while s:
    s = input()
    with open("out_file.txt", "a", encoding='utf-8') as file:
        file.write(s + '\n')
