"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
out_f = open("text_file.txt", "w", encoding='utf-8')
x = 1
while x == 1:
    user_line = input(f'Введите строку:')
    if len(user_line) != 0:
        out_f.write(user_line + "\n")
    else:
        x = 0
out_f.close()
